from enum import Enum	
import math
from collections import deque

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, idd = None, d2 = None):
        """
        Vertex constructor 
        @param color, parent(prethodni), auxilary data1(id), auxilary data2(distance)
        """
        self.c = c
        self.p = p
        self.id = idd
        self.d = d2

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

def BFS(G, s):
    for u in G.graph:
        for i in range(len(u)):
            u[i].c = VertexColor.WHITE
            u[i].d = math.inf
            u[i].p = None
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


def createGraph():
    # indeksiranje na dalje ide --> ako je CVOR 5 uzima se v[4] itd...
    v = [Vertex(c=VertexColor.WHITE, idd=1, d2=100), Vertex(c=VertexColor.WHITE, idd=2, d2=200), Vertex(c=VertexColor.WHITE, idd=3, d2=300),
         Vertex(c=VertexColor.WHITE, idd=4, d2=400),  Vertex(c=VertexColor.WHITE, idd=5, d2=500)]

    l = []
    
    l.append([v[1], v[4]])
    l.append([v[0], v[4], v[2], v[3]])
    l.append([v[1], v[3]])
    l.append([v[1], v[4], v[2]])
    l.append([v[3], v[0], v[1]])

    gr = Graph(l, 5)
    #print(gr.graph[0][1].d)
    for x,i in zip(gr.graph, range(gr.numberOfNodes)):
        for y in x:
            print("Vertex edges:  (", v[i].id , " , ", y.id, ")") 

    BFS(gr, v[4])

    print_path(gr, v[4], v[2])

if __name__ == "__main__":
    #u = Vertex(c=VertexColor.WHITE, d1=1, d2=22)
    #v = Vertex(c=VertexColor.GRAY, p=u, d1=33, d2=4)
    createGraph()


