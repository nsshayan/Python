#!/anaconda3/bin/python

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
