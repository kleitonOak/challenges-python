#!/usr/bin/env python
def matchsum(lista, valor):
    complemento = {}
    # considerando que seja um par de numero e nao mais que dois elementos
    for x in lista:
        if(x in complemento):
            return True
        else:
            complemento[abs (x - valor)] = x
    return False

elementos = [5, 1, 6, 2, 4, 3]
print matchsum(elementos, 11)
