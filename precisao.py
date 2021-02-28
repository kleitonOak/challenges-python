#!/usr/bin/env python

# from decimal import *
# getcontext().prec = 4
def printFrantionNumber(arrayElement, size):
    positive, negative, zero = 0,0,0
    for x in arrayElement:
        if(x > 0):
            positive += 1
        elif(x < 0):
            negative += 1
        elif(x == 0):
            zero += 1
    
    print format(positive/size, ".6f")
    print format(negative/size, ".6f")
    print format(zero/size, ".6f")

size = float(input())
printFrantionNumber([int(x) for x in raw_input().split()],size)