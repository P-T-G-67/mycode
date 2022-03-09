#!/usr/bin/env python3

def main():

    # collect user input for the hostname value
    hostname = input("What value should we set for the hostname?")

    # use the lower method to test if input value matches the expected value
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches the expected config")
    
    # notify user of script completion
    print("Exiting the script")

main()
