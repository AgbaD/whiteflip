#!usr/bin/python
# Author:   @BlankGodd_

from upload import Upload
import os
from entry import login
import json


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
    path = input("Enter file path> ")
    b,c= a.upload(path)
    print(b)
    print()
    print(c)
    




