"""
Problem to solve: 

Take a list of domains (one per line) from a text file as input, find the IP address for the domain using the standard system level DNS, and then check against DoH answers from both cloudflare and google. and say if all answers match properly or not.

"""
import socket
import requests


def main():
    sites = {}
    with open("dumpsites.txt") as list_of_sites:
        for each_site in list_of_sites:
            each_site = each_site.strip().lower()
            sites[each_site] = socket.gethostbyname(each_site)
    print(sites)


if __name__ == "__main__":
    main()
