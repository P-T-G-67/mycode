#!/usr/bin/env python3

# define main function
def main():
 
    # Explore read
    configfile = open("vlanconfig.cfg", "r")
    print(configfile.read())
    configfile.close()

    # Explore readlines
    configfile = open("vlanconfig.cfg", "r")
    configlist = configfile.readlines()
    print(configlist)

    # Iterate through configlist
    for x in configlist:
        print(x.strip())
    
    configfile.close()

main()
