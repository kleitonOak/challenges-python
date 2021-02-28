#!/bin/python3

import sys
array = input().strip().split(' ');
#print (array)
arr = list(map(int,array))
newList = sorted(arr, reverse=True)
min = newList[len(newList)-1]
max = newList[0]
for x in range(1,len(newList)-1):
    element = newList[x]
    min += element;
    max += element
    
print ("%s %s" % (min,max))



#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    # Complete this function

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
   

