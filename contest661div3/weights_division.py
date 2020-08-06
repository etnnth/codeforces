import math


class Vertex:
    def __init__(self):
        self.childs = set()
        self.weigth = 0
        self.parent = None
        self.decendances = None


def fill_tree(n):
    liste_edges = set()
    for edge in edges:
        if n == edge[0] or n == edge[1]:
            liste_edges.add(edge)
    for edge in liste_edges:
        if n == edge[0]:
            suivant, weigth = edge[1], edge[2]
        else:
            suivant, weigth = edge[0], edge[2]
        vertexs[n].childs.add(vertexs[suivant])
        vertexs[suivant].weigth = weigth
        vertexs[suivant].parent = vertexs[n]
        edges.remove(edge)
        fill_tree(suivant)


def compute_decendances(vertex):
    if len(vertex.childs) > 0:
        vertex.decendances = sum((compute_decendances(v) for v in vertex.childs))
        return vertex.decendances
    else:
        vertex.decendances = 1
        return 1


for _ in range(int(input())):
    number_vertex, max_weigth = [int(n) for n in input().split()]
    edges = set()
    for _ in range(number_vertex-1):
        v, u, w = input().split()
        edges.add((int(v), int(u), int(w)))
    vertexs = {i:Vertex() for i in range(1, number_vertex + 1)}
    moves = 0
    fill_tree(1)
    compute_decendances(vertexs[1])
    dec = [vertexs[k].decendances for k in vertexs]
    ws = [vertexs[k].weigth for k in vertexs]
    cumul = [d*w for d,w in zip(dec,ws)]
    while sum(cumul) > max_weigth:
        moves += 1
        diffs = [d * math.ceil(w/2) for d, w in zip(dec, ws)]
        indice = diffs.index(max(diffs))
        ws[indice] = math.floor(ws[indice]/2)
        cumul[indice] = dec[indice] * ws[indice]
    print(moves)




