#!/usr/bin/env python3

def main():

    # import tools
    import shutil
    import os

    # set the working directory
    os.chdir('/home/student/mycode')

    # move and rename objects  
    shutil.move('raynor.obj', 'ceph_storage/')
    xname = input('what is the new name for kerrigan.obj? ') # prompt user to rename second object
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # move second object using new name "xname"

main()
