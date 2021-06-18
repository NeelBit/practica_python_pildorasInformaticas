def divide():

	num1 = float(input("Introduce primer numero: "))
	num2 = float(input("Introduce segundo numero: "))

	resultado = num1 / num2
	print("El resultado es: ", resultado)

"""
try:
	divide()
except ZeroDivisionError:
	print("Trataste de dividir por cero!")

except ValueError:
	print("No introduciste un numero!")
"""

while True:

	try:
		divide()
		break

	# except se puede usar de manera general sin aclarar el nombre de la excepcion. pero no es recomendado!
	except ZeroDivisionError:
		print("Trataste de dividir por cero!")

	except ValueError:
		print("No introduciste un numero!")

	# finally siempre se ejecuta!
	finally:
		print("este es un texto en finally")

print("Continuacion del programa!")