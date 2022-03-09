#!/usr/bin/env python3

# Define the first function
def main():

    # set variables and dictionaries
    show_dict = {"Sci-fi": "The X-Files", "Comedy": "What We Do in the Shadows"}
    genre = input("Which TV genre(s) do you enjoy?")
    
    # test input value for True
    if genre == "Sci-fi":
        print("Excellent!  You might enjoy " + show_dict["Sci-fi"] + ".")
    elif genre == "Comedy":
        print("Right on!  You might enjoy " + show_dict["Comedy"] + ".")
    else:
        print("You must be fun at parties.")
main()

print("Exiting script")
