#!/usr/bin/env python3

def main():
    # set variables and file path(s)
    loginfail = 0 # initial failed logins count
    loginsuc = 0 # initial successful logins count    
    # create loop
    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r") as kstone:  # open parse file and auto close
        for line in kstone: 
            if "- - - - -] Authorization failed." in line: # specify search string
                loginfail += 1  # add 1 to our initial 0 value for loginfail variable
            if "-] Authorization failed" in line:
                loginsuc += 1   # add 1 to our initial 0 value for loginsuc variable
    print("The number of failed logon attempts is", loginfail)
    print("The number of successful logon attempts is", loginsuc)
    
main() 
