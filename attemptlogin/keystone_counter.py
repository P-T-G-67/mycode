#!/usr/bin/env python3

def main():
    # set variable and determine file(s)
    loginfail = 0 # the initial value for our failed login count
    kstone = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r") # path for the file to parse
    kstone_file_lines = kstone.readlines() # readlines specified in order to loop through all lines in the parse file

    # create for loop
    for line in kstone_file_lines: # loop through all lines in parse file
        if "- - - - -] Authorization failed." in line: # search for specific string on each line of parse file
            loginfail += 1 # add 1 to the initial count of 0 for each instance of search string found
    print("The number of failed log in attempts is", loginfail) 
    kstone.close() # close the file
main()
