#!/usr/local/bin/python

class Node():
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class Tree():
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def addNode(self,value):
        if self.root == None :
            self.root = Node(value)
        else :
            self._add(value,self.root)

    def _add(self,val,node):
