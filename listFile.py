#!/usr/bin/env python
import os, glob

def listAllFile(path, type):
    os.chdir(path)
    for file in glob.glob(type):
        print(file)

listAllFile(".","*.py")
