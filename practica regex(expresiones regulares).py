import re

cadena = "Vamos a aprender expresiones regulares en python. python posee muchas expresiones"

# Buscar una palabra en una cadena:
print(re.search("aprender", cadena))
print(re.search("vamos", cadena)) # devuelve None si no se encuentra la cadena

textoBuscar = input("introduce texto a buscar: ")

"""
if re.search(textoBuscar, cadena): # is not None: tambien se puede poner

	print(f"Si se encuentra la palabra \"{textoBuscar}\", en \"{cadena}\"")

else:

	print(f"No se encuentra la palabra \"{textoBuscar}\", en \"{cadena}\"")

"""

print()

textoEncontrado = re.search(textoBuscar, cadena)

# imprimir donde se encuentra la palabra
print(textoEncontrado.start())

# caracter donde termina la palabra encontrada:
print(textoEncontrado.end())

# devuelve tupla desde donde hasta donde va la palabra
print(textoEncontrado.span())

# imprimir todas las veces que se repite una palabra: devuelve una lista con las palabras las veces encontradas.
print(re.findall(textoBuscar, cadena))

# para que nos diga el numero de veces que se encuentra una palabra, solo agregamos len()
print(len(re.findall(textoBuscar, cadena)))