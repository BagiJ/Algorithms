from enum import Enum	
import math
import heapq

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, d1 = None, idd = None, d2 = None, p = None):
        """
        Vertex constructor 
        @param color, parent, weight, auxilary data1(id), auxilary edge(s), p(prethodnik)
        """
        self.color = c
        self.weight = d1
        self.id = idd
        self.d2 = d2
        self.p = p

    def __lt__(self, other):
        return self.weight < other.weight

class Edge:
    """
    Graph edge: A graph edge with data
    """
    def __init__(self, s = None, d = None, w = None):
        """
        Edge constructor
        @param source(vertex), destination(vertex), weight
        """
        self.source = s
        self.destination = d
        self.weight = w

class Graph:

    def __init__(self, g= None, n = None):
        self.graph = g
        self.numberOfNodes = n
     

class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		

#DIJKSTRA Q je minHeap (za heap heapq(python doc))
"""
@param graph(vetex), edges(weights), vertex s
"""
def dijkstra(G, w, s):
    initialize_single_source(G, s)
    S = []
    #heapq
    Q = []
    for v in G.graph:
        Q.append(v[0])

    heapq.heapify(Q)
    while Q:
        u = heapq.heappop(Q)
        S.append(u)
        for s in G.graph:
            if u == s[0]:
                for v in s:
                    if (v == u):
                        continue
                    relax(u, v, w)



def initialize_single_source(G, s):
    for v in G.graph:
        v[0].weight = math.inf
        v[0].p = None
    s.weight = 0

def relax(u, v, w):
    ww = get_weight(u, v, w)
    if v.weight > (u.weight + ww):
        v.weight = u.weight +  ww
        v.p = u

def get_weight(u, v, w):
    for edg in w:
        # nasao source
        if edg.source == u:
            #nadji destination
            for i in range(len(edg.destination)):
                # nasao i v
                if (edg.destination[i] == v):
                    #vrati weight
                    return edg.weight[i]


def print_path(G, s, v):
    if v == s:
        print(s.id)
    elif v.p == None:
        print("No path from 's' to 'v' exists")
    else:
        print_path(G, s, v.p)
        print("Id: ", v.id, " weight: ", v.weight)

##################### main #####################		
#u = Vertex(c=VertexColor.WHITE, d1=1, d2=22)
#v = Vertex(c=VertexColor.GRAY, p=u, d1=33, d2=4)


v = [Vertex(VertexColor.GRAY, 0, 's'), Vertex(VertexColor.WHITE, math.inf, 't'), Vertex(VertexColor.WHITE, math.inf, 'y'),
     Vertex(VertexColor.WHITE, math.inf, 'x'), Vertex(VertexColor.WHITE, math.inf, 'z')]

l = []

l.append([v[0], v[1], v[2]])
l.append([v[1], v[2], v[3]])
l.append([v[2], v[1], v[3], v[4]])
l.append([v[3], v[4]])
l.append([v[4], v[0], v[3]])

gr = Graph(l, 5)

#for x,i in zip(gr.graph, range(1, gr.numberOfNodes)):
#    for y in x:
#        if (x[0].id == y.id):
#            continue
#        print("Vertex edges: (", x[0].id, " , ", y.id, ")")

e = [Edge(v[0], [v[1],v[2]], [10, 5]), Edge(v[1], [v[2],v[3]], [2, 1]), Edge(v[2], [v[1], v[3], v[4]], [3, 9, 2]),
     Edge(v[3], [v[4]], [4]),  Edge(v[4], [v[0], v[3]], [7, 6])]

print("Edges -> (source ,destination, weight)")
for edg in e:
    for i in range(len(edg.destination)):
        print("(", edg.source.id, " , ",edg.destination[i].id,  " , ", edg.weight[i], ")")
   
s = v[0]

dijkstra(gr, e, s)

print("\n")

print_path(gr, s, v[4])

