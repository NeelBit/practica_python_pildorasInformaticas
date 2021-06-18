from tkinter import *
from tkinter import messagebox
import sqlite3


# --------------------- FUNCIONES ----------------------#

def conexionBBDD():

	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()

	# excepcion por si la base de datos ya está creada:
	try:

		miCursor.execute('''

			CREATE TABLE DATOS_USUARIOS (

			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(20),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(150)

			)
		''')

		messagebox.showinfo("Base de datos creada", "Has creado la base de datos correctamente!")
	
	except:

		messagebox.showwarning("Error al crear la BBDD", "La base de datos ya existe!")

def salirAplicacion():

	valor = messagebox.askquestion("Salir", "¿Seguro que desea salir de la aplicacion?")

	if (valor == "yes"):

		root.destroy()

def limpiarCampos():

	miId.set("")
	miNombre.set("")
	miPass.set("")
	miApellido.set("")
	miDireccion.set("")
	textoComentarios.delete(1.0, END)

def crear():


	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()
	"""
	miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, '" + miNombre.get() + 
														"', '" + miPass.get() + 
														"', '" + miApellido.get() + 
														"', '" + miDireccion.get() + 
														"', '" + textoComentarios.get("1.0", END) + "' 
														) 
					" )
	"""
	# parametrizado:
	datos = miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentarios.get("1.0", END)

	miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, ?, ?, ?, ?, ?)", (datos))


	miConexion.commit()

	messagebox.showinfo("Registro insertado", "El registro se inserto correctamente")


	
	

def leer():

	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" + miId.get())

	# devuelve array con los datos del usuario con el id que le pasamos
	elUsuario = miCursor.fetchall()

	for user in elUsuario:

		miId.set(user[0])
		miNombre.set(user[1])
		miPass.set(user[2])
		miApellido.set(user[3])
		miDireccion.set(user[4])
		textoComentarios.insert(1.0, user[5])

	miConexion.commit()

def actualizar():

	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()

	"""
	miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE='" + miNombre.get() + 
		"', PASSWORD='" + miPass.get() +
		"', APELLIDO='" + miApellido.get() + 
		"', DIRECCION='" + miDireccion.get() + 
		"', COMENTARIOS='" + textoComentarios.get("1.0", END) + 
		"' WHERE ID=" + miId.get() )
	"""

	# parametrizado:
	datos = miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), textoComentarios.get("1.0", END)

	miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? " + "WHERE ID=" + miId.get(), (datos))


	miConexion.commit()

	messagebox.showinfo("Registro actualizado", "El registro se actualizó correctamente")

def eliminar():

	miConexion = sqlite3.connect("Usuarios")
	miCursor = miConexion.cursor()

	miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID=" + miId.get())

	miConexion.commit()

	messagebox.showwarning("Registro borrado", "El registro se borro correctamente")

def infoAcercaDe():

	messagebox.showinfo("acerca de", "Programa hecho por nel, sin derechos de autor")


root = Tk()
root.title("CRUD")


# --------------------- BARRA DE MENU ----------------------#

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=500)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Create/Crear", command=crear)
crudMenu.add_command(label="Read/Leer", command=leer)
crudMenu.add_command(label="Update/Actualizar", command=actualizar)
crudMenu.add_command(label="Delete/Borrar", command=eliminar)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de", command=infoAcercaDe)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


# --------------------- FRAME PRINCIPAL ----------------------#
miFrame = Frame(root)
miFrame.pack()

# variables para los Entry:
miId = StringVar()
miNombre = StringVar()
miPass = StringVar()
miApellido = StringVar()
miDireccion = StringVar()



cuadroID = Entry(miFrame, justify="center", textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, justify="center", fg="red", textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroPass = Entry(miFrame, justify="center", show="*", textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)

cuadroApellido = Entry(miFrame, justify="center", textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame, justify="center", textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentarios = Text(miFrame, width=15, height=8)
textoComentarios.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentarios.yview)
scrollVert.grid(row=5, column=2, pady=10, sticky="nsew")
textoComentarios.config(yscrollcommand=scrollVert.set)


idLabel = Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, padx=10, pady=10, sticky="w")

passLabel = Label(miFrame, text="Contraseña:")
passLabel.grid(row=2, column=0, padx=10, pady=10, sticky="w")

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, padx=10, pady=10, sticky="w")

direccionLabel = Label(miFrame, text="Direccion:")
direccionLabel.grid(row=4, column=0, padx=10, pady=10, sticky="w")

textoComentariosLabel = Label(miFrame, text="Comentarios:")
textoComentariosLabel.grid(row=5, column=0, padx=10, pady=10, sticky="w")

# --------------------- FRAME INFERIOR ----------------------#
miFrameInferior = Frame(root)
miFrameInferior.pack()

btnCreate = Button(miFrameInferior, text="Create", bg="white", justify="center", command=crear)
btnCreate.grid(row=0, column=0, padx=10)

btnRead = Button(miFrameInferior, text="Read", bg="white", justify="center", command=leer)
btnRead.grid(row=0, column=1, padx=10)

btnUpdate = Button(miFrameInferior, text="Update", bg="white", justify="center", command=actualizar)
btnUpdate.grid(row=0, column=2, padx=10)

btnDelete = Button(miFrameInferior, text="Delete", bg="white", justify="center", command=eliminar)
btnDelete.grid(row=0, column=3, padx=10)






root.mainloop()