#!/usr/bin/env python3

# Import modules
import shutil
import os

# Set the start location of our script
os.chdir("/home/student/mycode/")

# Copy fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# Copy the entire directoryA to directoryB
shutil.copytree("5g_research/", "5g_research_backup/")
