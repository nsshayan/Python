def matrixMul(a,b):
	C=[[0,0],[0,0]]
	C[0][0] = a[0][0]*b[0][0]+a[0][1]*b[1][0]
	C[0][1] = a[0][0]*b[0][1]+a[0][1]*b[1][1]
	C[1][0] = a[1][0]*b[0][0]+a[1][1]*b[1][0]
	C[1][1] = a[1][0]*b[0][1]+a[1][1]*b[1][1]
	
	return C

def matrixPowN(Mat ,N):
	Mat_N = matrixMul(Mat,Mat)
	if N == 1:
		return Mat
	if N == 2:
		return Mat_N
	
	for i in range(1,N):
		Mat_N = matrixMul(Mat, Mat_N)

	return Mat_N	

input = open('C:\Personal\Projects\Python\\testcase1.txt','r')
T = int(input.readline())
LastN = 1000000000

for i in range(1,T+1):
	TestCase = (input.readline()).split()
	A,B,N = int(TestCase[0]),int(TestCase[1]),int(TestCase[2])

	if B < A:
		A,B = B,A
	Mat = [[1,1], [1,0]]
	
	Mat_N = matrixPowN(Mat, N)	

	F_n = Mat_N[1][0]*B + Mat_N[1][1]*A

	if F_n > LastN:
		F_n = F_n % LastN + 7
		print F_n

	else :
		print F_n


