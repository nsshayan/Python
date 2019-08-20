
input = open('C:\Personal\Projects\Python\\testcase1.txt','r')
T=int(input.readline())
#T = int(raw_input())
for i in range(0,T):
	N = int(input.readline())

	N = N * N 

	initial_N = N

	numFactors = 1
	last = N/2 + 1		
	for i in range(1,last):
		if N % i == 0:
			numFactors += 1
	
	numfactors += 1
	
		 
	#for i in range(2,initial_N+1):
	#	power = 0
	#	while N % i == 0: 
	#		N = N/i
	#		power += 1
	#	numFactors = numFactors * (power + 1)
	#if N > 1:
	#	numFactors = numFactors * 2

	print (numFactors +1)/2
