def counting_sort(A, B ,k):
	for i in range(len(A)):
		B.append(0)

	C = [None] * 6
#C[0..k] be a new array
	for i in range(0, k, 1):
		C[i] = 0
	for j in range(0, len(A), 1):
		C[A[j]] = C[A[j]] + 1
#C[i] now contains the number of elements equal to i
	for i in range(1, k, 1):
		C[i] = C[i] + C[i-1]
#C[i] noew contains the number of elements less than or equal to i
	for i in range(0, k, 1):
		C[i] -=1
	for j in  range(0, len(A), 1):
		B[C[A[j]]] = A[j]
		C[A[j]] = C[A[j]] - 1



	

A = [2, 5, 3, 0, 2, 3, 0, 3]
B=[]
print("List before sort: ", A)
counting_sort(A, B, 6)
print("List after sort: ", B)

