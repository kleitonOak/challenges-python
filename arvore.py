#!/usr/bin/env python

class Node:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

inputList = [1, 2, 3, 4, 5, 6]
q = len(inputList) // 2

arvore = Node()
arvore.data = inputList[q]
print ("Raiz: {}".format(arvore.data))
for x in inputList:
    if(x != arvore.data):
        if(x > arvore.data):
            x1 = Node()
            x1.data = x
            arvore.right = x1
            print ("DIREITA: {}".format(x))
        else:
            x1 = Node()
            x1.data = x
            arvore.left = x1
            print ("ESQUERDA: {}".format(x))
