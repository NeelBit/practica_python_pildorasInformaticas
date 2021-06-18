print(range(10))

# CONCATENAR TEXTO CON VALORES:
for i in range(10):
	print(f"La i, en el rango valdría: {i}")

# FOR ANIDADO INTENTO DE ESCALERITRA:
cont=0
for i in (range(5)):
	print("")
	for j in (range(i+1)):

		print("*", end="")

# Salto de linea:
print("")

# range(deDondeComienza, hastaDondeVa, deCuantoEnCuantoVa) --> si pongo 100 como en el ejemplo en realidad termina en el 99
for i in range(0, 100, 10):
	print(f"El valor de i es: {i}")

print("")
print("Imprimir una palabra la longitud de caracteres que tenga de veces: longitud")

palabra = "longitud"

print(f"la palabra longitud tiene: {len(palabra)} caracteres! ")

for i in range(len(palabra)):
	print(f"posicion ({i})")
	print(palabra[i])
	print("")
