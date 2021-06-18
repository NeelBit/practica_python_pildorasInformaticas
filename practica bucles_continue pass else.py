# INSTRUCCION CONTINUE, pasar a la siguiente iteracion

# for que recorre el string
for letra in "python":

	if letra == "h":
		# IGNORAR EL RESTO DEL BUCLE Y PASAR A LA SIGUIENTE ITERACION, osea no imprime h
		continue


	print("Viendo la letra: ", letra)

print()

# contar caracteres de un texto:
nombre = "pildoras informaticas"

print("El numero de caracteres es: ", len(nombre)) # imprimir longitud

# for para que cuente el numero de letras:
cont = 0
for letra in nombre:

	if letra == " ":
		continue


	cont += 1

print("El numero de letras validad es: ", cont)

print()

# INSTRUCCION PASS : anular

# ctrl + c salir de bucle infinito
"""
while True:
	pass
"""
"""
class MiClase:
	pass
"""
# tambien en funciones

# INSTRUCCION ELSE:

mail = input("Introduce un mail: ")

for i in mail:

	if i == "@":
		arroba = True

		break 	# cuando encuentre un arroba, arroba pasa a true y sale del for, y el else forma parte del for

else: 	# SE EJECUTA CUANDO y si se TERMINA DE EJECUTARSE todo EL bucle. por ejemplo si hace break porque detecta arroba (por lo tanto no termine de ejecutar el bucle), entonces no se ejecuta el else!
	arroba = False


print("Existe arroba?", arroba)