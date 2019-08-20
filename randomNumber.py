'''
m, 0 < m, The modulus
a, 0 < a < m, The multiplier
c, 0 <= c < m, The increment
X0, 0 <= X0 < m, The seed, or starting value'''

'''
Values used by GCC compiler
m = 2e31
a = 1103515245
c = 12345
'''

def randomFunction(X_n):
	X_n_plus_1 = (a * X_n + c) % m

	return X_n_plus_1

m = pow(2,31) 
a = 1103515245
c = 12345

seed = 0


for i in range(1,100):
	seed = randomFunction(seed)
	print seed%10 
	
