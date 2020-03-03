#!/anaconda3/bin/python
'''
Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].


'''
T = int(input())

for i in range(T):
    n = int(input())
    A = list(map(int,input().split()))

    if n%2 == 0:
        middleIndex = n/2
    else :
        middleIndex = (n+1)/2

    Q = A[int(middleIndex):]
    insertIndex = 1

    B = A[:int(middleIndex)]


    for i in range(-1,-(len(Q)+1),-1):
        B.insert(insertIndex,Q[i])
        insertIndex += 2
    
    print(B)
