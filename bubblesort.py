#!/usr/bin/env python

def bubblesort(listaElemento):
    for x in range(len(listaElemento)):
        for y in range((x+1),len(listaElemento)):
            if(listaElemento[x]>listaElemento[y]):
                aux = listaElemento[x]
                listaElemento[x] = listaElemento[y]
                listaElemento[y] = aux
    #return listaElemento

elementos = [5, 1, 6, 2, 4, 3]
print ("List Before: %s" % elementos)
bubblesort(elementos)
print ("List After: %s" % elementos)
print "Hence the complexity of Bubble Sort is O(n2)"
