#!/usr/bin/env python

def insertionsort(listaElemento):
    for x in range(1,len(listaElemento)):
        y = x - 1
        key = listaElemento[x]
        while(y >= 0 and key < listaElemento[y]):
            listaElemento[y+1] = listaElemento[y]
            y -= 1
        listaElemento[y+1] = key

elementos = [5, 1, 6, 2, 4, 3]
print ("List Before: %s" % elementos)
insertionsort(elementos)
print ("List After: %s" % elementos)
print "Worst Case Time Complexity : O(n2)"
print "Best Case Time Complexity : O(n)"
print "Average Time Complexity : O(n2)"
print "Space Complexity : O(1)"
