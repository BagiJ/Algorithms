import sys
import time
import math 

list = [3, 2, 0, 1, 5, 7, 9, 10]


def merge(A, p, q, r):
  n1 = q-p + 1
  n2 = r - q
  L = []
  R = []
  for i in range(0, n1):
    L.append(A[p + i])
        
  for i in range(0, n2):
    R.append(A[q + i+1])
  R.append(math.inf)
  L.append(math.inf)
  i = 0
  j = 0

  for k in range(p, r + 1):
    if L[i] <= R[j]:
      A[k] = L[i]
      i = i + 1
    else:
      A[k] = R[j]
      j = j + 1



def mergeSort(A, p, r): 
  if p<r:
    q = math.floor((p+r)/2)
    mergeSort(A, p, q)
    mergeSort(A, q +1, r)
    merge(A, p , q, r) 

start_time = time.clock()
mergeSort(list, 0, len(list)-1)
end_time = time.clock()
timee = end_time - start_time
print("Time is " , timee)
print(list)
