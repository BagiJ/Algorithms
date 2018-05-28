from enum import Enum

class Vertex:
    def __init__(self, c = None, p = None, d1 = None, d2 = None, name = "None"):
        self.c = c
        self.p = p
        self.d1 = d1
        self.d2 = d2 
        self.name = name

class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class VertexColor(Enum):
    BLACK = 0
    GRAY = 127
    WHITE = 255	



vertexes = []
for i in range(5):
    vertexes.append([])

s = Vertex(c = VertexColor.WHITE, d1 = None, d2 = None, name = "s")
t = Vertex(c = VertexColor.WHITE, d1 = None, d2 = None, name = "t")
y = Vertex(c = VertexColor.WHITE, d1 = None, d2 = None, name = "y")
x = Vertex(c = VertexColor.WHITE, d1 = None, d2 = None, name = "x")
z = Vertex(c = VertexColor.WHITE, d1 = None, d2 = None, name = "z")

vertexes[0].append(s) #0
vertexes[1].append(t) #1
vertexes[2].append(y) #2
vertexes[3].append(x) #3
vertexes[4].append(z) #4

vertexes[0].append(t)
vertexes[0].append(y)
vertexes[1].append(x)
vertexes[1].append(y)
vertexes[2].append(t)
vertexes[2].append(x)
vertexes[3].append(z)
vertexes[4].append(x)
vertexes[4].append(s)

edges = []

edges.append(Edge(s,t,10))
edges.append(Edge(s,y,5))
edges.append(Edge(t,y,2))
edges.append(Edge(t,x,1))
edges.append(Edge(y,t,3))
edges.append(Edge(y,x,9))
edges.append(Edge(y,z,2))
edges.append(Edge(z,x,6))
edges.append(Edge(z,s,7))
edges.append(Edge(x,z,4))

class G:
    def __init__(self, V = None, E = None):
        self.V = V
        self.E = E

GG = G(V = vertexes, E = edges)
