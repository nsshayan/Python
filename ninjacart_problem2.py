'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
T = int(input())

for i in range(T):
    score = 0
    n = int(input())
   
    tiles = []
    for tile in range(n):
        tiles.append(list(map(int,input().split())))
    print(tiles[1])
    i = n
    while i > 0:
        print(i-1)
        a,b,c = tiles[i-1]
        if i+3 < n:
            score += c
            i=i+3
        elif i+2 < n:
            score += b
            i += 2
        elif i+3 == n  :
            score += c
            i += 3
        elif i+2 == n :
            score += b
            i += 2
        elif i == n:
            score += c
            i += 3
        else :
            score += a
            i+=1
    
    print(score)
            