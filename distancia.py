#!/usr/bin/env python
import string

def distanceElement(coordenates):
    sumElement = 0
    for x,y in coordenates:
        sumElement += abs(x-y)
    return sumElement / len(coordenates)

print distanceElement([(1,2),(3,4),(5,6)])

def isAlmostPalidrome(strs):
    element = "".join(reversed(strs))
    count = 0
    if(element == strs):
        return True
    for x in range(len(strs)):
        if(strs[x] != element[x]):
            count += 1
    if(count > 1):
        return False
    return True
frase = "abccbgd"
print(isAlmostPalidrome(frase))

def mostPopularNumber(listaElemento):
    count = 0
    elemento = -1
    for x in listaElemento:
        v = listaElemento.count(x)
        if(v > count):
            count = v
            elemento = x
    print("(%s - appears, %s) times" % (elemento,count))

mostPopularNumber([34,31,34,77,82])
