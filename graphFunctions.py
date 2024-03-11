import networkx as nx
import random
import matplotlib.pyplot as plt
fig = None
ax = None
pos=None
def drawGraph(G, startVertex):
    global fig, ax, pos
    if fig is None or not plt.fignum_exists(fig.number):
        fig, ax = plt.subplots(figsize=(12, 10))
    else:
        ax.clear()
    if pos is None:
        pos = nx.spring_layout(G)    
    #print(pos, "POS mainiga vert")    
    node_colors = ['green' if node == startVertex else 'lightblue' for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color='gray', width=2, ax=ax)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, rotate=False)
    plt.show()
def drawMST():
    T = nx.minimum_spanning_tree(G,algorithm="prim")
    nx.draw_networkx_edges(T, pos, edge_color="red", width=3)
    edge_labels = nx.get_edge_attributes(G, 'weight') #ja nav šis tad mst zīmē pa virsu svariem
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax, rotate=False)
    plt.show()
def removeDrawnMST():
    drawGraph(G,startVertex)

def generateGraph(verticeCount):
    global G,startVertex,pos
    G=nx.Graph()
    vertices = verticeLetters(verticeCount)
    G.add_nodes_from(vertices)
    # virsotņu inicializācija svaru vēlākai implementācijai
    startVertex = random.choice(vertices)
    #print("startvertex:", startVertex)# sakuma virsotne
    vertices.remove(startVertex)
    nextVertex = random.choice(vertices)# virsotne uz kuru paries prima algoritms
    #print("nextVert:", nextVertex)
    vertices.remove(nextVertex)
    startWeight = 1#random.randint(1, 2) # prima algoritma 1.iteracija vienmer izvelesies so svaru
    addEdge(G, startVertex, nextVertex, startWeight)

    #sākuma virsotnes loku pievienošana ta lai velak varetu 
    defaultVerticeCount=3
    if verticeCount==7: #grafam ar 7 virsotnem nebus liekas virsotnes ja nesamazinas lielumu
        defaultVerticeCount=1
    elif verticeCount==8:
        defaultVerticeCount=2
    startVertexVerticesCount = random.randint(1, defaultVerticeCount) 
    startVertexVertices = random.sample(vertices, startVertexVerticesCount)
    #print("startVertexVertices:", startVertexVertices)
    uniqueWeights = [5,4,3]
    #random.shuffle(uniqueWeights)
#sakuma virsonei ir pievienotas virsotnes ar loku svariem 4-6 
    #prima algoritma 3 iteracija atgriezisies pie 1 iteracija ieguta loka
    for v in startVertexVertices:
        vertices.remove(v)
        weight = uniqueWeights.pop()
        addEdge(G, startVertex, v, weight)

    # 2. nosacijuma implementacija - 2 soli jaizvelas starp 2 vienadam vertibam
    nextVertexVertices = random.sample(vertices, min(2, len(vertices)))
    #print("nextVertexVertices:", nextVertexVertices)
    for v in nextVertexVertices:
        vertices.remove(v)
        addEdge(G, nextVertex, v, 2)

    #1. nosacijuma implementacija - jaizvelas vai atjaunot iezimes vertibu vai ne
    vertexstep1 = random.choice(vertices)
    #print("vertexstep1:", vertexstep1)
    vertices.remove(vertexstep1)
    randomNextVertexVertex=random.choice(nextVertexVertices)
    randomWeightS1=random.randint(7, 10) 
    #no nextvertexvertices algoritms savienots ar vienu no brivajam virsotnem un sakuma virsotni
    G.add_edge(vertexstep1, startVertex, weight=randomWeightS1) 
    G.add_edge(vertexstep1,randomNextVertexVertex, weight=randomWeightS1) 
    #sakums 4 sola implementacija kur vajag panakt ka meklejot virsones visas jau ir ieklautas karkasa un iezimes neatjauno
    nextVertexVertices.remove(randomNextVertexVertex)
    nextVertexVertex2 = nextVertexVertices[0]
    print("hello from next vvertex vertex2:", nextVertexVertex2)
    vertexStep4=random.choice(vertices)
    vertices.remove(vertexStep4)
    weight4=random.randint(7, 10)
    G.add_edge(vertexStep4, nextVertex, weight=weight4) 
    G.add_edge(vertexStep4,nextVertexVertex2, weight=6)

    namedVertices = [vertexStep4, vertexstep1, nextVertex, startVertex, randomNextVertexVertex, nextVertexVertex2] + startVertexVertices
    #print("namedVertices", namedVertices)
    for v in G.nodes:
        while G.degree[v] < 2:
            potentialEnd = random.choice(list(G.nodes))
            if v != potentialEnd and G.degree[potentialEnd] < 5 and potentialEnd != vertexStep4:
                if potentialEnd in namedVertices or v in namedVertices:
                    weight = random.randint(7, 10)
                else:
                    weight = random.randint(1, 6)
                addEdge(G, v, potentialEnd, weight)

    mstweight=calcMST(G)
    #drawGraph(G, startVertex)
    pos=nx.spring_layout(G)
    return G, mstweight, startVertex

def verticeLetters(verticeCount):
    return [chr(65 + i) for i in range(verticeCount)]

def addEdge(G, v1, v2, weight):
    if G.degree[v1] < 5 and G.degree[v2] < 5 and not G.has_edge(v1, v2):
        G.add_edge(v1, v2, weight=weight)
        return True
    return False

def removeVertex(v):
    global pos
    if v == startVertex:
        #print("StartVertex cant be removed")
        return
    if v in G:
        G.remove_node(v)
        if v in pos:
            del pos[v]
        drawGraph(G,startVertex)
        #print("removed")
    else:
        return
        #print("Fail to remove")

def addVertex(v):
    global pos
    if v not in G:
        G.add_node(v)
        oldNodes=list(G.nodes())
        oldNodes.remove(v)
        pos=nx.spring_layout(G,pos=pos,fixed=oldNodes)
        drawGraph(G,startVertex)
        #print("Added")
    else:
        return
        #print("Fail to add")

def removeEdge(v1, v2):
    if G.has_edge(v1, v2):
       G.remove_edge(v1, v2)
       drawGraph(G,startVertex)
       #print("Edge removed")
    else:
       #print("Failed to removeEdge")
       return

def addEdgeGUI(v1, v2, weight): 
    if not G.has_edge(v1, v2):
        G.add_edge(v1, v2, weight=weight)
        drawGraph(G,startVertex)
        #print("Edge added")
    else:
        #print("Failed to add")
        return

def editEdgeWeight(v1, v2, weight):
    if G.has_edge(v1, v2):
        G[v1][v2]['weight'] = weight
        drawGraph(G,startVertex)
        #print("Edge Weight edited")
    else:
        #print("failed to edit edge weight")
        return
def calcMST(G):
    if nx.is_connected(G):
        mst = nx.minimum_spanning_tree(G,algorithm="prim")
        mstweight = sum(mst[u][v]['weight'] for u, v in mst.edges())
        #print("MST val:", mstweight)
        return mstweight
    else:
        return 0
def recalculateVerticePos(G,startVertex):
    global pos
    pos=nx.spring_layout(G)
    drawGraph(G,startVertex)
def vertexInGraph(v):
    if v==startVertex:
        return 1
    elif G.has_node(v):   
        return 2
    else:
        return 3
def hasEdge(v1, v2):
    if G.has_edge(v1,v2):
        return True
    else:
        return False
