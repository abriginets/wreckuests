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
* :white_check_mark: Good perfomance implementation <sub>(threads with bad proxies will be stopped to gain some perfomance for threads with good proxies)</sub>

Disadvantages:
* :x: No automatic switching beetwen HTTP and HTTPS proxies(you can define only one type of proxies which will be using during the attack)
* :x: No Redirection Support(301 > 200, etc)

## Todo
TODO tasks are given in [Projects](https://github.com/JamesJGoodwin/PYg0odwin/projects/1) section.

## Dependencies
* Python 2.6-2.7 or 3.3+
* [Requests](https://github.com/kennethreitz/requests)

## Usage
First of all, you should install dependencies:

`apt-get install python && apt-get install python-pip && pip install requests`

Then, type under **sudo** mode:

`python3 goodwin.py http://example.com`

**Feel free to make pull requests and report issues.**
