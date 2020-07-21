#!usr/bin/python
# Author:   @BlankGodd_

import os

def login(name, path=None):
    key = ""
    if name == 'toby':
        pass
    else:
        cur = os.getcwd()
        os.chdir('..')
        filename = "gentoken.txt"
        pt = os.getcwd()
        path = os.path.join(pt,filename)
        os.chdir(cur)

    with open(path, 'r') as tf:
        key = tf.read()

    return key



