#!/usr/bin/env python3

# import module(s)
import netifaces

# define main function
def main():
    for i in netifaces.interfaces():
            print('\n**************Details of Interface - ' + i + ' *********************')
            try:    
                print('MAC: ', end='') # prints MAC without the end of a line
                print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # prints MAC 
                print('IP: ', end='')   # prints IP without the end of a line
                print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # prints IP
            except:
                print('Could not collect adapter information')  # prints and error message
main()
