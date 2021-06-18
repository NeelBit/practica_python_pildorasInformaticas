from tkinter import *

root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu, width= 400, height=300)

archivoMenu = Menu(barraMenu, tearoff=0) # tearoff son los guiones dentro del menú, por defecto trae, hay que desactivarlo

ayudaMenu = Menu(barraMenu)

editMenu = Menu(barraMenu)

herramientasMenu = Menu(barraMenu, tearoff=0)

# añadir: barra principal

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
barraMenu.add_cascade(label="Edición", menu=editMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)

# sub Menus:

# subMenu archivoMenu: ESTA ES LA FORMA CORRECTA
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Open")
archivoMenu.add_command(label="Guardar")
# añadir separador!
archivoMenu.add_separator()
archivoMenu.add_command(label="Exit")


# subMenu  de menus editmenu:
copiarSubEditMenu = Menu(editMenu)
cortarSubEditMenu = Menu(editMenu)
pegarSubEditMenu = Menu(editMenu)

editMenu.add_cascade(label="Copiar", menu=copiarSubEditMenu)
editMenu.add_cascade(label="Cortar", menu=cortarSubEditMenu)
editMenu.add_cascade(label="Pegar", menu=pegarSubEditMenu)

# subMenu herramientasMenu:
herramientasMenu.add_command(label="Personalizar")
herramientasMenu.add_command(label="Configuraciones")



root.mainloop()