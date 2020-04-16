"""
File to load up the journal for the journal app program
"""

import os  # to do file i/o


def load(file_name):
    # reads the journal from a file and returns it in a list
    data = []
    return data


def save(file_name, journal_data):
    f_name = os.path.abspath(os.path.join("./journals", file_name + ".jrl"))
    print(f"{f_name}")


def add_entry(journal_data, text):
    journal_data.append(text)
