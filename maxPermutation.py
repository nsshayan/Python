# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 19:55:31 2015

@author: snaganan
"""
print naive_max_perm([2,2,0,5,3,5,7,4])

def naive_max_perm(M, A=None):
    if A is None: # The elt. set not supplied?
        A = set(range(len(M))) # A = {0, 1, ... , n-1}
    if len(A) == 1: return A # Base case -- single-elt. A
    B = set(M[i] for i in A) # The "pointed to" elements
    C = A - B # "Not pointed to" elements
    if C: # Any useless elements?
        A.remove(C.pop()) # Remove one of them
        return naive_max_perm(M, A) # Solve remaining problem
    return A
    
