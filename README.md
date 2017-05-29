## What is this?
Wreckuests is a script, which allows you to run DDoS attacks with HTTP-flood(GET/POST). It's written in pure Python and uses proxy-servers as "bots".

[Download](https://github.com/JamesJGoodwin/wreckuests/releases)

**Warning:** This script is published for educational purposes only! Author will accept no responsibility for any consequence, damage or loss which might result from use.
## Features
* UserAgent substitution
* Referers randomizer
* Cache bypass with random `?abcd=efg` parameter
* HTTP proxy support
* Automatic gzip/deflate toggling
* CloudFlare detection and notification of
* HTTP Authentication bypass

<sup>...and everything else that [kennethreitz/requests](https://github.com/kennethreitz/requests) can do</sup>

## Todo
TODO tasks are given in [Projects](https://github.com/JamesJGoodwin/PYg0odwin/projects/1) section.

## Dependencies
* Python 3.5+
* [Requests](https://github.com/kennethreitz/requests) 2.10.0 or higher
* [netaddr](https://pypi.python.org/pypi/netaddr) (tested with 0.7.19)

## Usage
Type under **sudo** mode:

`python3 wreckuests.py -t <target url> -a <login:pass>`

**-h**:

Means *help*. Prints a message with possible parameters. 

**-t** or **--target**:

Specifies a link to the victim's site page. It could be the website's main page, someone's profile, `.php`-file or even image. Everything that has a lot of weight or is hard for server to give. The choice is yours.

**-a** or **--auth**:

Parameter for bypassing authentication. You'r victim could enable basic HTTP authentication and his website will ask you to enter login and password in popup window. Victim may previously publish login and password data for his users in VK/FB/Twitter and whatever social network.

**Important note**: A separate thread is created for each proxy address. The more proxies you use - the more threads you create. So, please, do not use way too much proxies. Otherwise, the script may exit abnormaly by meeting segmentation fault.

*Feel free to contribute*
