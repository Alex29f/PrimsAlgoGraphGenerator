import networkx as nx
import random

def verticeLetters(verticeCount):
    return [chr(65 + i) for i in range(verticeCount)]

def generateGraph(verticeCount):
    G = nx.Graph()
    vertices = verticeLetters(verticeCount)
    G.add_nodes_from(vertices)

    for i in range(1, verticeCount):
        G.add_edge(vertices[i-1], vertices[i], weight=random.randint(1, 10))

    for node in vertices:
        while len(G.edges(node)) < 2 or (len(G.edges(node)) < 5 and random.random() > 0.5):
            target = random.choice(vertices)
            if target != node and not G.has_edge(node, target) and len(G.edges(target)) < 5:
                G.add_edge(node, target, weight=random.randint(1, 10))

    return G