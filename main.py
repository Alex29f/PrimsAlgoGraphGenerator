from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from graphFunctions import GraphFunctions

def main():
    graph=GraphFunctions()
    def quit():#aizver ari plt logu
        if graph.pltOpen():
            graph.closePLT()
        root.destroy()
    def checkIfGraphCreated():
        if graph.pltOpen():
            return True
        else:
            return messagebox.showerror(title="Graph not Created", message="Graph not Created")
    def drawMST():
        if checkIfGraphCreated()!=True:
            return
        graph.drawMST()
    def removeMST():
        if checkIfGraphCreated()!=True:
            return
        graph.drawGraph()

    def addVertexUpdateMST():
        if checkIfGraphCreated()!=True:
            return
        v=vertex1Var.get()
        if v=="":
            return messagebox.showerror(title="Vertex error", message="Vertex value cannt be empty")
        if graph.vertexInGraph(v)==2 or graph.vertexInGraph(v)==1:
            return messagebox.showerror(title="Vertex error", message="Vertex already in graph")
        else:
            graph.addVertex(v)
            updateMSTLabel()
    def removeVertexUpdateMST():
        if checkIfGraphCreated()!=True:
            return
        v=vertex1Var.get()
        if graph.vertexInGraph(v)==3:
            return messagebox.showerror(title="Vertex error", message="Vertex not in graph")
        elif graph.vertexInGraph(v)==1:
            return messagebox.showerror(title="StartVertex", message="StartVertex cant be removed")
        else:
            graph.removeVertex(v)
            updateMSTLabel()

    def addEdgeUpdateMST():
        if checkIfGraphCreated()!=True:
            return
        v1= vertex2Var.get()
        v2= vertex1Var.get()
        inputWeight= weightVar.get()
        if graph.hasEdge(v1,v2):
            return messagebox.showerror(title="Edge error", message="Edge already exists")
        elif graph.vertexInGraph(v1)==3 or graph.vertexInGraph(v2)==3:
            return messagebox.showerror(title="Vertice error", message="One or Both of the chosen vertices not in graph")
        elif v1==v2:
            return messagebox.showerror(title="Vertice error", message="Cant connect vertex to itself")
        else:
            try:
                inputWeight = int(weightVar.get())
                if inputWeight<=0 or inputWeight>10:
                    return messagebox.showerror(title="Weight error", message="Weight should be between 1-10")
                else:
                    graph.addEdgeGUI(v1,v2,inputWeight)
                    updateMSTLabel()
            except ValueError:
                messagebox.showerror(title="Weight error", message="Weight should be type int")
                return
    def removeEdgeUpdateMST(): 
        if checkIfGraphCreated()!=True:
            return  
        v1=vertex1Var.get()
        v2=vertex2Var.get()
        if graph.hasEdge(v1,v2):
            graph.removeEdge(v1,v2)
            updateMSTLabel()
        else: 
            messagebox.showerror(title="Edge Error", message="No Edge found")
            return

    def editEdgeUpdateMST():
        if checkIfGraphCreated()!=True:
            return
        v1= vertex2Var.get()
        v2= vertex1Var.get()
        inputWeight= weightVar.get()
        if graph.hasEdge(v1,v2):
            try:
                inputWeight = int(weightVar.get())
                if inputWeight<=0 or inputWeight>10:
                    return messagebox.showerror(title="Weight error", message="Weight should be between 1-10")
                else:
                    graph.editEdgeWeight(v1, v2, inputWeight)
                    updateMSTLabel()
            except ValueError:
                messagebox.showerror(title="Weight error", message="Weight should be type int")
                return
        else:
            messagebox.showerror(title="Edge error", message="No edg found")

    def recalculateVerticePositions():
        if checkIfGraphCreated()!=True:
            return
        graph.recalculateVerticePos()

    def updateMSTLabel():
        mstweight=graph.calcMST()
        if mstweight == 0:
            mstLabel.config(text="Graph is not connected or cant calculate MST", foreground="red")
        else:
            mstLabel.config(text=f"MST weight: {mstweight}", foreground="green")
            #print("MST from update func:", mstweight)

    def generateBtnClick():
        try:
            vertices = verticesVar.get()
            if 7 <= int(vertices) <= 15:
                mstweight = graph.generateGraph(vertices)
                #print("mstweight from ttk", mstweight)
                mstLabel.config(text=f"MST weight: {mstweight}", foreground="green")
                graph.drawGraph()
            else:
                mstLabel.config(text="Vertex count should be 7 to 15", foreground="red")
        except TclError:
            mstLabel.config(text="Vertex should be a number 7-15", foreground="red")

    root = Tk()
    root.title("Specific Weight Graph Generator for Prims Algorithm")
    style = ttk.Style()
    style.configure('Red.TButton', foreground='red')
    style.configure('Green.TButton', foreground='green')

    frm = ttk.Frame(root, padding=2)
    frm.pack(expand=True, fill='both')
    ttk.Label(frm, text="Graph Generator for the purpose of teaching Prim's algorithm v1.0").pack(side="top", fill="both", pady=1, anchor="center")
    
    inputFrm = ttk.Frame(frm,padding=1)
    inputFrm.pack(side="top", fill="x",expand=True)
    ttk.Label(inputFrm, text="Enter Amount of Vertices for Graph {7-15}").pack(side="top")
    verticesVar = IntVar()
    verticesVar.set("")
    verticesCount = ttk.Entry(inputFrm, textvariable=verticesVar)
    verticesCount.pack(side="top")
    mstLabel = ttk.Label(frm, text="MST weight will be shown here")
    mstLabel.pack(side="top", pady=1)
    ttk.Button(inputFrm, text="Generate Graph", command=generateBtnClick, style='Green.TButton').pack(side="top", padx=2, pady=2)

    inputFrm2 = ttk.Frame(frm, padding=1)
    inputFrm2.pack(side="top", fill="x",expand=True)

    vertex1Frm = ttk.Frame(inputFrm2, padding=2)
    vertex1Frm.pack(side="left", fill="x",expand=True)
    ttk.Label(vertex1Frm, text="Vertex 1").pack(side="top")
    vertex1Var = StringVar()
    ttk.Entry(vertex1Frm, textvariable=vertex1Var).pack(side="top")

    vertex2Frm = ttk.Frame(inputFrm2, padding=2)
    vertex2Frm.pack(side="left", fill="x",expand=True)
    ttk.Label(vertex2Frm, text="Vertex 2").pack(side="top")
    vertex2Var = StringVar()
    ttk.Entry(vertex2Frm, textvariable=vertex2Var).pack(side="top")

    weightFrm = ttk.Frame(inputFrm2, padding=2)
    weightFrm.pack(side="left", fill="x",expand=True)
    ttk.Label(weightFrm, text="Weight").pack(side="top")
    weightVar = StringVar()
    ttk.Entry(weightFrm, textvariable=weightVar).pack(side="top")

    buttonFrm1 = ttk.Frame(frm, padding=2)
    buttonFrm1.pack(side="top", fill="x",expand=True)
    ttk.Button(buttonFrm1,width=20, text="Add Vertex", command=addVertexUpdateMST, style='TButton').pack(side="left", expand=True)
    ttk.Button(buttonFrm1,width=20, text="Add Edge", command=addEdgeUpdateMST, style='TButton').pack(side="left", expand=True)
    ttk.Button(buttonFrm1,width=20, text="Edit Edge Weight", command=editEdgeUpdateMST, style='TButton').pack(side="left", expand=True)
    buttonFrm2 = ttk.Frame(frm, padding=2)
    buttonFrm2.pack(side="top", fill="x",expand=True)
    ttk.Button(buttonFrm2,width=20, text="Remove Vertex", command=removeVertexUpdateMST, style='TButton').pack(side="left", expand=True)
    ttk.Button(buttonFrm2,width=20, text="Remove Edge", command=removeEdgeUpdateMST, style='TButton').pack(side="left", expand=True)
    ttk.Button(buttonFrm2,width=20, text="Recalculate vertices", command=recalculateVerticePositions, style='TButton').pack(side="left", expand=True)

    infoFrm = ttk.Frame(frm, padding=2)
    infoFrm.pack(side="top", fill="x",expand=True)
    ttk.Label(infoFrm, text="If you want to add or remove Vertex use only vertex1 field").pack(side="top")

    mstFrm=ttk.Frame(frm, padding=2)
    mstFrm.pack(side="top", fill="x",expand=True)
    ttk.Button(mstFrm,width=20, text="Show MST", command=drawMST, style='Green.TButton').pack(side="left", expand=True)
    ttk.Button(mstFrm,width=20, text="Hide MST", command=removeMST, style='Red.TButton').pack(side="left", expand=True)
    quitFrm = ttk.Frame(root, padding=1)
    quitFrm.pack(side=BOTTOM, fill="x")
    quitButton = ttk.Button(quitFrm, text="Quit", command=quit, style='Red.TButton')
    quitButton.pack(side=BOTTOM)

    root.mainloop()
if __name__ == "__main__":
    main()
