#!/usr/bin/env python3

# open file
with open("dnsservers.txt", "r") as dns_file:
    for svr in dns_file:
        print(svr, end="")
