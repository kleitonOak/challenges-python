#!/usr/bin/env python
import pickle

mylist = ["This", "is", 4, 13327]
# Open the file for writing. The letter r before the filename is used to
# prevent backslash escaping
myfile = open(r"/Users/oak/DSV/python/linguagem/binary.data","w")
pickle.dump(mylist,myfile)
myfile.close()

myfile = open(r"/Users/oak/DSV/python/linguagem/textoSimples.txt","w")
myfile.write("This is a simple string")
myfile.close()

myfile = open(r"/Users/oak/DSV/python/linguagem/textoSimples.txt")
print(myfile.read())

#Open the file fro readin
myfile = open(r"/Users/oak/DSV/python/linguagem/binary.data")
loadedlist = pickle.load(myfile)
myfile.close()

print(loadedlist)

print("This is the end")
