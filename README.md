![Logo](http://i.imgur.com/ZXQUpbq.png)

## What is this?
PYg0odwin is a script, which allows you to simulate http-flood DDoS atacks on test rounds. It's written in pure Python and uses proxy-servers as "bots".

[Download](https://github.com/JamesJGoodwin/PYg0odwin/releases)

**Warning:** This script is published for educational puproses only! Author will accept no responsibility for any consequence, damage or loss which might result from use.
## Description
Advantages:
* :white_check_mark: UserAgent Substitution
* :white_check_mark: Randomly generated referers + keywords combinations (1000 keywords * 350 referer links = 350k possible combinations)
* :white_check_mark: HTTP Proxy Support
* :white_check_mark: Good perfomance implementation (threads with bad proxies will be stopped to gain some perfomance for threads with good proxies)

Disadvantages:
* :x: No automatic switching beetwen HTTP and HTTPS proxies(you can define only one type of proxies which will be using during the attack)
* :x: No Redirection Support(301 > 200, etc)

## Todo

* Automatic switching beetwen HTTP and HTTPS proxies
* Redirection Support
* CloudFlare 'Checking your browser' bypass

## Dependencies
* Python 3.3+
* [Requests](https://github.com/kennethreitz/requests)

## Files

* `referers.txt` — referers links
* `keywords.txt` — keywords for combining with referers
* `user-agents.txt` — UserAgents
* `proxy.txt` — proxies

Note: all proxies in this repository has anonimity level elite and anonymous. Some proxies support HTTPS. 

## Usage
Type under **sudo** mode:

`python3 goodwin.py http://example.com`

## Remember
No DDoSing FBI, government, etc...

<sup><sup>From Russia with love</sup></sup>
