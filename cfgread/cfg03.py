#!/usr/bin/env python3

# define main function
def main():
    
    # prompt user for configuration file to be read
    config = input("Please enter the configuration filename: ")

    # create file object in read "r" mode
    with open(config, "r") as configfile:
        
        configlist = configfile.readlines()
        
        print(configlist)

main()
