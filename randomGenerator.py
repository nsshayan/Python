
def solve(A,B,C):
	if A == B:
		if c == A:
			return Fraction(1/2.0 * A * 1) 

		if c >= (A+B):
			return Fraction(1/2.0 *(A+B) * 1)

	if A < B:
		if c == A:
			return Fraction(1/2.0 * A * 1)
				
		elif 		

n = int(raw_input())

for i in range(0,n):
	line = raw_input().split()
	A,B,C = int(line[0]), int(line[1]), int(line[2])
	
	solve(A,B,C)
