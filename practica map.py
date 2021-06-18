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

def calculoComision(empleado):

	if empleado.salario <= 3000: 	# para que aplique solo a los inferiores de ese salario

		empleado.salario = empleado.salario * 1.03 # aplica 3% mas de salario

	return empleado


listaEmpleadoConComision = map(calculoComision, listaEmpleados)

for i in listaEmpleadoConComision:

	print(i)