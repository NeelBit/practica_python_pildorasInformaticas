import math

def raizCuadrada(listaNumeros):

	"""
	Sacar la raiz cuadrada de la lista de numero que se recibe por parametro.
	La funcion devuelve otra lista con los resultados.

	>>> lista = []
	>>> for i in [4, 9, 16]:
	... 	lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]
	
	
	>>> lista = []
	>>> for i in [4, -9, 16]:
	... 	lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
		...
	ValueError: math domain error

	"""

	# dejamos la primera linea y la última, con ... entre medio con sangria. para indicar que esperamos ese tipo de excepcion

	# utilizamos ... para indicar que es una expresion anidada que le sigue a la anterior.

	return [math.sqrt(n) for n in listaNumeros]

lista1Numeros = [29, 30, 445, 889, 15]

print(raizCuadrada(lista1Numeros))

print()

import doctest

doctest.testmod()