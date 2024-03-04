from tkinter import *
from tkinter import ttk
import graphFunctions

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
    verticesVar = IntVar()
    verticesVar.set("")
    verticesCount = ttk.Entry(inputFrm, textvariable=verticesVar)
    verticesCount.pack(side="top")

    mstLabel = ttk.Label(frm, text="MST weight will be shown here")
    mstLabel.pack(side="top", pady=5)
    def updateMSTLabel():
        mstweight=graphFunctions.calcMST(graphFunctions.G)
        if mstweight == 0:
            mstLabel.config(text="Graph is not connected or cant calculate MST", foreground="red")
        else:
            mstLabel.config(text=f"MST weight: {mstweight}", foreground="green")
            print("MST from update func:", mstweight)

    def generateBtnClick():
        try:
            vertices = verticesVar.get()
            if 7 <= int(vertices) <= 15:
                G, mstweight, startVertex = graphFunctions.generateGraph(vertices)
                print("mstweight from ttk", mstweight)
                mstLabel.config(text=f"MST weight: {mstweight}", foreground="green")
                graphFunctions.drawGraph(G, startVertex)
            else:
                mstLabel.config(text="Vertex count should be 7 to 15", foreground="red")
        except TclError:
            mstLabel.config(text="Vertex should be a number 7-15", foreground="red")

    
    ttk.Button(inputFrm, text="Generate Graph", command=generateBtnClick, style='Green.TButton').pack(side="top", padx=10, pady=5)

    inputFrm = ttk.Frame(root, padding=10)
    inputFrm.pack(side="top", fill="x")

    vertex1Frm = ttk.Frame(inputFrm, padding=5)
    vertex1Frm.pack(side="left", fill="x", expand=True)
    ttk.Label(vertex1Frm, text="Vertex 1").pack(side="top")
    vertex1Var = StringVar()
    ttk.Entry(vertex1Frm, textvariable=vertex1Var).pack(side="top")

    vertex2Frm = ttk.Frame(inputFrm, padding=5)
    vertex2Frm.pack(side="left", fill="x", expand=True)
    ttk.Label(vertex2Frm, text="Vertex 2").pack(side="top")
    vertex2Var = StringVar()
    ttk.Entry(vertex2Frm, textvariable=vertex2Var).pack(side="top")

    weightFrm = ttk.Frame(inputFrm, padding=5)
    weightFrm.pack(side="left", fill="x", expand=True)
    ttk.Label(weightFrm, text="Weight").pack(side="top")
    weightVar = StringVar()
    ttk.Entry(weightFrm, textvariable=weightVar).pack(side="top")

    def addVertexUpdateMST():
        graphFunctions.addVertex(vertex1Var.get())
        updateMSTLabel()

    def removeVertexUpdateMST():
        graphFunctions.removeVertex(vertex1Var.get())
        updateMSTLabel()

    def addEdgeUpdateMST():
        try:
            weight= int(weightVar.get())
        except ValueError:
            print("Value of weight not a number")
    
        graphFunctions.addEdgeGUI(vertex1Var.get(), vertex2Var.get(), weight)
        updateMSTLabel()

    def removeEdgeUpdateMST():     
        graphFunctions.removeEdge(vertex1Var.get(), vertex2Var.get())
        updateMSTLabel()

    def editEdgeUpdateMST():
        try:
            weight= int(weightVar.get())
        except ValueError:
            print("Value of weight not a number")
        graphFunctions.editEdgeWeight(vertex1Var.get(), vertex2Var.get(), weight)
        updateMSTLabel()
    def recalculateVerticePositions():
        graphFunctions.recalculateVerticePos(graphFunctions.G, graphFunctions.startVertex)
        


    buttonFrm = ttk.Frame(root, padding=10)
    buttonFrm.pack(side="top", fill="x")
    ttk.Button(buttonFrm, text="Remove Vertex", command=lambda: removeVertexUpdateMST(), style='TButton').pack(side="left", padx=5,expand=True)
    ttk.Button(buttonFrm, text="Add Vertex", command=lambda: addVertexUpdateMST(), style='TButton').pack(side="left", padx=5,expand=True)
    ttk.Button(buttonFrm, text="Remove Edge", command=lambda: removeEdgeUpdateMST(), style='TButton').pack(side="left", padx=5,expand=True)
    ttk.Button(buttonFrm, text="Add Edge", command=lambda: addEdgeUpdateMST(), style='TButton').pack(side="left", padx=5,expand=True)
    ttk.Button(buttonFrm, text="Edit Edge Weight", command=lambda: editEdgeUpdateMST(), style='TButton').pack(side="left", padx=5,expand=True)
    ttk.Button(buttonFrm, text="Recalculate vertice positions", command=lambda:recalculateVerticePositions(), style='TButton').pack(side="left", padx=5,expand=True)
    infoFrm = ttk.Frame(root, padding=10)
    infoFrm.pack(side="top", fill="x")
    ttk.Label(infoFrm, text="If you want to add or remove Vertex use only vertex1 field").pack(side="top")
    quitFrm = ttk.Frame(root, padding=10)
    quitFrm.pack(side=BOTTOM, fill=X)
    quitButton = ttk.Button(quitFrm, text="Quit", command=root.destroy, style='Red.TButton')
    quitButton.pack(side=BOTTOM)

    root.mainloop()


if __name__ == "__main__":
    main()
