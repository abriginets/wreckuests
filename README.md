<p align="center">
  <a href="https://github.com/JamesJGoodwin/wreckuests/releases"><img src="https://raw.githubusercontent.com/JamesJGoodwin/wreckuests/master/logo.png" width="600" height="200" alt="logo"></a>
</p>

## What is this?
Wreckuests is a script, which allows you to run DDoS attacks with HTTP-flood(GET/POST). It's written in pure Python and uses proxy-servers as "bots". OF COURSE, this script is not universal and you can't just drop Pentagon/NSA/whatever website with just a single mouse click. Each attack is unique, and for each website you'd need to search for vulnerabilities and exult them.

**Warning:** This script is published for educational purposes only! Author will accept no responsibility for any consequences, damage or loss which might result from use.
## Features
* Cache bypass with URL parameters randomization
* CloudFlare detection and notification of
* Automatic gzip/deflate toggling
* HTTP Authentication bypass
* UserAgent substitution
* Referers randomizer
* HTTP proxy support

<sup>...and everything else that [kennethreitz/requests](https://github.com/kennethreitz/requests) can do</sup>

## Todo
TODO tasks are given in [Projects](https://github.com/JamesJGoodwin/PYg0odwin/projects/1) section.

## Dependencies
* Python 3.5+
* [Requests](https://github.com/kennethreitz/requests) <sub>2.10.0 or higher</sub>
* [netaddr](https://pypi.python.org/pypi/netaddr) <sub>tested with 0.7.19</sub>

## Installation
Just clone repository in the disired directory and run the installation script:

```bash
chmod +x install.sh
./install.sh
```

## Usage
Type under *sudo* mode:

`python3 wreckuests.py -v <target url> -a <login:pass> -t <timeout>`

### Possible parameters:

`-h` or `--help`:

Prints a message with possible parameters. 

`-v` or `--victim`:

Specifies a link to the victim's site page. It could be the website's main page, someone's profile, `.php`-file or even image. Everything that has a lot of weight or is hard for server to give. The choice is yours.

`-a` or `--auth`:

Parameter for bypassing authentication. You'r victim could enable basic HTTP authentication and his website will ask you to enter login and password in popup window. Victim may previously publish login and password data for his users in VK/FB/Twitter and whatever social network.

`-t` or `--timeout`(defalut: 10):

Parameter to control connection'n'read timeout. This option also controls terminating time. **Note:** if you set `timeout=1` or somewhere about 2-3 seconds, the slow(but still working) proxies will not have any time to even connect to your victim's website and will not even hit it. If you still do not understand how it works - do not change this option. Also, this parameter regulates the intensiveness of requests you sending. So, if you sure your proxies are fast enough - you can reduce this value. Use this accordingly.

## Important

A separate thread is created for each proxy address. The more proxies you use - the more threads you create. So, please, do not use way too much proxies. Otherwise, the script may exit abnormaly by meeting segmentation fault.

<p align="center">:sparkles: *Feel free to contribute* :sparkles:</p>
