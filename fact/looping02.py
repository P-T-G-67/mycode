#!/usr/bin/env python3

# open a text file and create a list of lines

dns_file = open("dnsservers.txt", "r")
dns_list = dns_file.readlines()

# create a for loop

for svr in dns_list:
    print(svr, end="")

dns_file.close()
