# funcion tradicional para generar numeros pares.

""" MI FORMA DE HACERLO:
def generaPares(limite):

	listaPares = []

	for i in range(limite+1):

		if i % 2 == 0:
			listaPares.append(i)

	return listaPares

limit = int(input("Ingresa limite de numeros pares: "))

print(generaPares(limit))
"""

# forma de hacerlo del curso: aunque imprime esa cantidad de numeros pares, no como limite a ese numero como yo lo planteé
"""
def generaPares(limite):

	num = 1
	miLista = []

	while num <= limite:
		miLista.append(num * 2)
		num += 1

	return miLista

print(generaPares(10))
"""

# GENERADOR            YIELD

def generaPares(limite):

	num = 1

	while num <= limite:

		yield num * 2

		num += 1

# guardar el objeto iterable que devuelve la funcion:
objetoDevuelvePar = generaPares(10)
"""
for i in objetoDevuelvePar:

	print(i)
"""

# metodo next : obtener elemento a elemento, a partir del objeto iterable
print(next(objetoDevuelvePar))
print("Salto de linea!")
print(next(objetoDevuelvePar))