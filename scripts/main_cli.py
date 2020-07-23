#!usr/bin/python
# Author:   @BlankGodd_

from upload import Upload
import os
from entry import login


def start():
    print("Please Enter Your Name")
    name = input("> ")
    print("Welcome, {}".format(name))

    key = ""
    if name.lower() == "toby":
        path = input("Enter full key path: ")
        key = login(name, path)
    else:
        key = login(name)
    return key

if __name__ == "__main__":
    key = start()
    a = Upload(key)
    b = a.form()
    print(b)




