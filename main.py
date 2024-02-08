import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from drawGraph import drawGraph
from generateGraph import generateGraph

def main():
    root = tk.Tk()
    style = ttk.Style()
    style.configure('Red.TButton', foreground='red')
    style.configure('Green.TButton', foreground='green')

    frm = ttk.Frame(root, padding=10)
    frm.pack(expand=True)
    ttk.Label(frm, text="Graph Generator for the purpose of teaching Prim's algorithm v1.0").pack(side="top", fill="both", pady=3, anchor="center")
    
    inputFrm = ttk.Frame(frm)
    inputFrm.pack(side="top", fill="x", padx=10, pady=1)
    ttk.Label(inputFrm, text="Enter Amount of Vertices for Graph {7-15}").pack(side="top")
    verticesVar = tk.StringVar()
    verticesCount = ttk.Entry(inputFrm, textvariable=verticesVar)
    verticesCount.pack(side="top")

    imageFrm = ttk.Frame(root, padding=2)
    imageFrm.pack(expand=True, fill=tk.BOTH)
    label = tk.Label(imageFrm)  # Create the label and store it in a variable
    label.pack(expand=True, fill=tk.BOTH)  # Now pack the label

    def generateBtnClick():
        vertices = verticesVar.get()
        if vertices.isdigit() and 7 <= int(vertices) <= 15:
            G = generateGraph(int(vertices))  # Generate the graph
            graph_image = drawGraph(G)        # Draw the graph and get the image
            photo = ImageTk.PhotoImage(graph_image)

            label.config(image=photo)
            label.image = photo  # Keep a reference to avoid garbage collection
        else:
            print("Please enter a valid integer between 7 and 15")


    ttk.Button(inputFrm, text="Generate Graph", command=generateBtnClick, style='Green.TButton').pack(side="top", padx=10, pady=5)

    quit_frame = ttk.Frame(root, padding=10)
    quit_frame.pack(side=tk.BOTTOM, fill=tk.X)
    quit_button = ttk.Button(quit_frame, text="Quit", command=root.destroy, style='Red.TButton')
    quit_button.pack(side=tk.BOTTOM)

    root.mainloop()

if __name__ == "__main__":
    main()
