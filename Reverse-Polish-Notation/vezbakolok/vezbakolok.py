import re
import sys

class Node:
    def __init__(self, p = None, l = None, r = None, d = None):
        self.parent = p
        self.left = l
        self.right = r
        self.data = d



        
def create_list(s):
    l = []
    op = []
    val = []
    str = re.split('\s', s)
    for i in range(len(str)):
            l.append(str[i])

    return l

class BSTroot():
    def __init__(self, r = None):
        self.root = r
    
def is_literal(s):
    if (s == '+' or s == '-'):
        return True
    elif (s == '/' or s == '*'):
        return True
    else:
        return False

def makeNode(op, l, r):
    left_n   = Node(None, None, None, l)
    right_n  = Node(None, None, None, r)
    n        = Node(None, left_n, right_n, op)
    left_n.parent = n
    right_n.parent = n

    return n


if __name__ == "__main__":
    input_str = "3 4 5 * -"

    l = create_list(input_str)
    print("\nlist: ", l)
    

    while (len(l) != 1):
        for i in range(len(l)):
            # kad naidjemo na prvi literal
            if (is_literal(l[i])):
                # get last two
                left = l[i-2]
                right = l[i-1]
                n = makeNode(l[i], left,  right)
                l[i] = n 
                del l[i-1], l[i-2]
               
                break

    T = BSTroot(l[0])

    

    # nodes

    
    
    