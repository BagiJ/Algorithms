import sys
import math
import operator


class Node:
    """
    Tree node: parent, left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None):
        """
        Node constructor 
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d


class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, value, freq):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        @param key / value
        """
        self.value = value
        self.freq = freq
        

def MakeNewElem(node1, node2):
    newElem = Node(None, None, None, node1.data.freq + node2.data.freq)
    node1.parent = newElem
    node2.parent = newElem

    if node1.data.freq > newElem.data.freq:
        newElem.right = node1
    else:
        newElem.left = node1
    if node2.data.freq > newElem.data.freq:
        newElem.right = node2
    else:
        newElem.left = node2

# return the minimum elements
def getMinFreqElem(l):
    if len(l) > 1:
       min1 = l[0]
       min2 = l[1]

    return [l[0], l[1]]


def RemoveElem(l, index):
    if index < len(l)-1:
        del l[index]

def getHistogram(input):
    d=dict()
    for key in input:
        if (key in d):
            d[key] += 1
        else:
            d[key] = 1

    print(d)

    return d



def printList(l):
    for i in range(len(l)):
        print("Value: ", l[i].data.value,  \
            "Frequency: ", l[i].data.freq)


if __name__ == "__main__":

    listOfNodes =[]

    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    print(input3)

    d = getHistogram(input3)
    print("dict: ", d)

    # Sort dictonary 
    sorted_histogram = sorted(d.items(), key=operator.itemgetter(1))    

    print("Sorted Histogram: ", sorted_histogram)

    for value, freq in sorted_histogram:
        listOfNodes.append(Node(None, None, None, Data(value, freq)))

    printList(listOfNodes)

    # Making a tree 
    min1, min2 = getMinFreqElem(listOfNodes)
    print("Min elem: ", min1.data.freq, min2.data.freq)

    RemoveElem(listOfNodes, 0)

    printList(listOfNodes)


  



