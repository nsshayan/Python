# -*- coding: utf-8 -*-
"""
Generating Binary strings of length n

@author: snaganan
"""
n = 4

A = [None] * n

binary(n)
#print A 
del A
def binary(n):
    if n < 1:
        print A 
    else :
         A[n-1] = '0'
         binary(n-1)
         A[n-1]='1'
         binary(n-1)
    