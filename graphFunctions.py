import networkx as nx
import matplotlib.pyplot as plt
import random

class GraphFunctions:
    def __init__(self):
        self.G= nx.Graph()
        self.startVertex= None
        self.pos= None
        self.fig= None
        self.ax= None
    def drawGraph(self):
        if self.fig is None or not plt.fignum_exists(self.fig.number):
            self.fig, self.ax = plt.subplots(figsize=(12, 10))
        else:
            self.ax.clear()
        if self.pos is None:
            self.pos = nx.spring_layout(self.G) 
        node_colors = ['green' if node == self.startVertex else 'lightblue' for node in self.G.nodes()]
        nx.draw(self.G, self.pos, with_labels=True, node_color=node_colors, edge_color='gray', width=2, ax=self.ax)
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_labels, ax=self.ax, rotate=False)
        plt.show()
    def drawMST(self):
        T = nx.minimum_spanning_tree(self.G,algorithm="prim")
        nx.draw_networkx_edges(T, self.pos, edge_color="red", width=3)
        edge_labels = nx.get_edge_attributes(self.G, 'weight') #ja nav šis tad mst zīmē pa virsu svariem
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_labels, ax=self.ax, rotate=False)
        plt.show()
    def generateGraph(self,verticeCount):
        self.G=nx.Graph()
        vertices = self.verticeLetters(verticeCount)
        self.G.add_nodes_from(vertices)
        # virsotņu inicializācija svaru vēlākai implementācijai
        self.startVertex = random.choice(vertices)
        #print("startvertex:", startVertex)# sakuma virsotne
        vertices.remove(self.startVertex)
        nextVertex = random.choice(vertices)# virsotne uz kuru paries prima algoritms
        #print("nextVert:", nextVertex)
        vertices.remove(nextVertex)
        startWeight = 1#random.randint(1, 2) # prima algoritma 1.iteracija vienmer izvelesies so svaru
        self.addEdge(self.startVertex, nextVertex, startWeight)
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
            self.addEdge(self.startVertex, v, weight)

        # 2. nosacijuma implementacija - 2 soli jaizvelas starp 2 vienadam vertibam
        nextVertexVertices = random.sample(vertices, min(2, len(vertices)))
        #print("nextVertexVertices:", nextVertexVertices)
        for v in nextVertexVertices:
            vertices.remove(v)
            self.addEdge(nextVertex, v, 2)

        #1. nosacijuma implementacija - jaizvelas vai atjaunot iezimes vertibu vai ne
        vertexstep1 = random.choice(vertices)
        #print("vertexstep1:", vertexstep1)
        vertices.remove(vertexstep1)
        randomNextVertexVertex=random.choice(nextVertexVertices)
        randomWeightS1=random.randint(7, 10) 
        #no nextvertexvertices algoritms savienots ar vienu no brivajam virsotnem un sakuma virsotni
        self.G.add_edge(vertexstep1, self.startVertex, weight=randomWeightS1) 
        self.G.add_edge(vertexstep1,randomNextVertexVertex, weight=randomWeightS1) 
        #sakums 4 sola implementacija kur vajag panakt ka meklejot virsones visas jau ir ieklautas karkasa un iezimes neatjauno
        nextVertexVertices.remove(randomNextVertexVertex)
        nextVertexVertex2 = nextVertexVertices[0]
        print("hello from next vvertex vertex2:", nextVertexVertex2)
        vertexStep4=random.choice(vertices)
        vertices.remove(vertexStep4)
        weight4=random.randint(7, 10)
        self.G.add_edge(vertexStep4, nextVertex, weight=weight4) 
        self.G.add_edge(vertexStep4,nextVertexVertex2, weight=6)

        namedVertices = [vertexStep4, vertexstep1, nextVertex, self.startVertex, randomNextVertexVertex, nextVertexVertex2] + startVertexVertices
        #print("namedVertices", namedVertices)
        for v in self.G.nodes:
            while self.G.degree[v] < 2:
                potentialEnd = random.choice(list(self.G.nodes))
                if v != potentialEnd and self.G.degree[potentialEnd] < 5 and potentialEnd != vertexStep4:
                    if potentialEnd in namedVertices or v in namedVertices:
                        weight = random.randint(7, 10)
                    else:
                        weight = random.randint(1, 6)
                    self.addEdge(v, potentialEnd, weight)

        mstweight=self.calcMST()
        #drawGraph(G, startVertex)
        self.pos=nx.spring_layout(self.G)
        return mstweight
        
    def verticeLetters(self,verticeCount):
         return [chr(65 + i) for i in range(verticeCount)]

    def addEdge(self, v1, v2, weight):
        if self.G.degree[v1] < 5 and self.G.degree[v2] < 5 and not self.G.has_edge(v1, v2):
            self.G.add_edge(v1, v2, weight=weight)
            return True
        return False
    def removeVertex(self,v):
        if v == self.startVertex:
            #print("StartVertex cant be removed")
            return
        if v in self.G:
            self.G.remove_node(v)
            if v in self.pos:
                del self.pos[v]
            self.drawGraph()
            #print("removed")
        else:
            return
            #print("Fail to remove")

    def addVertex(self,v):
        if v not in self.G:
            self.G.add_node(v)
            oldNodes=list(self.G.nodes())
            oldNodes.remove(v)
            self.pos=nx.spring_layout(self.G,pos=self.pos,fixed=oldNodes)
            self.drawGraph()
            #print("Added")
        else:
            return
            #print("Fail to add")

    def removeEdge(self,v1, v2):
        if self.G.has_edge(v1, v2):
            self.G.remove_edge(v1, v2)
            self.drawGraph()
            #print("Edge removed")
        else:
            #print("Failed to removeEdge")
            return

    def addEdgeGUI(self,v1, v2, weight): 
        if not self.G.has_edge(v1, v2):
            self.G.add_edge(v1, v2, weight=weight)
            self.drawGraph()
            #print("Edge added")
        else:
            #print("Failed to add")
            return

    def editEdgeWeight(self,v1, v2, weight):
        if self.G.has_edge(v1, v2):
            self.G[v1][v2]['weight'] = weight
            self.drawGraph()
            #print("Edge Weight edited")
        else:
            #print("failed to edit edge weight")
            return
    def calcMST(self):
        if nx.is_connected(self.G):
            mst = nx.minimum_spanning_tree(self.G,algorithm="prim")
            mstweight = sum(mst[u][v]['weight'] for u, v in mst.edges())
            #print("MST val:", mstweight)
            return mstweight
        else:
            return 0
    def recalculateVerticePos(self):
        self.pos=nx.spring_layout(self.G,pos=self.pos)
        self.drawGraph()
    def vertexInGraph(self,v):
        if v==self.startVertex:
            return 1
        elif self.G.has_node(v):   
            return 2
        else:
            return 3
    def hasEdge(self,v1, v2):
        if self.G.has_edge(v1,v2):
            return True
        else:
            return False
    def pltOpen(self):
        if plt.get_fignums():
            return True
        else:
            return False
    def closePLT(self):
        plt.close()
