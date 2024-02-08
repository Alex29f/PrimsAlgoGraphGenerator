import networkx as nx
import random

def verticeLetters(verticeCount):
    return [chr(65 + i) for i in range(verticeCount)]

def generateGraph(verticeCount):
    G = nx.Graph()
    vertices = verticeLetters(verticeCount)
    G.add_nodes_from(vertices)

    for i in range(1, verticeCount):
        G.add_edge(vertices[i], vertices[random.randint(0, i - 1)], weight=random.randint(1, 10))

    # loop kas parbauda loku skaitu
    while True:
        for node in G.nodes():
            while len(list(G.edges(node))) < 2:
                target = vertices[random.randint(0, verticeCount - 1)]
                if target != node and not G.has_edge(node, target):
                    G.add_edge(node, target, weight=random.randint(1, 10))

        if all(2 <= len(list(G.edges(node))) <= 5 for node in G.nodes()):
            break

    return G