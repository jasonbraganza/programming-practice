"""
Read in an irc log file and figure out who spoke how many lines
"""
# ask for a file read the file line by line
# somehow figure out nicknames
# if the nick name is encountered for the first time, add it as a key to a dictionary and set its value to 1
# oh, create the darned dictionary
# the next time you read in a nickname, compare to the dict. if it’s in there, increment its value by one. if not, add the nick as a key to the dictionary
# once done, print out who spoke how many lines by looping over the items in the dictionary.

import os


def main():
    nicknames = (
        {}
    )  # creating a dictionary to hold the nicknames and the number of lines they spoke
    # read in a file


if __name__ == "__main__":
    main()
