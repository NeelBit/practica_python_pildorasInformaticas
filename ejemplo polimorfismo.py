class Coche():

	def desplazamiento(self):

		print("Me desplazo utilizando 4 ruedas")

class Moto():

	def desplazamiento(self):

		print("Me desplazo utilizando 2 ruedas")

class Camion():

	def desplazamiento(self):

		print("Me dezplazo utilizando 6 ruedas")

""" precindimos de todas estas lineas y aplicamos polimorfismo
miVehiculo = Moto()

miVehiculo.desplazamiento()

miVehiculo2 = Coche()

miVehiculo2.desplazamiento()

miVehiculo3 = Camion()

miVehiculo3.desplazamiento()
"""

def desplazamientoVehiculo(vehiculo): 	# recibe objeto por parametro y ese objeto llama a desplazamiento(), pero no sabemos de que tipo es

	vehiculo.desplazamiento()

miVehiculo = Camion()

desplazamientoVehiculo(miVehiculo)

miMoto1 = Moto()

desplazamientoVehiculo(miMoto1)

miCoche1 = Coche()

desplazamientoVehiculo(miCoche1)

# UN MISMO METODO QUE SABE COMO COMPORTARSE DEPENDIENDO DE QUE TIPO DE OBJETO RECIBE
