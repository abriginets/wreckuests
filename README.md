![Logo](http://i.imgur.com/ZXQUpbq.png)

## What is this?
PYg0odwin is a script, which allows you to simulate http-flood DDoS atacks. It's written in pure Python and uses proxy-servers as "bots".

[Download](https://github.com/JamesJGoodwin/PYg0odwin/releases)

**Warning:** This script is published for educational puproses only! Author will accept no responsibility for any consequence, damage or loss which might result from use.
## Description
Advantages:
* :white_check_mark: UserAgent substitution
* :white_check_mark: Referers random generations
* :white_check_mark: HTTP proxy support
* :white_check_mark: Good perfomance implementation (threads with bad proxies will be stopped to gain some perfomance for threads with good proxies)

Disadvantages:
* :x: No automatic switching beetwen HTTP and HTTPS proxies(you can define only one type of proxies which will be using during the attack)
* :x: No Redirection Support(301 > 200, etc)

## Todo
* Automatic switching beetwen HTTP and HTTPS proxies
* Redirection Support
* CloudFlare 'Checking your browser' bypass

## Dependencies
* Python 2.6 - 2.7 or 3.3+
* [Requests](https://github.com/kennethreitz/requests)

## Files
* `referers.txt` — referers links
* `keywords.txt` — keywords for combining with referers
* `user-agents.txt` — UserAgents
* `proxy.txt` — proxies

Note: all proxies in this repository has anonimity level elite and anonymous. Some of them support HTTPS as well. 

## Usage
Type under **sudo** mode:

`python3 goodwin.py http://example.com`

## Remember
No DDoSing FBI, government, etc...

<sup><sup>From Russia with love</sup></sup>
