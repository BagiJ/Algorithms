import math
def merge_sort(A, p, r):
	if p < r:
		q = math.floor((p + r) / 2)
		print(p, q, r)
		merge_sort(A, p, q)
		merge_sort(A, q+1, r)
		N = merge(A, p, q, r)
	return N

def merge(A, p, q, r):

	n1 = q - p 
	n2 = r - q -1
	L = [None] * n1
	R = [None] * n2
	if (n1 == 0 or n2 == 0):
		return
	#let L[0, n1 ] and R[0, n2] be new arrays
	for i in range(n1):
		print("------------", i)
		L[i] = A[p+i]
	for j in range(n2):
		print(j)
		R[j] = A[q+j]
	i = 0
	j = 0
	for k in range(p, r):
		if L[i] <= R[j]:
			A[k] = L[j]
			if(i < len(L) - 1):
				i+=1
		else:
			A[k] = R[j]
			if(j < len(R)-1):
				j+=1
	return N


A = [3, 7, 2, 1, 4, 5]

print("Array before merge sort: ", A)
N = merge_sort(A, 0, len(A)-1)
print("Array after merge sort: ", N)