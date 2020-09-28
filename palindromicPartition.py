#!/anaconda3/bin/python


def partition(s):
    C = [[0 for i in range(n)]for i in range(n)]
    P = [[False for i in range(n)] for i in range(n)]

    j,k,L=0,0,0

    for i in range(n):
        P[i][i] = True
        C[i][i] = 0



T = int(input())

for i in range(T):
    n = int(input())
    s = input()
    print("Min palindromic partition is "+partition(n,s))