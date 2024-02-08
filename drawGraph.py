import matplotlib.pyplot as plt
import networkx as nx

def drawGraph(G):
    pos = nx.spring_layout(G) 

    # Draw nodes and edges
    nx.draw(G, pos,
            with_labels=True,
            node_color='lightblue',
            edge_color='gray',
            width=2         
            )

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()