#!/usr/bin/env python

class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

#
# def lista(elementos):
#     if(elementos is not None):
#         elemento = elementos
#         while(elemento.next):
#             elemento = elemento.next
#             print("Elemento Next")
#         while(elemento.data):
#             elemento = elemento.data
#             print("Elemento Data: {}".format(elemento.data))
#     else:
#         print("Nao existe elementos")

def lista(elemento):
    if(elemento.next):
        lista(elemento.next)
        print ("Dados: {}".format(elemento.data))
    else:
        print ("Fim: {}".format(elemento.data))

oakFilho3 = Node(4)
oakFilho2 = Node(3,oakFilho3)
oakFilho  = Node(2,oakFilho2)
oakRaiz = Node(1,oakFilho)
lista(oakRaiz)
