#!/usr/bin/env python3

def main():
    
    # prompt user for an IP address
    ipchk = input("Set IP address: ")

    # string value returns True
    if ipchk:
        print("Looks like the IP address was set: " + ipchk)
    else:
        print("No input provided")

main()
