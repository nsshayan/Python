# -*- coding: utf-8 -*-
"""
Generate k-ary strings from string of length n

@author: snaganan
"""

K = "shayan"

n = 2

A = [None] * n


def k_string(n,k):
    if n < 1:
        print A
    else :
        for j in range(k):
            A[n-1]=K[j]
            k_string(n-1,k)
            

k_string(n,len(K))