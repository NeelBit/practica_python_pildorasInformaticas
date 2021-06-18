from tkinter import *
# Importamos modulo
from tkinter import filedialog


raiz = Tk()

raiz.title("Ventana con selector de archivos externos")
raiz.config(width=400, height=350)

# funcion para que se nos abra una ventana para seleccionar archivo al clickear un boton
def abreFichero():

	fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de word", "*.docx"), ("Fichero de imagen", "*.jpg"), ("Todos", "*"))) # parametro initialdir para modificar donde abre por defecto .Parametro filetypes para modificar que tipos de archivos ver recibe tupla

	print(fichero) # imprime la ruta del fichero seleccionado!


button = Button(raiz, text="Abrir archivo...", command=abreFichero)
button.pack()

raiz.mainloop()