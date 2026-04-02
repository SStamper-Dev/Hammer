# Hammer
An SSH-bruteforcer using Python

This tool was created using an experiment between two Virtual Machines running Ubuntu with their Network "Attached to" option changed to 'Host-only Adapter'.
It's intended use is for a controlled lab environment, but can deploy across WLAN.
Because of space limits, we cannot provide the text file containing a list of popular passwords.
Google "rockyou.txt" to find it yourself and place it in the same directory as hammer.py (text filename MUST be 'rockyou.txt').

Attacking PC/VM Prerequisites:
Python and its 'paramiko' library installed

Victim PC/VM Prerequisites:
OpenSSH installed and enabled
UFW enabled and set to allow SSH (TCP/Port 22)
