"""
File to load up the journal for the journal app program
"""

import os  # to do file i/o


def get_file_name(file_name):
    f_name = os.path.abspath(os.path.join("./journals", file_name + ".jrl"))
    return f_name


def load(file_name):
    """This loads the file name into a list and then returns it. If no file exists, it returns an empty list
    
    Arguments:
        file_name {string} -- a filename is expected
    
    Returns:
        {list} -- a list full of entries that was typed. or an empty list
    """
    # reads the journal from a file and returns it in a list
    data = []

    full_path_file_name = get_file_name(file_name)

    if os.path.exists(full_path_file_name):
        with open(full_path_file_name, "r") as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(file_name, journal_data):
    full_path_file_name = get_file_name(file_name)

    with open(full_path_file_name, "w") as fout:
        for entry in journal_data:
            fout.write(entry + "\n")


def add_entry(journal_data, text):
    journal_data.append(text)
