# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 12:21:51 2016

@author: snaganan
"""

class stack:
    
    def __init__(self):
        print "stack created"
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
        if self.stackData == None :
            return True
        else :
            return False
    
    def size(self):
        return len(self.stackData)
        
#    def __del__(self):
#        del self.stackData
#        print "Object cleaned up"
            
            
        
