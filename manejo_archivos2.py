from io import open

archivoDeTexto = open("text.txt", "r+") # lectura y escritura

listaTexto = archivoDeTexto.readlines()

print(archivoDeTexto.readlines())

print(archivoDeTexto.read())

#print(archivoDeTexto.read())

# por defecto al puntero lo pone al inicio.
# si el puntero lo ponemos al final, no leera nada del archivo. 
# o si hacemos dos llamadas, uno arranca desde el inicio, lo deja al puntero al final, y la segunda llamada no leera nada.
# para cambiar la ubicacion del puntero utilizamos zeek(ubicacionDelCaracter)

archivoDeTexto.seek(10)

print()


print(archivoDeTexto.read())

print()

# por parametro a read(intHastaDondeLeer) le podemos pasar la ubicacion HASTA DONDE debe leer

archivoDeTexto.seek(0)

print(archivoDeTexto.read(4)) # hola

print()

# para que nos lea DESDE la mitad del texto: 

archivoDeTexto.seek(len(archivoDeTexto.read()) / 2) 	# coloca puntero a la mitad

print(archivoDeTexto.read())

print()

print(listaTexto)

listaTexto[1] = "Esta linea ha sido incluida desde writelines \n"

archivoDeTexto.seek(0)

archivoDeTexto.writelines(listaTexto)

archivoDeTexto.close()