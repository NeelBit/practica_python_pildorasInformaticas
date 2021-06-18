class Persona():

	def __init__(self, nombre, edad, lugarResidencia):

		self.nombre = nombre
		self.edad = edad
		self.lugarResidencia = lugarResidencia

	def descripcion(self):

		print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nLugar de residencia: {self.lugarResidencia}")


class Empleado(Persona):

	def __init__(self, salario, antiguedad, nombre, edad, residencia):

		super().__init__(nombre, edad, residencia)

		self.salario = salario
		self.antiguedad = antiguedad


	def descripcion(self):

		super().descripcion()

		print(f"Salario: {self.salario}\nAntiguedad: {self.antiguedad}")


antonio = Persona("Antonio", 30, "Valencia")

antonio.descripcion()

print()

empleadoUNO = Empleado(8000, 10, "Empleado uno fulano", 40, "Argentina")

empleadoUNO.descripcion()

print()

# SABER SI UN OBJETO ES DE CIERTO TIPO:
x = isinstance(empleadoUNO, Empleado)
print(x)