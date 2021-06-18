from tkinter import *

raiz = Tk()
raiz.title("Probando grid/rejilla")
raiz.config(bg="black")

miFrame = Frame(raiz, width=500, height=400, bg="white")


miFrame.pack(fill="both", expand="True") # expandir el frame junto con el marco

# indicamos que la variable, se trata de una cadena de caracteres!!!!!!!!!!!!!!!!!!!!!!!!
miNombre = StringVar()


#
labelNombre = Label(miFrame, text="Ingrese nombre: ", bg="white")
labelNombre.grid(row="0", column="0", sticky="w", padx=10, pady=10) # sticky=puntocardinal - para posicional contenido w = west(oeste) - e east (este)

entryNombre = Entry(miFrame, textvariable=miNombre) # textvariable para asociar a variable de arriba, este valor lo asociamos cuando pulsamoe el boton de enviar!!!!!!
entryNombre.grid(row="0", column="1", padx=10, pady=10)

entryNombre.config(fg="red", justify="center") # cambiamos el color frontal de lo que escribamos en el cuadro de texto, cambiar alineacion del texto dentro del cuadro

#
labelApellido = Label(miFrame, text="Ingrese apellido: ", bg="white")
labelApellido.grid(row=1, column=0, sticky="w", padx=10, pady=10)

entryApellido = Entry(miFrame)
entryApellido.grid(row=1, column=1, padx=10, pady=10)

#
labelDireccion = Label(miFrame, text="Ingrese direccion: ", bg="white")
labelDireccion.grid(row=2, column=0, sticky="w", padx=10, pady=10)

entrydireccion = Entry(miFrame)
entrydireccion.grid(row=2, column=1, padx=10, pady=10)

#
# CAMPO PASSWORD!!!
labelPass = Label(miFrame, text="Ingrese password: ", bg="white")
labelPass.grid(row=3, column=0, sticky="w", padx=10, pady=10)

entryPass = Entry(miFrame)
entryPass.grid(row=3, column=1, padx=10, pady=10)

entryPass.config(show="*") # show para que muestre lo que decime, * en este caso

# COMENTARIOS Y TEXT
comentariosLabel = Label(miFrame, text="Comentarios: ", bg="white")
comentariosLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)

textoComentarios = Text(miFrame, width=15, height=5)
textoComentarios.grid(row=4, column=1, padx=0, pady=10)

# añadir scroll al text: yview para que sea vertical
scrollBarComentarios = Scrollbar(miFrame, command=textoComentarios.yview)
scrollBarComentarios.grid(row=4, column=2, padx=0, pady=10, sticky="nsew") # sticky permitimos que se adapte al tamaño del widget al que pertenece

textoComentarios.config(yscrollcommand=scrollBarComentarios.set) # añadimos el scroll correctamente al textoComentarios y se comporta bien

textoComentarios.config(cursor="heart", bg="yellow") # hacemos que el cursor tome forma de corazon al estar encima de textoComentarios



# AÑADIR BOTON: command= añadir funcionalidad codigoBoton es una funcion por ejemplo

# que al pulsar en enviar, mande mi nombre al entryNombre:
def codigoBoton():

	miNombre.set("Nell")

btn = Button(raiz, width=5, height=2, text="Enviar", command=codigoBoton) # raiz por ejemplo, NO miFrame, para probar.


btn.pack()



# prueba
labelCualquiera = Label(miFrame, text="Esto deberia estar en 6,6")
labelCualquiera.grid(row=6, column=6, padx=10, pady=10) # pady o padx es el espacio que hay entre el objeto y el padre, o siguiente elemento!


raiz.mainloop()