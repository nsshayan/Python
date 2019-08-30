import math
import time
start_time = time.time()
input = open('C:\Personal\Projects\Python\\testcase1.txt','r')
T = long(input.readline())
for i in range(0,T):
	N = int(input.readline())

	N = N * N 

	initial_N = N

	numFactors = 1
	factors = {}
	factors[2]=0
	while N%2 == 0 :
		factors[2] += 1
		N = N/2	
	i = 3
	while i < (math.sqrt(N)+1):
		factors[i] = 0
		while N%i == 0: 
			factors[i] += 1
			N = N/i
		if factors[i] == 0:
			del factors[i]
		i += 2
	for i in factors:
		numFactors = numFactors * (factors[i] + 1)
		 
	print (numFactors +1)/2
print "seconds = ",time.time()-start_time
