from enum import Enum
from math import inf

class Vertex:
    def __init__(self,id = 0, c = None, p = None, dl = None):
        self.c = c
        self.p = p
        self.dl = dl
        self.id = id

class VertexColor(Enum):
    BLACK = 0
    GRAY = 127
    WHITE = 255


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight



def MakeGraph():
    a = Vertex(1, c = VertexColor.WHITE, p = None, dl = 1)
    b = Vertex(2, c = VertexColor.WHITE, p = None, dl = 2)
    c = Vertex(3, c = VertexColor.WHITE, p = None, dl = 3)
    d = Vertex(4, c = VertexColor.WHITE, p = None, dl = 4)
    e = Vertex(5, c = VertexColor.WHITE, p = None, dl = 5)
    f = Vertex(6, c = VertexColor.WHITE, p = None, dl = 6)
    g = Vertex(7, c = VertexColor.WHITE, p = None, dl = 7)

    graph = []
    graph.append([a, b, c])
    graph.append([b, d])
    graph.append([c, e, d])
    graph.append([d, e, f])
    graph.append([e, f, g])
    graph.append([f, g])
    graph.append([g])

    edges = []

    edges.append(Edge(a,b,8))
    edges.append(Edge(a,c,6))
    edges.append(Edge(b,d,10))
    edges.append(Edge(c,e,9))
    edges.append(Edge(c,d,15))
    edges.append(Edge(d,e,14))
    edges.append(Edge(d,f,4))
    edges.append(Edge(e,f,13))
    edges.append(Edge(e,g,17))
    edges.append(Edge(f,g,7))

    return (graph, edges)

def printGraph(g):
    for i in range(len(g)):
        print("Za cvor {}, veze su:".format(i+1))
        for j in range(1, len(g[i])):
            print(g[i][j].id)
    return

(graph , W) = MakeGraph()
printGraph(graph)   

def GetInDegrees(graph):
    degreeList = []
    for i in range(len(graph)):
        count = 0
        for j in range(len(graph)):
            if i != j and graph[i][0] in graph[j]:
                count+=1
        degreeList.append(count)
        count = 0
    return  degreeList

print(GetInDegrees(graph))

def GetOutDegrees(graph):
    degreeList = []
    for i in range(len(graph)):
        degreeList.append(len(graph[i])-1)
    return  degreeList

print(GetOutDegrees(graph))

def initializeSingleSource(G, s):
    for v in G:
        v.dl = inf
        v.p = None
    s.d = 0

def findEdgeValue(w, u, v):
    for i in w:
        if i.source == u and i.destination == v:
            return i.weight
    return inf

def relax(u, v, w):
    if v.dl > u.dl + findEdgeValue(w, u, v):
        v.dl = u.dl + findEdgeValue(w, u, v)
        v.p = u

def BellmanFord(G,w,s):
    initializeSingleSource(G,s)
    for i in range(len(G)):
       for edge in w:
           relax(edge.source, edge.destination, w)
    for edge in w:
        if edge.source.dl > edge.destination.dl + findEdgeValue(w, edge.source, edge.destination):
            return False
    return True


def ShortestPath(G, nodeA, nodeB, w):
    BellmanFord(G, w, nodeA)
    L = []
    L = createPath(G, nodeA, nodeB, L)
    n = G[len(G) - 1].d
    return (L, n)

def createPath(G, s, v, L):
    if v == s:
        L.append(v)
    elif v.p == None:
        return None
    else:
        createPath(G, s, v.p, L)
        L.append(v)
    return L





def UpdateEdge(w, nodeA, nodeB, weight):
    if findEdgeValue(w, nodeA, nodeB) != inf:
        for i in w:
            if i.source == nodeA and i.destination == nodeB:
                i.weight = weight
    else:
        w.append(Edge(nodeA, nodeB, weight))

    



for x in W:
    print((x.source.id, x.destination.id, x.weight) )



UpdateEdge(W, graph[0], graph[2], 25)

for x in W:
    print((x.source.id, x.destination.id, x.weight) )








