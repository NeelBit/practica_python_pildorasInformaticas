import pickle

class Persona():

	def __init__(self, nombre, genero, edad):

		self.nombre = nombre
		self.genero = genero
		self.edad = edad

		print("Se ha creado la persona", self.nombre)


	def __str__(self):

		return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas():

	personas = []

	# constructor:	
	def __init__(self):

		# creamos fichero externo que almacenara la informacion de manera permanente. ab+ append (agregar) binario con lectura
		listaDePersonas = open("fichero_externo", "ab+")

		# desplazar el cursor al principio
		listaDePersonas.seek(0)

		# metemos en un try esto, por si es la primero ves que la hacemos y no hay contenido en la lista, entonces nos dará error
		try: 
			# cargar el contenido externo a nuestro lista
			self.personas = pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas))) 

		except:

			print("El fichero esta vacio!")

		finally:

			listaDePersonas.close()
			del(listaDePersonas)

	# metodo para almacenar personas en la lista:
	def agregarPersonas(self, p):
		# añade p a la lista personas:
		self.personas.append(p)

		# llamamos al metodo para agregar personas a fichero_externo:
		self.guardarPersonaEnFicheroExterno()

	# metodo para leer las personas almacenadas en la lista: ver informacion almacenada en lista
	def mostrarPersonas(self):

		for i in self.personas:

			print(i)

	# metodo para añadir las personas al archivo externo:
	def guardarPersonaEnFicheroExterno(self):
		# fichero externo con permisos para write de binario
		listaDePersonas = open("fichero_externo", "wb")

		# volcado de informacion de personas[] a la listaDePersonas --> fichero externo
		pickle.dump(self.personas, listaDePersonas)

		listaDePersonas.close()
		del(listaDePersonas)



# objeto de la listaPersonas para poder utilizar los metodos:
miListaPersonas = ListaPersonas()

"""
p1 = Persona("Juan", "Masculino", 30)
p5 = Persona("fulano", "Masculino", 50)
p10 = Persona("Mengana", "Femenino", 40)

# añadimos la personas creada a la lista:
miListaPersonas.agregarPersonas(p1)
miListaPersonas.agregarPersonas(p5)
miListaPersonas.agregarPersonas(p10)
"""

persona1 = Persona("nombre de persona", "Masculino", 50)
miListaPersonas.agregarPersonas(persona1)

miListaPersonas.mostrarPersonas()

# EL ARCHIVO TIENE GUARDADO PERMANENTE ENTONCES CADA VES QUE LE EJECUTO GUARDA LAS MISMAS PERSONAS, y lee todas las agregadas anteriormente
