def funcion_decoradora(funcion_parametro):

	def funcionInterior(*args, **kwargs):						# num1, num2 tambien podemos poner de parametros, 
								# keyword arguments

		# acciones adicionales que decoran

		print("Vamos a realizar un calculo: ")

		funcion_parametro(*args, **kwargs) 		# *args indica que puede recibir un numero indeterminado de parametros

		# acciones adicionales que decoran

		print("Calculo realizado!")

	return funcionInterior





# funcion normal: si por ejemplo tenemos 20 funciones como las de abajo sencillas, pero en algun momentos queres añadir una funcionalidad extra a todas
# por ej: añadir un print a las dos funciones antes y despues del calculO:

@funcion_decoradora # asi le indicamos que vamos a decorar la funcion suma
def suma(num1, num2, num3):

	print(num1 + num2 + num3)


@funcion_decoradora
def resta(num1, num2):

	print(num1 - num2)


# nueva funcion, para probar kwargs

@funcion_decoradora
def potencia(uno, dos, base, exponente):

	print(f"probando: {uno} y {dos}")

	print(base**exponente)




suma(5, 5, 5)

print()

resta(10, 5)

print()

print("potencia: ")

# AL PASAR PARAMETROS DE ESTA FORMA ENTOCES PRIMERO VAN LOS ARGUMENTOS Y LUEGO VAN LOS KEYWORD ARGUMENTS

potencia(1, 2, base=2, exponente=5)

"""
funcion_decoradora(suma)
funcion_decoradora(resta)
"""