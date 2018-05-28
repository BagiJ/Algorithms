import random
import math

def partition(A, p , r):
	x = A[r]
	i = p-1
	for j in range(p, r-1):
		if A[j] <= x:
			i+=1
			A[i], A[j] = A[j], A[i]
			print(A[i], A[j])
	A[i+1], A[r] = A[r], A[i+1]
	return (i+1)

def randomized_partition(A, p, r):
	print(p, r)
	#i = random.randint(p, r)
	#i =  r
	#A[r], A[i] = A[i], A[r]
	return partition(A, p, r)

def randomized_quicksort(A, p, r):
	if p < r:
		q = randomized_partition(A, p, r)
		randomized_quicksort(A, p, q-1)
		randomized_quicksort(A, q+1, r)		

#----------------------------------------

A = [2, 5, 1, 3, 6, 7, 8]
print("Array before sort: ", A)
randomized_quicksort(A, 0, len(A)-1)
print("Array after sorting: ", A)
