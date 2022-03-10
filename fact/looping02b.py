#!/usr/bin/env python3

# open a text file and create a list of lines

with open("dnsservers.txt", "r") as dns_file:
    dns_list = dns_file.readlines()

    for svr in dns_list:
        print(svr, end="")
