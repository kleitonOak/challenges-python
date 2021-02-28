#!/usr/bin/env python
from math import sqrt
def isPrimo(num1,num2):
    if num1 <= 1:
        num1 = 2

    numeroList = list([ x for x in range(num1,num2)])
    # print ("List %s - SQRT: %s" % (numeroList,int(sqrt(num2))))
    for k in range(num1,(int(sqrt(num2)) +1)):
        print k
        for l in range(len(numeroList)):
            if(numeroList[l] != k and numeroList[l] % k == 0):
                numeroList[l] = 0
    return numeroList

# numeroList = [ x for x in range(2,30)]
# print numeroList
print filter(lambda a: a != 0, isPrimo(1,30))
