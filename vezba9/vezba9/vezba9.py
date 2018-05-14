from enum import Enum	
import math
from collections import deque

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, idd = None, d2 = None, f = None):
        """
        Vertex constructor 
        @param color, parent(prethodni), auxilary data1(id), auxilary data2(distance)
        """
        self.c = c
        self.p = p
        self.id = idd
        self.d = d2
        self.f = f

class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2

class Graph:

    def __init__(self, g= None, n = None):
        self.graph = g
        self.numberOfNodes = n
	
class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		
############## BFS #################


def BFS(G, s):
    for u in G.graph:
            u[0].c = VertexColor.WHITE
            u[0].d = math.inf
            u[0].p = None
    s.c = VertexColor.GRAY
    s.d = 0
    s.p = None
    Q = deque()
    Q.append(s)
    while Q:
         u = Q.popleft()
         for v in G.graph[u.id-1]:
             if v.c == VertexColor.WHITE:
                 v.c = u.d +1
                 v.p = u
                 Q.append(v)
         u.c == VertexColor.BLACK

def print_path(G, s, v):
    if v == s:
        print(s.id)
    elif v.p == None:
        print("No path from 's' to 'v' exists")
    else:
        print_path(G, s, v.p)
        print(v.id)
############## DFS #################
time = 0
def DFS(G):

    for u in G.graph:
            u[0].c = VertexColor.WHITE
            u[0].p = None
    time = 0
    for u in G.graph:
        if u[0].c == VertexColor.WHITE:
            DFS_Visit(G, u, u[0])

# xx - trenutni obradjivani
def DFS_Visit(G, u, xx):
    # white vetex u has just been discovered
    global time    
    time += 1
    xx.d = time
    xx.c = VertexColor.GRAY
    # explore edge (u,v)
    for v in u[1:]:
        if v.c == VertexColor.WHITE:
            v.p = u
            DFS_Visit(G, u, v)
    #blacken u: it is finished
    xx.c = VertexColor.BLACK
    time += 1
    xx.f = time

####################################


def createGraph():
    # indeksiranje na dalje ide --> ako je CVOR 5 uzima se v[4] itd...
    v = [Vertex(c=VertexColor.WHITE, idd=1, d2=100), Vertex(c=VertexColor.WHITE, idd=2, d2=200), Vertex(c=VertexColor.WHITE, idd=3, d2=300),
         Vertex(c=VertexColor.WHITE, idd=4, d2=400),  Vertex(c=VertexColor.WHITE, idd=5, d2=500)]

    l = []
    
    l.append([v[0], v[1], v[4]])
    l.append([v[1], v[0], v[4], v[2], v[3]])
    l.append([v[2], v[1], v[3]])
    l.append([v[3], v[1], v[4], v[2]])
    l.append([v[4], v[3], v[0], v[1]])

    gr = Graph(l, 5)
    #print(gr.graph[0][1].d)
    for x,i in zip(gr.graph, range(1, gr.numberOfNodes)):
        for y in x:
            print("Vertex edges:  (", x[0].id , " , ", y.id, ")") 

    BFS(gr, v[4])

    print_path(gr, v[4], v[2])

    #DFS(gr)
    #print("cao")
    ## print DFT
    #for u in gr.graph:
    #    print("Vertex id: ", u[0].id)
    #    for v in u[1:]:
    #        print("Vertex id :", v.id, " Time_stamp1: ", v.d, " Finish time: ", v.f)

if __name__ == "__main__":
    #u = Vertex(c=VertexColor.WHITE, d1=1, d2=22)
    #v = Vertex(c=VertexColor.GRAY, p=u, d1=33, d2=4)
    createGraph()


