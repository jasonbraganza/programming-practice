"""
A new improved engine to download lolcats XD
Seriously though, it uses Michael Kennedy’s api site at "http://consuming-python-services-api.azurewebsites.net/cats/random" to get a random picture of a cat, (number of pictures, folder location and file names provided by calling program) and then save them to a folder
"""

import os
import shutil

import requests


def get_cats(folder, name):
    """
    this is the function that gets called externally.
    it then gets cats and saves them

    :param folder: name of folder to store files
    :type folder: string
    :param name: filename to give the currently downloading cat image
    :type name: string
    """
    url = "http://consuming-python-services-api.azurewebsites.net/cats/random"
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    """
    takes a url and returns a raw binary stream

    :param url: url to get cat images from
    :type url: string
    :return: image file
    :rtype: binary
    """
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder, name, data):
    """
    takes a raw image stream and writes it to the file name and folder provided

    :param folder: folder name
    :type folder: string
    :param name: name of image file
    :type name: string
    :param data: image data
    :type data: binary
    """
    a_file_name = os.path.join(folder, name + ".jpg")
    with open(a_file_name, "wb") as fout:
        shutil.copyfileobj(data, fout)
