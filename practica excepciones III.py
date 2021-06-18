""" 
def evaluaEdad(edad):

# crear excepcion propia: raise
	if edad < 0 or edad >= 100:

		raise TypeError("Edad no válida!")



	if edad < 20:
		return "eres muy joven!"

	elif edad < 40:
		return "eres joven"

	elif edad < 65:
		return "eres maduro"

	elif edad < 110:
		return "cuidate..."

#print(evaluaEdad(80))



while True:
	try:

		edad = int(input("Introduce edad: "))
		print(evaluaEdad(edad))

		break

	except TypeError:
		print("Introduciste una edad no valida, vuelve a intentarlo! ")

print("continuacion del programa!")

"""

# crear excepcion y tratarla para funcion que intente sacar raiz cuadrada, y se tope con numero negativo:
import math
def calculaRaiz(num1):

	if num1 < 0:

		# Si recibe un numero menor a cero, lanza una excepcion
		raise ValueError("El numero no puede ser negativo")


	else:

		resultado = math.sqrt(num1)
		return resultado



#print(calculaRaiz(numUsuario))

#solucion 1:
"""
try:
	print(calculaRaiz(numUsuario))

except ValueError:

	print("Debes introducir un numero positivo!")
"""

#solucion 2:

while True:
	try:
		numUsuario = int(input("Introduce en numero para ver su raíz cuadrada: "))
		print(calculaRaiz(numUsuario))
		break

	# se puede dar un alias al error!
	except ValueError as ErrorDeNumeroNegativo:
		#print("Debes introducir un numero positivo para poder saber si raiz cuadrada!")
		print(ErrorDeNumeroNegativo) # imprime concretamente lo que le decimos en el raise


print("Continuacion del programa!")