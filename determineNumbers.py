'''You are given an array of integers. The special property of the array is that exactly two different elements occur once while other elements occur twice.

You are required to determine those two elements.

Input format

First line: Integer  denoting the number of elements in the array
Second line:  space-separated integers denoting the values in the array
Output format

Print two space-separated integers that occur once in the array in ascending order.

Constraints
1 <= N <= 10^6
1<=Ai<10^6, where  denotes the  element in the array
'''
N = int(input())
A = list(map(int,input().split()))
first = A[0]
second = A[1]

def solve(N,A):    
    first = 0
    second = 0
    
    
    xor = A[0]
    for i in range(1,N):
        xor ^= A[i]
        
    y = xor & ~(xor-1)
    
    for i in range(0,N):
        if A[i]&y:
            first = first^A[i]
        else:
            second = second^A[i]
            
    return first,second


first,second = solve(N,A)
if first > second:
    print(second,first)
else:
    print(first,second)
