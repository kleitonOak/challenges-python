#!/usr/bin/env python

def quicksort(lista, inicio, fim):

    if(inicio < fim):
        pivor = particionamento(lista, inicio, fim)
        # print("{}".format(pivor))
        quicksort(lista, inicio, pivor)
        quicksort(lista, pivor+1, fim)

def particionamento(lista, inicio, fim):
    x, y, pivor, temp = inicio, fim, lista[inicio], -1

    while True:
        while lista[x] < pivor and pivor != lista[x]:
            x += 1
        while lista[y] > pivor and pivor != lista[y]:
            y -= 1

        if x < y:
            temp = lista[x]
            lista[x] = lista[y]
            lista[y] = temp
        else:
            return y

elementos = [5, 1, 6, 2, 4, 3]
print ("List Before: %s" % elementos)
quicksort(elementos,0,5)
print ("List After: %s" % elementos)
print u"Worst: {}, Best: {}, Average: {}, Space: {}".format("O(n elevado a 2)", "O (n log n)", "O( n log n)", "O( n log n)")
