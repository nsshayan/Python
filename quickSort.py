

def quickSort(A, lo, hi):
	if lo < hi: 
		p = partition(A, lo, hi)
		quickSort(A, lo, p-1)
		quickSort(A, p+1, hi)


def partition(A, lo, hi):
	pivotIndex = lo
	pivotValue = A[pivotIndex]

	A[pivotIndex], A[hi] = A[hi], A[pivotIndex]
	storeIndex = lo

	for i in range(lo,hi):
		if A[i] <= pivotValue :
			A[i],A[storeIndex] = A[storeIndex], A[i]
			storeIndex = storeIndex + 1 

	A[storeIndex],A[hi] = A[hi], A[storeIndex]

	return storeIndex

L = [-7,6,-5,4,-3,2,-1,0]

print "before sort", L
quickSort(L, 0, len(L)-1)
print "after sort", L
