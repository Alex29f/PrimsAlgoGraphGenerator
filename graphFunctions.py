import networkx as nx
import random
import matplotlib.pyplot as plt
fig = None
ax = None

def drawGraph(G, startVertex):
    global fig, ax
    if fig is None or ax is None:
        fig, ax = plt.subplots(figsize=(12, 10))
    else:
        ax.clear()
    pos = nx.spring_layout(G)
    node_colors = ['green' if node == startVertex else 'lightblue' for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', width=2, ax=ax)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    plt.show()

def generateGraph(verticeCount):
    global G,startVertex
    G=nx.Graph()
    vertices = verticeLetters(verticeCount)
    G.add_nodes_from(vertices)
    # virsotņu inicializācija svaru vēlākai implementācijai
    startVertex = random.choice(vertices)
    print("startvertex:", startVertex)# sakuma virsotne
    vertices.remove(startVertex)
    nextVertex = random.choice(vertices)# virsotne uz kuru paries prima algoritms
    print("nextVert:", nextVertex)
    vertices.remove(nextVertex)
    startWeight = random.randint(1, 2) # prima algoritma 1.iteracija vienmer izvelesies so svaru
    addEdge(G, startVertex, nextVertex, startWeight)

    #sākuma virsotnes loku pievienošana ta lai velak varetu 
    defaultVerticeCount=3
    if verticeCount==7: #grafam ar 7 virsotnem nebus liekas virsotnes ja nesamazinas lielumu
        defaultVerticeCount=2        
    startVertexVerticesCount = random.randint(1, defaultVerticeCount) 
    startVertexVertices = random.sample(vertices, startVertexVerticesCount)
    print("startVertexVertices:", startVertexVertices)
    unique_weights = [4, 5, 6]
    random.shuffle(unique_weights)
#sakuma virsonei ir pievienotas virsotnes ar loku svariem 4-6 
    #prima algoritma 3 iteracija atgriezisies pie 1 iteracija ieguta loka
    for v in startVertexVertices:
        vertices.remove(v)
        weight = unique_weights.pop()
        addEdge(G, startVertex, v, weight)

    # 2. nosacijuma implementacija - 2 soli jaizvelas starp 2 vienadam vertibam
    nextVertexVertices = random.sample(vertices, min(2, len(vertices)))
    print("nextVertexVertices:", nextVertexVertices)
    for v in nextVertexVertices:
        vertices.remove(v)
        addEdge(G, nextVertex, v, 3)

    #1. nosacijuma implementacija - jaizvelas vai atjaunot iezimes vertibu vai ne
    vertexstep1 = random.choice(vertices)
    print("vertexstep1:", vertexstep1)
    vertices.remove(vertexstep1)
    randomNextVertexVertex=random.choice(nextVertexVertices)
    randomWeightS1=random.randint(7, 10) 
    #no nextvertexvertices algoritms savienots ar vienu no brivajam virsotnem un sakuma virsotni
    G.add_edge(vertexstep1, startVertex, weight=randomWeightS1) 
    G.add_edge(vertexstep1,randomNextVertexVertex, weight=randomWeightS1) 
    #sakums 4 sola implementacija kur vajag panakt ka meklejot virsones visas jau ir ieklautas karkasa un iezimes neatjauno
    namedVertices = [vertexstep1, nextVertex, startVertex] + nextVertexVertices + startVertexVertices
    print("namedVertices", namedVertices)
    for v in G.nodes:
        while G.degree[v] < 2:
            potential_end = random.choice(list(G.nodes))
            if v != potential_end and G.degree[potential_end] < 5:
                if potential_end in namedVertices or v in namedVertices:
                    weight = random.randint(7, 10)
                else:
                    weight = random.randint(1, 6)
                addEdge(G, v, potential_end, weight)

    mst = nx.minimum_spanning_tree(G)
    mstweight = sum(mst[u][v]['weight'] for u, v in mst.edges())
    print("MST val:", mstweight)
    #drawGraph(G, startVertex)
    return G, mstweight, startVertex

def verticeLetters(verticeCount):
    return [chr(65 + i) for i in range(verticeCount)]

def addEdge(G, v1, v2, weight):
    if G.degree[v1] < 5 and G.degree[v2] < 5 and not G.has_edge(v1, v2):
        G.add_edge(v1, v2, weight=weight)
        return True
    return False

def removeVertex(v):
    if v == startVertex:
        print("StartVertex cant be removed")
        return
    if v in G:
        G.remove_node(v)
        drawGraph(G,startVertex)
        print("removed")
    else:
        print("Fail to remove")

def addVertex(v):
    if v not in G:
        G.add_node(v)
        drawGraph(G,startVertex)
        print("Added")
    else:
        print("Fail to add")


def removeEdge(v1, v2):
    if G.has_edge(v1, v2):
       G.remove_edge(v1, v2)
       drawGraph(G,startVertex)
       print("Edge removed")
    else:
       print("Failed to removeEdge")

def addEdgeGUI(v1, v2, weight): 
    if not G.has_edge(v1, v2):
        G.add_edge(v1, v2, weight=weight)
        drawGraph(G,startVertex)
        print("Edge added")
    else:
        print("Failed to add")

def editEdgeWeight(v1, v2, weight):
    if G.has_edge(v1, v2):
        G[v1][v2]['weight'] = weight
        drawGraph(G,startVertex)
        print("Edge Weight edited")
    else:
        print("failed to edit edge weight")