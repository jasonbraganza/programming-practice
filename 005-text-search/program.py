import os
import collections

SearchResult = collections.namedtuple("SearchResult", "file, line_num, text")
# creating a named tuple so that i can refer to my search results in a sane manner


def main():
    """
    prints the header
    gets a folder to look through
    searches through all the subdirectories in the folder
    gets the results
    dumps them on screen
    """
    header_print()
    folder = get_folder_to_search()
    if not folder:
        print(f"Sorry, we cannot search that location")

    text = get_search_text_from_user()
    if not text:
        print(f"You need to enter something to search for")

    matches = search_data(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1
        print("==============Match Found====================")
        print(f'Text searched for: "{m.text.rstrip()}"')
        print(f"File is {m.file}")
        print(f"Found at line number: {m.line_num}")
        print("=============================================")
        print()
    print(f"Found, {match_count} matches")


def header_print():
    """
    Prints the header for the program
    """
    print("==================================")
    print("Welcome to the Text Search program")
    print("==================================")
    print()


def get_folder_to_search():
    """
    asks the user for the folder to look through 

    :return: the full file path of the subfolder given
    :rtype: string (full file path)
    """
    folder = input(
        "What folder to you want to look in? (give either a subfolder in your current directory or type in the full path)"
    )
    if not folder or not folder.strip():
        return None
    if not os.path.isdir(folder):
        return None
    return os.path.abspath(folder)


def get_search_text_from_user():
    """
    asks the user for text to search for

    :return: the text sanitised to all lower case for easy search
    :rtype: string
    """
    text = input("What are you searching for [single phrases only]? ")
    return text.lower()


def search_data(folder, text):
    """
    looks through a location, and then call the search for text function. if it is a subdirectory, then go in list those and call the search function on those files. does this recursively until the whole folder structure is exhausted

    :param folder: folder to run through
    :type folder: string (folder path)
    :param text: text to look for
    :type text: string
    :yield: calls the search data or file functions and yields further files listings or the actual search results
    :rtype: generator object
    """
    items = os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(
            full_item
        ):  # recursive function, need to understand and learn this better
            yield from search_data(full_item, text)

        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    """
    Runs through a given file, looking for text to search (skips binary files with the help of the try/except block looking for errors where it tells us it ain’t a text file)

    :param filename: file that we got by listing the folder
    :type filename: file object
    :param search_text: text we are looking for
    :type search_text: string
    :yield: results as a generator object
    :rtype: generator object
    """
    try:
        with open(filename, "r", encoding="utf-8") as fin:
            line_num = 0
            for line in fin:
                line_num += 1
                if line.lower().find(search_text) >= 0:
                    m = SearchResult(line_num=line_num, file=filename, text=line)
                    yield m
    except UnicodeDecodeError:
        print("NOTICE: Binary file {} skipped.".format(filename))


if __name__ == "__main__":
    main()
