import os
import collections

SearchResult = collections.namedtuple("SearchResult", "file, line_num, text")


def main():
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
    folder = input("What folder to you want to look in? ")
    if not folder or not folder.strip():
        return None
    if not os.path.isdir(folder):
        return None
    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input("What are you searching for [single phrases only]? ")
    return text.lower()


def search_data(folder, text):
    # all_matches = []
    items = os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            yield from search_data(full_item, text)

        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    # matches = []
    with open(filename, "r", encoding="utf-8") as fin:
        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line_num=line_num, file=filename, text=line)
                yield m


if __name__ == "__main__":
    main()
