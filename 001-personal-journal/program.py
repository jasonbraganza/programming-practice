"""
Creates and lists a journal for personal use
"""

import journal  # all the journal create and load functions are in there


def main_header():
    """
    Prints the header for the program
    """
    print("=========================")
    print("Welcome to my journal app")
    print("=========================")


def run_event_loop():
    """
    Runs an event loop to accept commands.
    """
    print(" ")
    print("Hey, the journal app has launched!")
    print("What do you want to do with your journal?")
    cmd = "None"
    journal_file_name = "default"
    journal_data = journal.load(
        journal_file_name
    )  # creating a list to hold the journal data
    while cmd != "x":
        cmd = input("(A)dd an entry, (L)ist entries or e(X)it? ")
        cmd = cmd.lower().strip()
        if cmd == "a":
            add_entry(journal_data)
        elif cmd == "l":
            list_entries(journal_data)
        elif cmd != "x":
            print(f"Sorry, {cmd} is not a valid command. Please try again")
    print("Saving journal …")
    # journal.save(journal_file_name, journal_data)
    print("Goodbye!")


def list_entries(data):
    """
    Function to list entries from a list (all the journal data)
    """
    reversed_list = reversed(data)  # reversing the list to get latest items on top
    for index, item in enumerate(
        reversed_list
    ):  # using enumerate to get list entry numbers along with the entries themselves
        print(f"{index+1}. {item}")  # adding 1 so that entry numbers don’t start at 0


def add_entry(data):
    """
    Function to add an item from a list (add entry to journal data)
    """
    text = input("Type your entry, and hit enter to exit: ")
    journal.add_entry(data, text)


def main():
    main_header()
    run_event_loop()


if __name__ == "__main__":
    main()
