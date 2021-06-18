class Auto():

	# metodo constructor:
	def __init__(self, ruedas, largo):

	#propiedades: variables

	# 	ENCAPSULAMIENTO!!!!! poniendo dos guiones bajos __ para que no se pueda modificar desde fuera de la clase
		self.__largoAuto = largo
		self.__anchoAuto = 150
		self.__ruedas = ruedas
		self.__enMarcha = False

	#comportamientos: metodos (los metodos pertenecen a la clase, y las funciones no) | self es lo mismo que el this, osea referencia al objeto mismo como parametro. python obliga a poner como primer parametro
	def arrancar(self, arrancamos): 	# le pasamos por parametro si queremos arrancar o no
		self.__enMarcha = arrancamos # le da valor a ese variable __enMarcha

		#comprombamos en marcha y hacemos chequeo:
		if self.__enMarcha:
			# almacenamos en chequeo lo que devuelva chequeoInterno()
			chequeo = self.__chequeoInterno() # llamado a otro metodo, y almacenamos en variablo local

		if self.__enMarcha and chequeo:
			return "El coche esta en marcha"

		elif self.__enMarcha and chequeo == False:
			return "Algo ha ido mal en el chequeo!, no se puede arrancar"

		else:
			return "NO esta en marcha el coche"

		
	# metodo para ver estado:
	def verEstado(self):
		print("El coche tiene: ", self.__anchoAuto, " de ancho y ", self.__largoAuto, " de largo. Además tiene ", self.__ruedas, " ruedas")


	# añadir metodo para hacer chequeo antes de arrancar: necesitamos llamar a este metodo antes de arrancar
	# si un coche no esta encendido no debe ser capaz de hacer un chequeo entonces es necesario encapsular el metodo!
	def __chequeoInterno(self):

		print("Realizando chequeo interno!")

		self.gasolina = "ok" #crea variable gasolina
		self.aceite = "ok"
		self.puertas = "cerradas"

		if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
			return True
		else:
			return False




# creamos instancia de clase Auto:
miAuto1 = Auto(3, 500) # le decimos que auto2 tiene 3 ruedas, como pasamos por parametro, y 500 de largo

miAuto1.verEstado()

print(miAuto1.arrancar(True))

miAuto1.verEstado() 	# metodo verEstado ya hace print, osea que no hace falta

print("------------ creamos segundo objeto ------------")

miAuto2 = Auto(5, 400) # le decimos que auto2 tiene 5 ruedas, como pasamos por parametro, y 400 de largo

print(miAuto2.arrancar(False))

# auto2.__ruedas(2) NO NOS PERMITE MODIFICAR POR LA ENCAPSULACION __

miAuto2.verEstado() 	# metodo verEstado ya hace print, osea que no hace falta

#print("varificar chequeo interno. ESTO NO TIENE SENTIDO! desde fuera, por eso es necesario encapsular el metodo")
#print(miAuto2.__chequeoInterno())