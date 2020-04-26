"""
program to download cat images from the internet.

"""

import os
import platform
import subprocess

import cat_service  # module that actually goes to the net and gets the pics and saves them to a file


def main():
    """
    Prints the header
    Sets up a folder to save cat images in
    calls the cat service module to download and save images in the folder
    opens up the folder in the gui.
    """
    print_header()
    cat_folder = get_or_create_output_folder()
    download_cats(cat_folder)
    open_cat_folder(cat_folder)


def print_header():
    """
    Prints the header for the program
    """
    print("=============================")
    print("Welcome to the LOLCAT factory")
    print("=============================")
    print()


def get_or_create_output_folder():
    """
    returns (or creates first and returns) a subfolder in the program directory to save cat images.


    :return: folder to save images in 
    :rtype: string
    """
    folder = "lolcats"
    base_folder = os.path.dirname(__file__)
    full_path = os.path.join(base_folder, folder)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f"No folder for cats! That’s a shame. Creating folder at {full_path} … ")
        os.mkdir(full_path)
    return full_path


def download_cats(cat_folder):
    """
    calls the cat service module repeatedly until cat count is reached.
    the loop also gives it a series of incrementing file names

    :param cat_folder: folder to save the cat images in
    :type cat_folder: string
    """
    cat_count = 5
    print("Contacting LOLcat server to download cats … ")
    for i in range(1, cat_count + 1):
        cat_file_name = f"lolcat_{i}"
        print(f"Downloading cat, {cat_file_name}")
        cat_service.get_cats(cat_folder, cat_file_name)
    print("Done")


def open_cat_folder(cat_folder):
    """
    opens the folder in the operating system gui, so that the user can enjoy their lolcat images :)

    :param cat_folder: the folder, that the images are saved in
    :type cat_folder: string
    """
    if platform.system() == "Darwin":
        subprocess.call(["open", cat_folder])
    elif platform.system() == "Linux":
        subprocess.call(["xdg-open", cat_folder])
    elif platform.system() == "Windown":
        subprocess.call(["explorer", cat_folder])
    else:
        print(f"We don’t support {platform.system()}")


if __name__ == "__main__":
    main()
