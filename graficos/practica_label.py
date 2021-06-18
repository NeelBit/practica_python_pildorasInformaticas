from tkinter import *

root = Tk()

root.title("Probando label")

# creamos el frame y pasamos parametros, va a estar en la raiz, ancho y alto
miFrame = Frame(root, width=500, height=400, bg="white")

miFrame.pack()


# creamos label y añadimos: primero parametro es el contenedor
miLabel = Label(miFrame, text="Esta es una etiqueta!") # muchos mas parametros podemos pasar!
#miLabel.pack() # hace que el frame y el marco tenga el tamaño del label, no qeremos eso entonces usamos place()

# donde queremos ubicar con parametros x and y
miLabel.place(x=100, y=200)

# si es que no vamos a volver a utilizar el label, se puede abreviar codigo de la siguiente manera:
Label(miFrame, text="Hola esta es otra label", fg="red", font=("arial", 18)).place(x=100, y=100)


# label con imagen:
imagen = PhotoImage(file="image.gif") # sin animacion el gif

Label(miFrame, image=imagen).place(x=100, y=300)





root.mainloop()