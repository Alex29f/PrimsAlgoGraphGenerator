import networkx as nx
import random
##ASCII A=65.... Z=90
def verticeLetters(verticeCount):
     return [chr(65 + i) for i in range(verticeCount)]

def generateGraph(a):
    # Example usage
    verticeCount = 8 # a
    vertices = verticeLetters(verticeCount)
    #print(vertices)
    #vertices = ['A', 'B', 'C', 'D', 'E']
    
    Graph = nx.Graph()
    for vertex in vertices:
        Graph.add_node(vertex)

    ## algorithm to add edges and weights for specific cases
    randomEdgeCount= random.randint(2, 5) ## degree of each vertice
    #print(randomEdgeCount)
    Graph.add_edge('D', 'E', weight=6)

    # Print the graph's nodes and edges
    print("Nodes:", Graph.nodes())
    print("Edges:", Graph.edges(data=True))