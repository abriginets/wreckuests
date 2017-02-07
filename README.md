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

Disadvantages:
* :x: Poor Multithreading Implementation
* :x: No HTTPS Proxy Support
* :x: Can't be stoped over CTRL+C combination(you need to forcibly kill the process in task manager)
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
