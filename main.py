import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    #root.geometry('500x500') 
    style = ttk.Style()
    style.configure('Red.TButton', foreground='red')
    style.configure('Green.TButton', foreground='green')

    frm = ttk.Frame(root, padding=10)
    frm.pack(expand=True)
    ttk.Label(frm, text="Graph Generator for the purpose of teaching Prim's algorithm v1.0").pack(side="top", fill="both", pady=3, anchor="center")
    
    inputFrm = ttk.Frame(frm).pack(side="top", fill="x", padx=10, pady=1)
    ttk.Label(inputFrm, text="Enter Amount of Vertices for Graph {7-15}").pack(side="top")
    verticesVar = tk.StringVar()
    verticesCount = ttk.Entry(inputFrm, textvariable=verticesVar).pack(side="top")

    def generateBtnClick():
            vertices = verticesCount.get()
            if vertices.isdigit():
                print("succseful click")
            else:
                print("Please enter a valid integer")

    ttk.Button(inputFrm, text="Generate Graph", command=generateBtnClick, style='Green.TButton').pack(side="top", padx=10, pady=5)
    ## temporary to check 
  # Main frame configuration
    image_frame = ttk.Frame(root, padding=10)
    image_frame.pack(expand=True, fill=tk.BOTH)

    # Load an image using Pillow (PIL)
    # For a local image, replace 'path_to_image' with the file path
    image = Image.open('test.jpg')
    photo = ImageTk.PhotoImage(image)

    # Create a Label to display the image
    label = tk.Label(image_frame, image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection
    label.pack(expand=True, fill=tk.BOTH)

## temporary to check 


    quit_frame = ttk.Frame(root, padding=10)
    quit_frame.pack(side=tk.BOTTOM, fill=tk.X)
    quit_button = ttk.Button(quit_frame, text="Quit", command=root.destroy, style='Red.TButton')
    quit_button.pack(side=tk.BOTTOM)

    root.mainloop()

if __name__ == "__main__":
    main()
