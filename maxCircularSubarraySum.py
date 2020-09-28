#!/anaconda3/bin/python
import sys
sys.path.append("/Users/snaganan/Documents/Personal/Projects/Python")
from maxContiguousSubarray import maxSubArraySum


def maxCircularSum(A):
    n = len(A)

    maxSum = SA.maxSubArraySum(A)

    maxSum2 = 0 
    for i in range(0,n):
        maxSum2 += A[i]
        A[i] = -A[i]
    
    maxSum2 = maxSum2 + SA.maxSubArraySum(A)

    if maxSum2 > maxSum:
        return maxSum2
    else:
        return maxSum



T = int(input()) # No of testcases

for i in range(T):
    A = list(map(int,input().split()))
    maxCircularSum(A)
