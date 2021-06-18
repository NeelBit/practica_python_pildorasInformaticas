from tkinter import *

# el nombre raiz se suele usar por convencion y es el primer elemento, es la ventana misma 
raiz = Tk()

# MODIFICAR PROPIEDADES DE LA VENTANA:

# titulo
raiz.title("Ventana de prueba")

# redimensionar: recibe 2 parametros booleanos ancho y alto
#raiz.resizable(True, False)

# añadir icono a la ventana, tener archivo .ico, preferentemente en el mismo directorio
raiz.iconbitmap("icono.ico")

# tamaño por defecto de la ventana, ancho(width) y alto(height) "anchoxalto" LA RAIZ SIEMPRE SE ADAPTA AL TAMAÑO DEL CONTENEDOR INTERNO (frame)
#raiz.geometry("400x250")

# varias cosas, y cambiar color de fondo: bg= (bg: background)
raiz.config(bg="black")

# CREAMOS FRAME:

miFrame = Frame()

# empaquetamos frame, osea, le metemos dentro de la raiz (ventana)
miFrame.pack()
#miFrame.pack(side="right") # en este caso por ejemplo siempre va a estar pegado el frame a la derecha del marco
#miFrame.pack(side="bottom") # para que este pegado a la parte inferior
#miFrame.pack(side="top", anchor="e") # top para que este arriba, y anchor="e" e de east (este) para que este al borde superior al este

miFrame.pack(fill="x") # x rellena horizontalmente
#miFrame.pack(fill="y", expand="True") # rellena verticalmente
#miFrame.pack(fill="both", expand="True") # para expandir el frame cuando se redireccione el marco en general!


# cambiar color de fondo de frame:
miFrame.config(bg="blue")

# dar tamaño al frame:
miFrame.config(width="400", height="250")

# cambiar configuraciones del borde:
#cambiar tamaño del borde:
miFrame.config(bd="40")

miFrame.config(relief="sunken")

# cambiar el tipo de cursor/flecha en el frame:
#miFrame.config(cursor="hand2") # forma de mano
miFrame.config(cursor="pirate") # forma de calavera al poner el cursor en el frame

# TODO ESTO ES APLICABLE A LA RAIZ, POR EJEMPLO podemos cambiar borde, fondo, cursor, etc a raiz
raiz.config(cursor="hand2")
raiz.config(bd="10")
raiz.config(relief="groove")


# metodo mainloop() siempre debe estar al final!!
raiz.mainloop()