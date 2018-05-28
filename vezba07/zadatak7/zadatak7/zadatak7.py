import sys
import math
import random
import time

M = 10
p = 23

class Data:
    """
    @param key: Atribut key predstavlja celobrojnu vrednost koja se koristi kao argument u hash funkciji
    @param literal: Atribut literal predstavlja znakovnu vrednost atributa key
    """
    def __init__(self, key, literal):
        self.key = key
        self.literal = literal
        

def hash_division_method(k):
    return k % M

def hash_multiplication_method(k):
    A = (math.sqrt(5)-1) / 2
    return math.floor(M * (k*A % 1))

def universal_hasing(k):

    a = random.randint(1, p-1)
    b = random.randint(1, p-1)
    return ((a*k + b) % p) % M


#insert x at the head of list T[h(x, key)]
def chained_hash_insert(T, xData):
    """
    Choose the SAME hash method
    """
    index = hash_division_method(xData.key)
    #index = hash_multiplication_method(xData.key)
    #index = universal_hasing(xData.key)
    l=[]
    
    strIndex = str(index)
   
    if strIndex in T:
       
        if (isinstance(T[strIndex], list)):
            for i in range(len(T[strIndex])):
                l.append(T[strIndex][i])
            l.append(xData.literal)
            T[strIndex] = l
            return
        
        l.append(T[strIndex])
        l.append(xData.literal)
        T[strIndex] = l
    else:
        T[strIndex] = xData.literal

# search for an element with key k in the list T[h(k)]
def chained_hash_search(T, key):
    """
    Choose the SAME hash method
    """
    index = hash_division_method(key)
    #index = hash_multiplication_method(key)
    #index = universal_hasing(key)

    strIndex = str(index)
    if strIndex in T:
        print("Key: ", strIndex, " found. Literal: ", T[strIndex])
        return strIndex
    else:
        print("Key: ", strIndex, " not in list.")
        return "NOT FOUND"

def chained_hash_delete(T, xData):

    strIndex = chained_hash_search(T, xData.key)

    if (strIndex == "NOT FOUND"):
        print("Item not found.")
        return "ITEM NOT FOUND"
    else:
        if ( isinstance(T[strIndex], list)):
            for i in range(len(T[strIndex])):
                if (T[strIndex][i] == xData.literal):
                    print("Item: ", T[strIndex][i], " deleted.")
                    del T[strIndex][i]
                    return
        else:
            print("Item: ", T[strIndex], " deleted.")
            del T[strIndex]
        
        return


##############
#### main ####
##############
if __name__ == "__main__":
    table = dict()
    dataList = [Data(1, "AAA"), Data(2, "BBB"), Data(3, "CCC"), Data(4, "DDD"), Data(5, "EEE"), Data(1, "RRR"), 
        Data(6, "SSS"), Data(1, "DZDZD")]

    ########### CHAINED_HASH_INSERT ###########
    for i in range(len(dataList)):
        chained_hash_insert(table, dataList[i])
   
    print(table, "\n")
    ###########################################


    ########### CHAINED_HASH_SEARCH ###########
    serach_key = 1

    start_time = time.clock()
    value = chained_hash_search(table, serach_key)

    elapsed_time = time.clock() - start_time
    
    print("Key: ", serach_key, " Value: ", value)
    print("Elapsed time for search: ", elapsed_time)
    ###########################################


    ########### CHAINED_HASH_DELETE ###########
    delete_data = dataList[2]

    value = chained_hash_delete(table, delete_data)
    
    print("\n", table, "\n")
    ###########################################

