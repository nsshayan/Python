# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 13:47:08 2016

@author: snaganan
"""



N = raw_input()
callingOrder = raw_input().split(' ')
idealOrder = raw_input().split(' ')

time = 0
while len(callingOrder) != 0 :
   
    if callingOrder[0] == idealOrder[0]:
        time += 1
        del callingOrder[0]
        del idealOrder[0]
    else :
        pushNo = callingOrder[0]
        del callingOrder[0]
        callingOrder.append(pushNo)
        time += 1 
    
print time