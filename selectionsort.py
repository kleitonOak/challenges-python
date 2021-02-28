#!/usr/bin/env python

def selectionsort(lista):
    for x in range(len(lista) -1):
        menor = x
        for y in range(x+1,len(lista)):
            if lista[y] < lista[menor]:
                menor = y
        temp = lista[x]
        lista[x] = lista[menor]
        lista[menor] = temp

print "Worst Case Time Complexity : O(n2)"
print "Best Case Time Complexity : O(n2)"
print "Average Time Complexity : O(n2)"
elementos = [5, 1, 6, 2, 4, 3]
print ("List Before: %s" % elementos)
selectionsort(elementos)
print ("List After: %s" % elementos)
print "{} - {}".format("Eu","Aprendi")
