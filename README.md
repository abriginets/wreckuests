![Logo](http://i.imgur.com/ZXQUpbq.png)

## What is this?
PYg0odwin is a script, which allows you to simulate http-flood DDoS atacks on test rounds. It's written in pure Python and uses proxy-servers as "bots".

[Download](https://github.com/JamesJGoodwin/PYg0odwin/releases/tag/0.0.1)

**Warning:** This script is published for educational puproses only! Author will accept no responsibility for any consequence, damage or loss which might result from use.
## Description
Advantages:
* :white_check_mark: UserAgent Substitution
* :white_check_mark: Randomly generated referers with random links and keywords
* :white_check_mark: HTTP Proxy Support
* :white_check_mark: Good perfomance implementation (threads with bad proxies will be stopped to gain some perfomance for threads with good proxies)

Disadvantages:
* :x: No HTTPS Proxy Support
* :x: No Redirection Support

## Dependencies
* Python 3.3+
* [Requests](https://github.com/kennethreitz/requests)

## Files

* `referers.txt` — referers links
* `keywords.txt` — keywords for combining with referers
* `user-agents.txt` — UserAgents
* `proxy.txt` — proxies

## Usage
Type under **sudo** mode:

`python goodwin.py http://example.com`

## Remember
No DDoSing FBI, government, etc...

<sup><sup>From Russia with love</sup></sup>
