# clase padre
class Vehiculos():

	# constructor: recibe 2 parametros
	def __init__(self, marca, modelo):

		self.marca = marca
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False

	# definimos comportamientos, metodos
	def arrancar(self):

		self.enMarcha = True

	def acelerar(self):

		self.acelera = True

	def frenar(self):

		self.frena = True

	def estadoVehiculo(self):

		print(f"La marca es {self.marca}, el modelo: {self.modelo}\nSe encuentra en marcha: {self.enMarcha}, se encuentra acelerando: {self.acelera}, se encuentra frenando: {self.frena} ")


# la herencia!
class Furgoneta(Vehiculos):

	#cargado = False

	def carga(self, cargar):

		self.cargado = cargar

		if (self.cargado):

			return "La furgoneta esta cargada!"

		else:

			return "No esta cargada la furgoneta!"




class Moto(Vehiculos):

	caballito = "-"

	def haceCaballito(self):

		self.caballito = "Voy haciendo caballito!"

	#sobre-escribir metodos:
	def estadoVehiculo(self):

		print(f"La marca es {self.marca}, el modelo: {self.modelo}\nSe encuentra en marcha: {self.enMarcha}, se encuentra acelerando: {self.acelera}, se encuentra frenando: {self.frena}. y hace caballito: {self.caballito}")


class VElectricos(Vehiculos):

	def __init__(self, marca, modelo):

		# llamar al constructor del padre:
		super().__init__(marca, modelo)

		self.autonomia = 100 	# por defecto la autonomia de los objetos instanciados van a tener 100 kmtros.

	# metodo que cuando lo llamamos esta cargando
	def cargarEnergia(self):

		self.cargando = True


# instancia de moto:
miMoto = Moto("Brava", "Nevada") # esta heredando también el constructor asi que debemos pasarle la marca y modelo

miMoto.estadoVehiculo()

miMoto.acelerar()

miMoto.arrancar()

miMoto.haceCaballito()

miMoto.estadoVehiculo()


# intancia de furgoneta:
miFurgoneta = Furgoneta("Renault", "kangoo")

miFurgoneta.arrancar()

miFurgoneta.estadoVehiculo()

print(miFurgoneta.carga(True))


# HERENCIA MULTIPLE
class BicicletaElectrica(VElectricos, Vehiculos):

	pass


print()

# EN LA HERENCIA MÚLTIPLE SE DA PREFERENCIA A LA PRIMER CLASE QUE HEREDAMOS, EN ESTE CASO VElectricos
miBiciElectrica = BicicletaElectrica("Mountain", "bike")

miBiciElectrica.arrancar()

miBiciElectrica.estadoVehiculo()

print("Tiene autonomia: ", miBiciElectrica.autonomia)

