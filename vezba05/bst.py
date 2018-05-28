class Node:
    """
    Tree node: left child, right child and data
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
    def __init__(self, key, val1):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        @param key / value
        """
        self.key = key
        self.a1 = val1


def MakeTNode(p, node1, node2):
    node1.parent = p
    node2.parent = p

    if node1.data.key > p.data.key:
        p.right = node1
    else:
        p.left = node1
    if node2.data.key > p.data.key:
        p.right = node2
    else:
        p.left = node2

def printTNode(node):
    print("Current node:\t", node.data.key,        \
          "\nParent node:\t", node.parent.data.key if(node.parent is not None) else "No parent node" \
          "\nLeft child:\t", node.left.data.key if(node.left is not None) else "No left node",   \
          "\nRight child:\t", node.right.data.key if(node.right is not None) else "No right child" )

class TBST:
    """
    @param The root of the tree and the size
    """
    def __init__(self, r = None, s = None):
        self.root = r
        self.size = s


def tree_insert(T, z):
    y = None
    x = T.root
    while x is not None:
        y = x
        if z.data.key < x.data.key:
            x = x.left
        else: 
            x = x.right
    z.parent = y
    if y is None:
        T.root = z
    elif z.data.key < y.data.key:
        y.left = z
    else:
        y.right = z



def transplant(T, u, v):
    if u.parent is None:
        T.root = v
    elif u is u.parent.left:
        u.parent.left = v
    else:
         u.parent.right = v
    if v is not None:
        v.parent = u.parent


def tree_delete(T, z):
    if z.left is None:
        transplant(T, z, z.right)
    elif z.right is None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.parent is not z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y
        transplant(T, z, y)
        y.left = z.left
        y.left.parent = y

def tree_minimum(x):
    while x.left is not None:
        x = x.left
    return x

def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.data.key)
        inorder_tree_walk(x.right)

def tree_search(x, k):
    if x is None or k == x.data.key:
        return x
    if k < x.data.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)

def tree_max(x):
    while x.right is not None:
        x = x.right
    return x

def tree_successor(x):
    if x.right is not None:
        return tree_successor(x.right)
    y = x.parent
    while (y is not None) and (x is y.right):
        x = y
        y = y.parent
    return y


def iterative_tree_search(x, k):
    while (x is not None) and (k is not x.data.key):
        if k < x.data.key:
            x = x.left
        else:
            x = x.right
    return x
       


     
if __name__ == "__main__":
    d1 = Data(1, 2)
    d2 = Data(4, 11)
    d3 = Data(6, 23)
    d4 = Data(11, 6)
    print("Key values: ", d1.key, d2.key, d3.key, d4.key , "\n")
    #print(d.a1, d.a2)

    n4 = Node(None, None, None, d4)
    n3 = Node(None, None, None, d3)
    n2 = Node(None, None, None, d1)
    n1 = Node(None, None, None, d2)

   # MakeTNode(n1, n2, n3)
    T = TBST()

    #inserting nodes in tree
    tree_insert(T, n1)
    tree_insert(T, n2)
    tree_insert(T, n3)
    tree_insert(T, n4)
    tree_insert(T, Node(None, None, None, Data(0, 2)))
    tree_insert(T, Node(None, None, None, Data(5, 11)))
    tree_insert(T, Node(None, None, None, Data(7, 23)))
    tree_insert(T, Node(None, None, None, Data(12, 6)))

   # printTNode(n1)
    inorder_tree_walk(T.root)
    
   # tree_delete(T, n2)
    print("\n")
    inorder_tree_walk(T.root)
    
    index = tree_search(T.root, 4)
   # print("The key is: ", index.data.a1)
  #  printTNode(n1)

    print("Tree max: ", tree_max(T.root).data.key)
    print("Tree min: ", tree_minimum(T.root).data.key)
    #findSuccessor = n2
    #print("Successor of ", findSuccessor.data.key , " is : ", tree_successor(findSuccessor).data.key if(tree_successor(findSuccessor) is not None) else "No successor" )
