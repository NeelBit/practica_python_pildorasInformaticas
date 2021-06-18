from io import open

"""
# primer parametro es el nombre, el segundo es w de write, escribir, tambien puede ser lectura o append
archivo_texto = open("nombre_archivo.txt", "w") # modo creacion y escritura de archivo
# si ejecutas hasta aca, crea el archivo de texto

frase = "Esta es la primer linea de texto del archivo archivo_texto \nEsta es la segunda linea y hoy es 19/05/2020"

archivo_texto.write(frase)

archivo_texto.close() # cerramos el archivo en memoria
"""

archivo_texto = open("nombre_archivo.txt", "r") # modo lectura de archivo r .  a de append . a+ lectura y append

archivoTexto2 = open("text.txt", "r")

lecturaYappendTexto1 = open("nombre_archivo.txt", "a")
# creamos una variable texto, para en ella guardar el contenido de archivo_texto

# SI AL USAR READ() DESPUES UTILIZAMOS READLINES() BORRA TODO EL CONTENIDO!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#texto = archivo_texto.read()

texto2todoJunto = archivoTexto2.read()

# podemos usar readlines() para almacenar linea a linea en una lista, asi es mas facil realizar acciones de busquedas por ejemplo

# a archivo_texto añadimos una linea mas:
lecturaYappendTexto1.write("\nEste texto esta añadido")

lecturaYappendTexto1.close()

print(lecturaYappendTexto1)

textoLineas = archivo_texto.readlines()

texto2 = archivoTexto2.readlines()

archivo_texto.close() 	# importante cerrar!

archivoTexto2.close()

#print(texto)
print(texto2todoJunto)

print()

print(textoLineas)

print(texto2)

# PARA IMPRIMER SOLAMENTE UNA LINEA, POR LO TANTO POR EJEMPLO HACEMOS: print(texto2[0]) para que imprima la primera linea, luego de que hicimos una lista con readlines()