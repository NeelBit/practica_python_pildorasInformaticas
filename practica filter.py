# funcion que devuelva los pares:
"""
def numeroPar(num):

	if num % 2 == 0:

		return True

	else:
		return False

"""

# simplificamos todo lo de arriba en una sola linea:
"""
numeros = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda num: num%2==0, numeros)))
"""

# ejemplo practico de uso de filter, con objetos:

class Empleado:

	def __init__(self, nombre, cargo, salario):

		self.nombre = nombre
		self.cargo = cargo
		self.salario = salario


	def __str__(self):

		return "{} tiene el cargo de {} y tiene un salario de {}$".format(self.nombre, self.cargo, self.salario)


listaEmpleados = [

	Empleado("jose", "Administrador", 1500),
	Empleado("juan", "Director", 4000),
	Empleado("carlos", "RRHH", 3000),
	Empleado("ana", "RRPP", 1000),
	Empleado("julio", "Gerente", 5000)

]

salariosAltos = filter(lambda e: e.salario > 2500, listaEmpleados)

for l in salariosAltos:

	print(l)

