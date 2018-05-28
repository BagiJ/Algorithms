import sys
from math import inf


class Edge:
    def __init__(self, first, second, val):
        self.first = first
        self.second = second
        self.val = val

class Vertex:
    def __init__(self, val):
        self.val = val
        self.con = []

def MakeGraph():
    a = Vertex("a")
    b = Vertex("b")
    c = Vertex("c")
    d = Vertex("d")
    e = Vertex("e")
    f = Vertex("f")
    g = Vertex("g")

    graph = [a, b, c, d, e, f, g]

    edges = []

    edges.append(Edge(a, b, 8))
    edges.append(Edge(a, c, 6))
    edges.append(Edge(b, d, 10))
    edges.append(Edge(c, e, 9))
    edges.append(Edge(c, d, 15))
    edges.append(Edge(d, e, 14))
    edges.append(Edge(d, f, 4))
    edges.append(Edge(e, f, 13))
    edges.append(Edge(e, g, 17))
    edges.append(Edge(f, g, 7))

    return (graph, edges)

def find_edge_value(w, u, v):
    for x in w:
        if x.first == u and x.second == v:
            return x.val
    return inf

def initialize_single_source(G, s):
    for v in G:
        v.d = inf
        v.p = None
    s.d = 0

def relax(u, v, w):
    if v.d > u.d + find_edge_value(w, u, v):
        v.d = u.d + find_edge_value(w, u, v)
        v.p = u

def bellman_ford(G, w, s):
    initialize_single_source(G, s)
    for i in range(len(G)):
        for edge in w:
            relax(edge.first, edge.second, w)
    for edge in w:
        if edge.first.d > edge.second.d + find_edge_value(w, edge.first, edge.second):
            return False
    return True

def GetInDegrees(G, w):
    L = []
    for v in G:
        n = 0
        for edge in w:
            if edge.second == v:
                n += 1
        L.append(n)
    return L

def GetOutDegrees(G, w):
    L = []
    for v in G:
        n = 0
        for edge in w:
            if edge.first == v:
                n += 1
        L.append(n)
    return L

def ShortestPath(G, nodeA, nodeB, w):
    bellman_ford(G, w, nodeA)
    L = []
    L = create_path(G, nodeA, nodeB, L)
    n = G[len(G) - 1].d
    return (L, n)

def create_path(G, s, v, L):
    if v == s:
        L.append(v)
    elif v.p == None:
        return None
    else:
        create_path(G, s, v.p, L)
        L.append(v)
    return L

def UpdateEdge(w, nodeA, nodeB, weight):
    if find_edge_value(w, nodeA, nodeB) != inf:
        for i in w:
            if i.first == nodeA and i.second == nodeB:
                i.val = weight
    else:
        w.append(Edge(nodeA, nodeB, weight))



if __name__ == "__main__":
    # Zadatak 1
    print ("\nZadatak 1 - MakeGraph()")
    (G, w) = MakeGraph()
    print([x.val for x in G])
    print([(x.first.val, x.second.val, x.val) for x in w])

    # Zadatak 2
    print ("\nZadatak 2 - GetInDegrees(), GetOutDegrees()")
    Lin = GetInDegrees(G, w)
    Lout = GetOutDegrees(G, w)

    for i in range(len(G)):
        print("Node:", G[i].val, "In degrees:", Lin[i], "Out degrees:", Lout[i])

    # Zadatak 3
    print ("\nZadatak 3 - ShortestPath()")
    bellman_ford(G, w, G[0])
    (L, n) = ShortestPath(G, G[0], G[6], w)
    
    print("Shortest path from", G[0].val, "to", G[6].val, "is", n)
    for i in range(len(L)):
        print(L[i].val, end = " ")
    print()

    # Zadatak 4
    print("\nZadatak 4 - UpdateEdge()")
    UpdateEdge(w, G[0], G[1], 8)
    UpdateEdge(w, G[1], G[2], -6)
    print([(x.first.val, x.second.val, x.val) for x in w])

    # Zadatak 5
    print("\nZadatak 5")
    bellman_ford(G, w, G[0])
    (L, n) = ShortestPath(G, G[0], G[6], w)
    
    print("New shortest path from", G[0].val, "to", G[6].val, "is", n)
    for i in range(len(L)):
        print(L[i].val, end = " ")
    print()