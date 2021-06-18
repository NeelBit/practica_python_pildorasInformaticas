""" # WHILE COMUN
num = 1

while num <= 10:
	#DOS FORMAS DE IMPRIMIR:
	print(f"El valor de num es: {num}")
	print("Valor: " + str(num))

	# INCREMENTO EN PYTHON - python NO cuenta con operador incremento int++
	num += 1

"""

""" WHILE QUE PIDE LA EDAD
edad = int(input("Introduce tu edad: "))

while edad <=0 or edad > 110:
	print("Has introducido una edad incorrecta!")
	edad = int(input("Introduce tu edad nuevamente! : "))

print(f"Tienes {edad} años")


""" # raiz cuadrada de un numero. bucle NO infinito: sentencia break

import math

print("Programa de calculo de raiz cuadrada: ")

numero = int(input("Introduce el numero: "))

intentos = 0

while numero <= 0:
	print("no se puede hallar la raiz cuadrada de un numero igual o menor a cero!")

	intentos += 1

	numero = int(input("Introduce nuevamente el numero: "))

	if intentos == 3:
		print("Intentaste 3 veces mas con numeros invalidos")
		break # sale del while!

solucion = math.sqrt(numero)
print(f"La raiz cuadrada de {numero} es {solucion}")