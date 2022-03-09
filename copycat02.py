#!/usr/bin/env python3

def main():
    
    # import additional code to complete our task
    import shutil
    import os

    os.chdir("/home/student/mycode/") # move into the working directory

    # copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy the entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

main()

