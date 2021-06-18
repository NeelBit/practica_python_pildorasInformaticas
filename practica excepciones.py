def suma(num1, num2):
	return num1 + num2

def resta(num1, num2):
	return num1 - num2

def multiplica(num1, num2):
	return num1 * num2


def divide(num1, num2):
	
	try:
# controlar excepcion de division por cero:
		return num1 / num2

	except ZeroDivisionError:

		print("No puedes dividir por cero!")
		return "Operacion erronea"


# BUCLE INFINITO PARA SOLUCIONAR PROBLEMAS! 
while True:

	try:
	# controlar excepcion ValueError , si se introduce letras en ves de numero
		op1 = int(input("Introduce el primer numero: "))
		op2 = int(input("Introduce el segundo numero: "))

		break # o sino no saldría nunca del bucle infinito!!!! , al leer el break sale del bucle while sin pasar por el except

	except ValueError: 
		
		print("Introduce numero valido!")
	


operacion = input("Introduce la operacion a realizar (suma, resta, multiplicacion, division) : ")

if operacion == "suma":
	print(suma(op1, op2))

elif operacion == "resta":
	print(resta(op1, op2))

elif operacion == "multiplicacion":
	print(multiplica(op1, op2))

elif operacion == "division":
	print(divide(op1, op2))

else:
	print("Operacion no válida!")

print("Operacion ejecutada, esta es la continuacion de la ejecución del programa!")