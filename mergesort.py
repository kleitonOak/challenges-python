#!/usr/bin/env python

def mergesort(lista):
    if(len(lista) > 1):
        meio = len(lista) / 2

        listaEsquerda = lista[:meio] # NAO E INCLUSIVE - EX. 4 - VAI ATÉ 3
        listaDireita = lista[meio:]

        mergesort(listaEsquerda)
        mergesort(listaDireita)

        i = 0 # apenas para a lista da esquerda
        j = 0 # apenas para a lista da direita
        k = 0 # usado para a lista completa

        # PODE SER TODOS OS ELEMENTOS DA ESQUERDA
        # PODE SER TODOS OS ELEMENTOS DA DIREITA
        # PODE SER UMA MISTURA DE AMBOS
        while(i < len(listaEsquerda) and j < len(listaDireita)):
            # ORDENCAO
            if listaEsquerda[i] < listaDireita[j]:
                # ESQUEDA
                lista[k] = listaEsquerda[i]
                i += 1
            else:
                # DIREITA
                lista[k] = listaDireita[j]
                j += 1
            # SEMPRE INCREMENTA, INDEPENDENTE SE FOR DIREITA OU ESQUERDA
            k += 1

        # PODE SER QUE NEM TODOS OS ELEMENTOS DA ESQUERDA FORAM COLOCADOS NA LISTA (PODE TER SIDO REMOVIDO)
        # MANTÉM O VALOR DE J, I E K ANTERIORRES
        while i < len(listaEsquerda):
            lista[k] = listaEsquerda[i]
            # ATE COMPLETAR O ARRAY
            i += 1

            # SEMPRE INCREMENTA, INDEPENDENTE SE FOR DIREITA OU ESQUERDA
            k += 1

        while j < len(listaDireita):
            lista[k] = listaDireita[j]
            # ATE COMPLETAR O ARRAY
            j += 1
            # SEMPRE INCREMENTA, INDEPENDENTE SE FOR DIREITA OU ESQUERDA
            k += 1

# Melhor, Médio, Pior:  O(n*log(n))
# Desvantagens:
# Utiliza funções recursivas;
# Gasto extra de memória.
# O algoritmo cria uma cópia do vetor para cada nível da chamada recursiva,
# totalizando um uso adicional de memória igual a (n log n).


listaElemento = [6,9,2,1,9,8,3,0,22]
print("Before %s " % listaElemento)
mergesort(listaElemento)
print( "After %s " % listaElemento)
