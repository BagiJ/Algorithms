import  sys
import time
from enum import Enum
import random

path = []

class Direction(Enum):
    UP = 0
    LEFT = 127
    UP_LEFT = 255

def lcs(S, n, T, m):
    if n == 0 or m == 0:
        return 0
    if S[n] == T[m]:
        return 1 + lcs(S, n-1, T, m-1)
    else:
        return max(lcs(S, n-1, T, m), lcs(S, n, T, m-1))


def lcs_length(X, Y):
    m = len(X)
    n = len(Y)

    #            BROJ KOLONA,               BROJ REDOVA
    #matrix = ([[0 for x in range(5)]  for y in range(10)])
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    #  for row in matrix]))

    # Creates a list containing m-1 lists, each of n items, all set to 0
    b = [[0 for x in range(n+1)] for y in range(m+1)] 
    c = [[0 for x in range(n+1)] for y in range(m+1)] 

    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    #  for row in b]))
    #print()
    #print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
    #  for row in c]))


    for i in range(1, m):
        c[i][0] = 0
    for j in range(n):
        c[0][j] = 0

    for i in range(1,m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = Direction.UP_LEFT
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = Direction.UP
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = Direction.LEFT
    return [b, c]


def print_lcs(b, X, i, j):
    global path
    path = []
    if i == 0 or j == 0:
        return 
    if b[i-1][j-1] == Direction.UP_LEFT:
        print_lcs(b, X, i-1, j-1)
        print(X[i-1], end=" ")
        path.append(X[i-1])
    elif b[i-1][j-1] == Direction.UP:
        print_lcs(b, X, i-1, j)
    else:
        print_lcs(b, X, i, j-1)


if __name__=="__main__":
    #S = "ABCBDAB"
    #T = "BDCABA"
    
    #S = [x for x in range(10)]
    #T = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    S = random.sample(range(50), 10)
    T = random.sample(range(50), 10)

    print(S)
    print(T)

    start_time = time.clock()
    lcs_num = lcs(S, len(S)-1, T, len(T)-1)
    end_time = time.clock()
    timee = end_time - start_time
    print("Time for LCS " , timee)
    print("LCS for: ", S, "and")
    print(T, " is ", lcs_num)


    [B, C] = lcs_length(S, T)
    print()
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in C]))

    print("\n\nLCS:", end=" ")
    print_lcs(B, S, len(S), len(T))
    print()
    #print(path)