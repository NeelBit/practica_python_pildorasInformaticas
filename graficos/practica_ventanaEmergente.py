from tkinter import *
# libreria para ventana emergente:
from tkinter import messagebox

root = Tk()

# funciones que sera la encargada de construir la ventana emergente:
def infoAdicional(): # acerca de

	messagebox.showinfo("Este es el título!", "Aqui va el contenido de la ventana emergente!")

def avisoLicencia(): # licencia

	messagebox.showwarning("Licencia", "Software sin licencia!")

def salirAplicacion():
	# si no: askquestion devuelve yes o no
	#valor = messagebox.askquestion("Salir", "Seguro que desea salir?") # el metodo askquestion devuelve un valor "yes" o "no"

	# aceptar cancelar: askokcancel devuelve True o False
	valor = messagebox.askokcancel("Salir", "Seguro que desea salir?")

	"""
	if (valor == "yes"):

		# salir de aplicacion
		root.destroy()
	"""

	if (valor == True):

		root.destroy()

def cerrarDocumento():

	# devuelve True o False
	valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado!")

	# false para que no reintente por ejmplo y salga.
	if (valor == False):

		root.destroy()


root.title("Menu y ventana emergente")

barraMenu = Menu(root)

root.config(menu=barraMenu, width=500, height=300)

# Menu de archivo:
archivoMenu = Menu(barraMenu, tearoff=0)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Open")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Exit", command=salirAplicacion)

# Menu de edicion:
edicionMenu = Menu(barraMenu, tearoff=0)

barraMenu.add_cascade(label="Edición", menu=edicionMenu)

edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Pegar")

# Menu de ayuda:
ayudaMenu = Menu(barraMenu, tearoff=0)

barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

ayudaMenu.add_command(label="Licencia", command=avisoLicencia)
ayudaMenu.add_command(label="Acerca de", command=infoAdicional)


root.mainloop()