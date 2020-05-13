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
import subprocess
import re


def main():
    nickname_dict = (
        {}
    )  # creating a dictionary to hold the nicknames and the number of lines they spoke
    # get the file name
    file_name = input(
        "Please enter a file (with the entire path if in a different folder): "
    )
    # read it in and start processing it
    with open(file_name, "r") as fin:
        file_contents = fin
        split_file_contents = []
        for line in file_contents:
            line = line.strip()
            print(line)


if __name__ == "__main__":
    main()
