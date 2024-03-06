from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import graphFunctions

def main():    
    def addVertexUpdateMST():
        v=vertex1Var.get()
        if graphFunctions.vertexInGraph(v)==2 or graphFunctions.vertexInGraph(v)==1:
            return messagebox.showerror(title="Vertex error", message="Vertex already in graph")
        else:
            graphFunctions.addVertex(v)
            updateMSTLabel()
    def removeVertexUpdateMST():
        v=vertex1Var.get()
        if graphFunctions.vertexInGraph(v)==3:
            return messagebox.showerror(title="Vertex error", message="Vertex not in graph")
        elif graphFunctions.vertexInGraph(v)==1:
            return messagebox.showerror(title="StartVertex", message="StartVertex cant be removed")
        else:
            graphFunctions.removeVertex(v)
            updateMSTLabel()

    def addEdgeUpdateMST():
        v1= vertex2Var.get()
        v2= vertex1Var.get()
        inputWeight= weightVar.get()
        if graphFunctions.hasEdge(v1,v2):
            return messagebox.showerror(title="Edge error", message="Edge already exists")
        elif graphFunctions.vertexInGraph(v1)==3 or graphFunctions.vertexInGraph(v2)==3:
            return messagebox.showerror(title="Vertice error", message="One or Both of the chosen vertices not in graph")
        elif v1==v2:
            return messagebox.showerror(title="Vertice error", message="Cant connect vertex to itself")
        else:
            try:
                inputWeight = int(weightVar.get())
                if inputWeight<=0 or inputWeight>10:
                    return messagebox.showerror(title="Weight error", message="Weight should be between 1-10")
                else:
                    graphFunctions.addEdgeGUI(v1,v2,inputWeight)
                    updateMSTLabel()
            except ValueError:
                messagebox.showerror(title="Weight error", message="Weight should be type int")
                return
    def removeEdgeUpdateMST():   
        v1=vertex1Var.get()
        v2=vertex2Var.get()
        if graphFunctions.hasEdge(v1,v2):
            graphFunctions.removeEdge(v1,v2)
            updateMSTLabel()
        else: 
            messagebox.showerror(title="Edge Error", message="No Edge found")
            return

    def editEdgeUpdateMST():
        v1= vertex2Var.get()
        v2= vertex1Var.get()
        inputWeight= weightVar.get()
        if graphFunctions.hasEdge(v1,v2):
            try:
                inputWeight = int(weightVar.get())
                if inputWeight<=0 or inputWeight>10:
                    return messagebox.showerror(title="Weight error", message="Weight should be between 1-10")
                else:
                    graphFunctions.editEdgeWeight(v1, v2, inputWeight)
                    updateMSTLabel()
            except ValueError:
                messagebox.showerror(title="Weight error", message="Weight should be type int")
                return
        else:
            messagebox.showerror(title="Edge error", message="No edg found")

    def recalculateVerticePositions():
        graphFunctions.recalculateVerticePos(graphFunctions.G, graphFunctions.startVertex)

    def updateMSTLabel():
        mstweight=graphFunctions.calcMST(graphFunctions.G)
        if mstweight == 0:
            mstLabel.config(text="Graph is not connected or cant calculate MST", foreground="red")
        else:
            mstLabel.config(text=f"MST weight: {mstweight}", foreground="green")
            #print("MST from update func:", mstweight)

    def generateBtnClick():
        try:
            vertices = verticesVar.get()
            if 7 <= int(vertices) <= 15:
                G, mstweight, startVertex = graphFunctions.generateGraph(vertices)
                #print("mstweight from ttk", mstweight)
                mstLabel.config(text=f"MST weight: {mstweight}", foreground="green")
                graphFunctions.drawGraph(G, startVertex)
            else:
                mstLabel.config(text="Vertex count should be 7 to 15", foreground="red")
        except TclError:
            mstLabel.config(text="Vertex should be a number 7-15", foreground="red")

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
       
    ttk.Button(inputFrm, text="Generate Graph", command=generateBtnClick, style='Green.TButton').pack(side="top", padx=10, pady=5)

    inputFrm2 = ttk.Frame(root, padding=10)
    inputFrm2.pack(side="top", fill="x")

    vertex1Frm = ttk.Frame(inputFrm2, padding=5)
    vertex1Frm.pack(side="left", fill="x", expand=True)
    ttk.Label(vertex1Frm, text="Vertex 1").pack(side="top")
    vertex1Var = StringVar()
    ttk.Entry(vertex1Frm, textvariable=vertex1Var).pack(side="top")

    vertex2Frm = ttk.Frame(inputFrm2, padding=5)
    vertex2Frm.pack(side="left", fill="x", expand=True)
    ttk.Label(vertex2Frm, text="Vertex 2").pack(side="top")
    vertex2Var = StringVar()
    ttk.Entry(vertex2Frm, textvariable=vertex2Var).pack(side="top")

    weightFrm = ttk.Frame(inputFrm2, padding=5)
    weightFrm.pack(side="left", fill="x", expand=True)
    ttk.Label(weightFrm, text="Weight").pack(side="top")
    weightVar = StringVar()
    ttk.Entry(weightFrm, textvariable=weightVar).pack(side="top")

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
