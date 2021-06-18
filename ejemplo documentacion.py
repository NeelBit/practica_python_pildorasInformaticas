
class Areas:

	""" Clase para calcular el area de diferentes figuras geometricas """

	def areaCuadrado(lado):

		""" Calcula el area de un cuadrado, elevando al cuadrado
		el lado pasado por parametro """

		return "El area del cuadrado es: " + str(lado*lado)

	def areaTriangulo(base, altura):

		""" Calcula el area de un triangulo, multiplicando los parametros
		base por la altura y al resultado dividiendolo por 2"""

		return "El area del triangulo es: " + str((base*altura)/2)


print(Areas.areaCuadrado(6))

#print(areaCuadrado.__doc__)

# TAMBIEN PODEMOS UTILIZAR LA FUNCION help()
#help(Areas.areaCuadrado)

#help(Areas.areaTriangulo)

# ayuda de toda la clase:
help(Areas)

print(Areas.areaTriangulo(4, 5))