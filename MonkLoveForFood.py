# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 10:03:28 2016

@author: snaganan
"""

class stack:
    
    def __init__(self):
        self.stackData = [] 
    
    def push(self,data):
        self.stackData.insert(0,data)
        
    def pop(self):
        popData = self.stackData[0]
        del self.stackData[0]
        return popData
    
    def topElement(self):
        return self.stackData[0]

    def isEmpty(self):
        if len(self.stackData) == 0 :
            return True
        else :
            return False
    
    def size(self):
        return len(self.stackData)


Q = int(raw_input())
FoodStack = stack()
for i in range(Q):
    testCase = raw_input()
    if testCase == '1':
        if FoodStack.isEmpty():
            print 'No Food'
        else :
            print FoodStack.pop()
    else:
        FoodStack.push(testCase.split(' ')[1])