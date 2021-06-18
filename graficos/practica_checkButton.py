from tkinter import *

root = Tk()

root.title("Practica checkbutton")

playa = IntVar()
monta = IntVar()
turismo = IntVar()

def opcionesViaje():

	opcionSeleccionada = ""

	if (playa.get() == 1):

		# incremente este string
		opcionSeleccionada += " Playa"

	if (monta.get() == 1):

		opcionSeleccionada += " Montaña"

	if (turismo.get() == 1):

		opcionSeleccionada += " Turismo rural"


	textoFinal.config(text=opcionSeleccionada, bg="Green", font=14)

image = PhotoImage(file="help.png")
Label(root, image=image).pack()

Label(root, text="Elige destinos:").pack()

# frame para meter los Checkbutton:
frame = Frame(root)
frame.pack()

# onvalue para decirle el valro que toma cuando se seleeciona lo que le decime en variable, y offvalue el valor cuando no este seleccionado
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).grid(row=1, column=1, sticky="w")

Checkbutton(frame, text="Montaña", variable=monta, onvalue=1, offvalue=0, command=opcionesViaje).grid(row=2, column=1, sticky="w")

Checkbutton(frame, text="Turismo rural", variable=turismo, onvalue=1, offvalue=0, command=opcionesViaje).grid(row=3, column=1, sticky="w")


textoFinal = Label(root)
textoFinal.pack()



root.mainloop()