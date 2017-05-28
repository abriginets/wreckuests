## What is this?
Wreckuests is a script, which allows you to run DDoS attacks with HTTP-flood(GET/POST). It's written in pure Python and uses proxy-servers as "bots".

[Download](https://github.com/JamesJGoodwin/wreckuests/releases)

**Warning:** This script is published for educational purposes only! Author will accept no responsibility for any consequence, damage or loss which might result from use.
## Features
* UserAgent substitution
* Referers random generation
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
* [Requests 2.10.0+](https://github.com/kennethreitz/requests)
* [netaddr 0.7.19](https://pypi.python.org/pypi/netaddr)

## Usage
Then, type under **sudo** mode:

`python3 wreckuests.py -t <target url> -a <login:pass>`

**-h**:

Means *help*. Prints a message with possible parameters. 

**-t** or **--target**:

Specifies a link to the victim's site page. It could be the website's main page, someone's profile, `.php`-files or even image. Everything that has a lot of weight or is hard for server to give.

**-a** or **--auth**:

Parameter for bypassing authentication. You'r victim could enable basic HTTP authentication and his website will request to enter login and password in popup window previously published login and password data for his users in VK/FB/Twitter and whatever social network.

*Feel free to contribute*
