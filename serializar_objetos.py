import pickle

class Vehiculo():

	def __init__(self, marca, modelo):

		self.marca = marca
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):

		self.enMarcha = True

	def acelerar(self):

		self.acelera = True


	def frena(self):

		self.frena = True


	def estado(self):

		print(f"Marca: {self.marca}, Modelo: {self.modelo}, acelerando: {self.acelera}, en marcha: {self.enMarcha}, frena: {self.frena}")


coche1 = Vehiculo("Honda", "civic")
coche2 = Vehiculo("Mazda", "MX")
coche3 = Vehiculo("toyota", "hilux")

coches = [coche1, coche2, coche3]

for i in coches:

	i.estado()

fichero = open("listaCochesBinario", "wb")

# hacemos el volvado de la informacion: 1º el contenido, 2º fichero donde lo vamos a volvar.
pickle.dump(coches, fichero)

fichero.close()

# LA SENTENCIA del ELIMINA OBJETOS, CLASES, O ELEMENTOS DE LISTAS:

del(fichero)

print() 

# podemos cargar la informacion desde aca:

ficheroApertura = open("listaCochesBinario", "rb")

listaCochesCargado = pickle.load(ficheroApertura)

ficheroApertura.close()

for i in listaCochesCargado:

	print(i.estado())

