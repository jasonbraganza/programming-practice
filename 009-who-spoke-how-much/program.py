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
    # get the log file name to process
    file_name = input(
        "Please enter a file (with the entire path if in a different folder): "
    )
    # read it in and start processing it
    with open(file_name, "r") as fin:
        file_contents = fin
        for every_line in file_contents:
            split_line_list = re.split(r"(]\s|>\s)", every_line)
            if len(split_line_list) <= 3:
                continue
            else:
                nickname = split_line_list[2].lstrip("<").lstrip("@")
                number_of_words = len(split_line_list[4].split())
                # print(f"{nick_name} said {words} words")
                if nickname not in nickname_dict.keys():
                    nickname_dict[nickname] = number_of_words
                else:
                    nickname_dict[nickname] += number_of_words
    for name, blah in sorted(nickname_dict.items()):
        print(f"{name} spoke {blah} words")


if __name__ == "__main__":
    main()
