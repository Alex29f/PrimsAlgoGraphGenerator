from tkinter import *
from tkinter import ttk
from generateGraph import generateGraph
from generateGraph import drawGraph
#from PIL import Image, ImageTk
#import gc
#from drawGraph import drawGraph

def main():
    root = Tk()
    style = ttk.Style()
    style.configure('Red.TButton', foreground='red')
    style.configure('Green.TButton', foreground='green')

    frm = ttk.Frame(root, padding=10)
    frm.pack(expand=True)
    ttk.Label(frm, text="Graph Generator for the purpose of teaching Prim's algorithm v1.0").pack(side="top", fill="both", pady=3, anchor="center")
    
    inputFrm = ttk.Frame(frm)
    inputFrm.pack(side="top", fill="x", padx=10, pady=1)
    ttk.Label(inputFrm, text="Enter Amount of Vertices for Graph {7-15}").pack(side="top")
    verticesVar = StringVar()
    verticesCount = ttk.Entry(inputFrm, textvariable=verticesVar)
    verticesCount.pack(side="top")

    imageFrm = ttk.Frame(root, padding=2)
    imageFrm.pack(expand=True, fill=BOTH)
    label = Label(imageFrm)
    label.pack(expand=True, fill=BOTH)  

    mstLabel = ttk.Label(frm, text="MST weight will be shown here")
    mstLabel.pack(side="top", pady=5)
    def generateBtnClick():
        vertices = verticesVar.get()
        if vertices.isdigit() and 7 <= int(vertices) <= 15:
            G, mstweight,startVertex=generateGraph(int(vertices))
            print("mstweight from ttk", mstweight)
            mstLabel.config(text=f"MST weight: {mstweight}", foreground="green")
            drawGraph(G, startVertex)
            #root.update_idletasks()#salabo to ka 1.reize neparadas mst
            #uncomment this portion and drawGraph2 function for the graph to be drawn in tkinter window not new window
            #photo = ImageTk.PhotoImage(graph_image)
            #label.config(image=photo)
            #label.image = photo
            #gc.collect()
        else:
            #sito japartaisa par popup
            mstLabel.config(text="Vertex count should be 7 to 15", foreground="red")
            #print("input 7 to 15")

    ttk.Button(inputFrm, text="Generate Graph", command=generateBtnClick, style='Green.TButton').pack(side="top", padx=10, pady=5)

    quitFrm = ttk.Frame(root, padding=10)
    quitFrm.pack(side=BOTTOM, fill=X)
    quitButton = ttk.Button(quitFrm, text="Quit", command=root.destroy, style='Red.TButton')
    quitButton.pack(side=BOTTOM)

    root.mainloop()

if __name__ == "__main__":
    main()
