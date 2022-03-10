#!/usr/bin/env python3

# create main function
def main():

    # import modules and or define variables
    import csv

    # open working file
    with open("csv_users.txt", "r") as csvfile:
        # counter to create unique file names
        i = 0
        # loop across the open file line by line
        for row in csv.reader(csvfile):
            i = i + 1 # increase i by 1 to create unique file names
            filename = f"admin.rc{i}"

            with open(filename, "w") as rcfile:
                print("export OS_AUTH_URL=" + row[0], file=rcfile)
                print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
                print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
                print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
                print("export OS_USERNAME=" + row[3], file=rcfile)
                print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
                print("export OS_PASSWORD=" + row[5], file=rcfile)

    print("admin.rc files created!")

main()  
