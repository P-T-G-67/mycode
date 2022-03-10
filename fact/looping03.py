#!/usr/bin/env python3

# import options and create variables
import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")

# set range for loop iteration
for rando in range(howmany):
    print( uuid.uuid4() )

