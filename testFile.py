# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 12:29:05 2016

@author: snaganan
"""

from Stack import stack
from queue import queue
s = stack()

s.push(5)
s.push(6)
s.push(7)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.push(0)
s.push(-1)
print "stack output"
print s.pop()
print s.pop()
print s.stackData
print "end of stack output"
#print s.pop()

#print s.stackData


q = queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print q.size()
print q.isEmpty()

print q.queueData
q.dequeue()

print q.queueData

