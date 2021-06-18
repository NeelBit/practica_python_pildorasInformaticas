import pickle

class Persona():

	def __init__(self, nombre, edad):

		self.nombre = nombre
		self.edad = edad

	def dameInfo(self):

		return f"El nombre es: {self.nombre} y la edad es: {self.edad}"

persona1 = Persona("cosme", 25)

persona2 = Persona("fulanito", 23)

listaDePersonas = [persona1, persona2]

for i in listaDePersonas:

	print(i.dameInfo())

"""
archivoPersonas = open("lista2personas", "wb")

pickle.dump(listaDePersonas, archivoPersonas)

archivoPersonas.close()
"""

# leer el archivo de arriba:

"""
archivoPersonas = open("lista2personas", "rb")

listaPersona = pickle.load(archivoPersonas)

for i in listaPersona:

	print(i.dameInfo())

"""