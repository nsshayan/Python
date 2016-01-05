# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 15:23:14 2016

@author: snaganan
"""

class queue:
    
    def __init__(self):
        print "Queue created."
        self.queueData = []
    
    def enqueue(self,data):
        self.queueData.insert(0,data)
    
    def dequeue(self):
        self.queueData.pop()
        
    def front(self):
        element = self.queueData[self.queueData.count-1]
        return element
    
    def size(self):
        return len(self.queueData)
    
    def isEmpty(self):
        if self.queueData == None :
            return True
        else :
            return False
    
#==============================================================================
#     def __del__(self):
#         del self.queueData
#         print "queue destroyed."
#==============================================================================
