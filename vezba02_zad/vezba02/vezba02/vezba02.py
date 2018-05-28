import random
import time
import sys

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 200, 100)


def print_list(l):
    print("list: ", l)


def insertion_sort(A):
	for j in range(1, (len(A))):
		key = A[j]
		i = j-1
		while (i>=0 and A[i]>key):
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key



def bubble_sort(A):
	index = -1
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(A)-1):
			if (A[i] > A[i+1]):
				A[i], A[i+1] = A[i+1], A[i]
				swapped = True
		
	return index

	

def linear_search(A, num):
	index = -1
	for i in range(len(A)):
		if (A[i] == num):
			index = i
	return index



def binary_search(A, val):
	low = 0
	high = len(A)-1
	while (low <= high):
		mid =int((low + high) / 2)
		if (A[mid] > val):
			high = mid -1
		elif (A[mid] < val):
		    low = mid + 1
		else:
			return mid
	return "Element_not found"


TEST_INSTERION = 'n'
TEST_BUBBLE = 'no'
TEST_LINEAR = 'y'
TEST_BINARY_INSERTION = 'n'
TEST_BINARY_BUBBLE = 'n'


if TEST_INSTERION == 'y':
	print("------------- Insertion Sort -------------")
	print("List before sorting: ", l)

	start_time = time.clock()
	insertion_sort(l)
	end_time = time.clock() - start_time
	print("Duration: ", end_time)

	print("List after sorting: ", l)
if TEST_BUBBLE == 'y':
	print("------------- Bubble Sort -------------")
	print("List before bubble_sort: ", l)

	start_time = time.clock()
	bubble_sort(l)
	end_time = time.clock() - start_time
	print("Duration: ", end_time)
	print("List after bubble_sort: ", l)
if TEST_LINEAR == 'y':
	print("------------- Linear_search -------------")
	print("List: ", l)
	start_time = time.clock()
	linear_search(l,21)
	end_time = time.clock() - start_time
	print("Duration: ", end_time)
	print("Index: ", linear_search(l, 11))
if TEST_BINARY_INSERTION == 'y':
	print("------------- Binary search + Insertion sort -------------")
	insertion_sort(l)
	print("List: ", l)
	print("Index: ", binary_search(l, 3))
if TEST_BINARY_BUBBLE == 'y':
	print("------------- Binary search + Bubble sort -------------")
	bubble_sort(l)
	print("List: ", l)
	print("Index: ", binary_search(l, 3))

	
