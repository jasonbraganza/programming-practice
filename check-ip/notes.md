## Problem
- Take a list of domains (one per line) from a text file as input, find the IP address for the domain using the standard system level DNS, and then check against DoH answers from both cloudflare and google. and say if all answers match properly or not.

## Notes  

What do I need to do?
- Get a list of popular websites, (probably Alexa)
- figure out a way to read them in
- get ips for all of them and store them in a dictionary, with the site addresses as keys
    - the sockets module should help to get the ips
- use the requests library to query each site in the dictionary and check the return value, against the value stored in the dict
- Say if they match or not