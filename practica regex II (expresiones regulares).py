import re

# ANCLA - COMIENZO Y FIN - COMODINES

listaNombres = ["juan peres", 
				"pepe mujica", 
				"fulano cosme", 
				"mengano fulanito",
				"mengano mujica", 
				"robot pezcador"
				]

for i in listaNombres:

	if (re.findall('^juan', i)): 	# ^queArranqueConEsto
		print("nombre que arrancan con juan: ")
		print(i)

	print()

	if (re.findall('mujica$', i)):	# queFinaliceConEsto$
		print("nombres que finalizan en mujica: ")
		print(i)

	print()

# muy util por ejemplo para caracteres latinos o también para tildes!

	if (re.findall('[z]', i)):
		print("se encuentra la Z")	# si se encuentra la [zOvariosCaracteresEnCualquierOrden]
		print(i)

print()

lista2 = ["hombre",
			"mujeres",
			"niños",
			"niñas",
			"mascotas",
			"camion",
			"camión"
			]


print("imprimimos palabras que arrancan con niñ[o ó a]s : ")

for i in lista2:

	# por ejemplo si queremos que nos muestre "niños" y "niñas"
	if (re.findall('niñ[oa]s', i)): 
		print(i)

print()

femeOmascu = input("ingrese si f o m (o ó a): ")

print("ingresaste: ", femeOmascu)

for i in lista2:
# segun el patron ingresado:
	if (re.findall(f'niñ[{femeOmascu}s]', i)):
		print(i)

print()

# un ejemplo para buscar palabras que se pudieron olvidar la TILDE
print("imprimimos camion y camión")
for i in lista2:

	if (re.findall('cami[oó]n', i)):
		print(i)
