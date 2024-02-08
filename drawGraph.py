import matplotlib.pyplot as plt
import networkx as nx
import io

def drawGraph(G):
    #plt.clf() ievietot šeit ja tiek izmantots plt.show()
    pos = nx.spring_layout(G) 

    nx.draw(G, pos,
            with_labels=True,
            node_color='lightblue',
            edge_color='gray',
            width=2         
            )
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
## šo daļu var aizstat ar  plt.show() ja grib lai katru rreizi tiktu atverts logs kuru saglabat
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    from PIL import Image
    img = Image.open(buf)

    return img 