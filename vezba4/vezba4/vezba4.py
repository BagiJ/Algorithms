import math
import random
import time


def heapsort(A):
	heapSize = len(A) -1
	build_max_heap(A)
	#for i in range(heapSize, 0, -1):
#probaj sa while(heapsize >=0)
	while heapSize != 0:
		A[0], A[heapSize] = A[heapSize], A[0]
		heapSize -= 1
		max_heapify(A, 0, heapSize)


def build_max_heap(A):
	A_heap_size = len(A) -1
	for i in range(math.floor(A_heap_size/2), -1, -1):
		max_heapify(A, i, A_heap_size)


def max_heapify(A, index, heapSize):
	l = left(index)
	r = right(index)
	largest = index
	if l <= heapSize and A[l] > A[largest]:
		largest = l
	if r <= heapSize and A[r] > A[largest]:
		largest = r
	if largest != index:
		A[index], A[largest] = A[largest], A[index]
		max_heapify(A, largest, heapSize)


def left(i):
	return 2*i + 1

def right(i):
	return 2*i + 2



def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

#A = random_list(1, 100, 50)

A = [4, 17, 3, 1, 2, 8, 12, 11]

print("List before sort: ", A)
start_time = time.clock()
heapsort(A)
end_time = time.clock() - start_time
print("Duration od heap_sort: ", end_time)
print("List after sort: ", A)