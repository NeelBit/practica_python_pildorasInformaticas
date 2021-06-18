from tkinter import *

root = Tk()

# hay que asignarle una variable y un valor, al igual que los entry?
varOpcion = IntVar()

Label(root, text="Seleccione sexo: ").pack()

# es comun que cuando se seleccione alguna opcion llame a una funcion, entonces escribimos una funcion:
def imprimir():

	#print(varOpcion.get()) # esto nos imprime o un 1 o un 2

	if (varOpcion.get() == 1):

		etiqueta.config(text="Masculino", bg="light blue")

	else:

		etiqueta.config(text="Femenino", bg="pink")

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()

Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()




root.mainloop()