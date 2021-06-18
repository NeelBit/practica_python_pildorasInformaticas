from tkinter import *

root = Tk()
root.title("Practica Entry")

miFrame = Frame(root, width=500, height=400)
miFrame.pack()

miEntry = Entry(miFrame)
miEntry.pack()

miEntry.place(x=100, y=100)

miLabel = Label(miFrame, text="Ingrese nombre: ")
miLabel.place(x=20, y=100) # si se utiliza la misma coordenada el primer widget empuja al siguiente!
#miLabel.pack()


root.mainloop()