#!/usr/bin/env python3

def main():
    
    # prompt user for an IP address
    ipchk = input("Set IP address: ")

    # check the string value
    if ipchk == "192.168.70.1":
        print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
    elif ipchk: #if any data is provided, this will test True
        print("Looks like the IP address was set: " + ipchk)
    else:
        print("No input provided")

main()

print("Exiting script")
