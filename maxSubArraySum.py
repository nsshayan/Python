#!/anaconda3/bin/python

def maxSubArraySum(A):
    max_so_far = 0
    max_ending_here = 0

    for i in A:
        max_ending_here += i

        if max_ending_here < 0:
            max_ending_here = 0
        
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    
    return max_so_far



T = int(input())
for i in range(T):
    n = int(input())
    A = list(map(int,input().split()))

    print(maxSubArraySum(A))