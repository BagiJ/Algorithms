import sys
import math
from enum import Enum
import heapq


path = []
length = 0

class Vertex:
    def __init__(self, c= None, p = None, id = None, d2 = None, l = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1(ID), auxilary data2
        """
        self.c = c
        self.p = p
        self.id = id
        self.d = d2
        self.neighbours = []
        self.letter = l

    def __lt__(self, other):
        return self.id < other.id

class Edge:
    """
    Graph edge: A graph edge with data
    """
    def __init__(self, s= None, d = None, w = None):
        self.src = s
        self.dst = d
        self.weight = w

class Graph:
    def __init__(self, v = None, e = None, n = None):
        self.verticies = v
        self.edges = e
        self.NumberOfNodes = n


class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255	


def MakeGraph():
    a = Vertex(c = VertexColor.WHITE , id = 1, l = 'a')
    b = Vertex(c = VertexColor.WHITE , id = 2, l = 'b')
    c = Vertex(c = VertexColor.WHITE , id = 3, l = 'c')
    d = Vertex(c = VertexColor.WHITE , id = 4, l = 'd')
    e = Vertex(c = VertexColor.WHITE , id = 5, l = 'e')
    f = Vertex(c = VertexColor.WHITE , id = 6, l = 'f')
    g = Vertex(c = VertexColor.WHITE , id = 7, l = 'g')

    a.neighbours.append(b)
    a.neighbours.append(c)
    b.neighbours.append(d)
    c.neighbours.append(d)
    c.neighbours.append(e)
    d.neighbours.append(e)
    d.neighbours.append(f)
    e.neighbours.append(f)
    e.neighbours.append(g)
    f.neighbours.append(g)



    #vertices
    v = [a, b, c, d, e, f, g]
#    print(v[0].id)

    e1 = Edge(a, b, 8)
    e2 = Edge(a, c, 6)
    e3 = Edge(b, d, 10)
    e4 = Edge(c, d, 15)
    e5 = Edge(c, e, 9)
    e6 = Edge(d, e, 14)
    e7 = Edge(d, f, 4)
    e8 = Edge(e, f, 13)
    e9 = Edge(e, g, 17)
    e10 = Edge(f, g, 7)

    #printAll edges

    #edges
    e = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
#    print(e1.src.letter, " ", e1.dst.letter, " ", e1.weight)

    g = Graph(v, e, 7)
    return g

# ulazni stepen
def GetInDegrees(graph):
    ret = []
    for v in graph.verticies:
        val = 0
        for e in graph.edges:
            #nasli smo, uzmemo weight i saberemo
            if v == e.dst:
            #    val += e.weight
                val += 1
        ret.append(val)

    return ret

# izlazni stepen
def GetOutDegrees(graph):
    ret = []
    for u in graph.verticies:
        val = 0
        for e in graph.edges:
            #nasli smo , uzmemo weight i saberemo
            if u == e.src:
            #    val += e.weight
                val += 1
        ret.append(val)
    
    return ret

def initialize_single_source(G, s):
    for v in G.verticies:
        v.d = math.inf
        v.p = None
    s.d = 0

def findEdge(u ,v ,e):
    w =0 
    for x in e:
        if u == x.src:
            if v == x.dst:
                w = x.weight
    return w


# vertex , vertex , edges
def relax(u, v, e):
    #find the weight between u,v
    w = findEdge(u, v, e)
    if v.d > u.d + w:
        v.d = u.d + w
        v.p = u

#graph , edges, vertex
def bellman_ford(G, e, s):
    initialize_single_source(G, s)
    for i in range(len(G.verticies) - 1):
        for edge in G.edges:
            relax(edge.src, edge.dst, e)
    for edge in G.edges:
        if edge.dst.d > edge.src.d + edge.weight:
            return False
    return True


#print i update lenght i path
def print_path(G, s, v):
    global path
    global length
    length = 0
    path = []

    if v == s:
#        print(s.letter, end = " ")
        path.append(s.letter)
    elif v.p == None:
        print("no path from ,", s.letter , "--> ", v.letter, " exists")
    else:
        print_path(G, s, v.p)
#        print(v.letter, end = " ")
        length += findEdge(v.p, v, G.edges)
        path.append(v.letter)



def ShortestPath(graph, nodeA, nodeB):
    # shortest path algorithm (graph, u, v)
    global path
    global length

    bellman_ford(graph, graph.edges, nodeA)
    print_path(graph, nodeA, nodeB)
    print("Shortes path from: ", nodeA.letter, " to ", nodeB.letter, " with length: ", end = " ")
    print("( ", path, " " , length, " )")

def edge_exists(nodeA, nodeB, e):
    for x in e:
        if x.src == nodeA:
            if x.dst == nodeB:
                return True
    return False

def change_weight(nodeA, nodeB, e, newWeight):
    for x in e:
        if x.src == nodeA:
            if x.dst == nodeB:
                x.weight = newWeight

def UpdateEdge(graph, nodeA, nodeB, weight):
    if edge_exists(nodeA, nodeB, graph.edges):
        change_weight(nodeA, nodeB, graph.edges, weight)
    else:
        new_edge = Edge(nodeA, nodeB, weight)
        graph.edges.append(new_edge)




if __name__ == "__main__":
    graph = MakeGraph()
#    print(graph.verticies[0].id)
    inDegrees  = []
    outDegrees = []

    inDegrees = GetInDegrees(graph)
    print("In degrees: ", end = " ")
    print(inDegrees, end = "\n\n")

    outDegrees = GetOutDegrees(graph)
    print("Out degrees: ", end = " ")
    print(outDegrees, end = "\n\n")

    nodeA = graph.verticies[0]
    nodeB = graph.verticies[6]

    ShortestPath(graph, nodeA, nodeB)

#    UpdateEdge(graph, graph.verticies[4], graph.verticies[5], -4)
    UpdateEdge(graph, graph.verticies[1], graph.verticies[2], -6)


    ShortestPath(graph, nodeA, nodeB)

