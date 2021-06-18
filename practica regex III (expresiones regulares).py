# rangos y expresiones regulares

import re

lista = ["ana",
		"pedro",
		"jose",
		"juan",
		"macarena",
		"maria",
		"mengano"]

# buscar por ejemplo nombre que tengan las letras de la O a las T
for elemento in lista:

	if (re.findall('[o-t]',elemento)): 	# devuelve todos los elementos de la lista en cuyo interior tengas ese rango de letras.

		print(elemento)

print()

# todos los que comienzan con caracteres de la a a la J
print("comienzan con letras de a a j: ")
for elemento in lista:

	if (re.findall('^[a-j]', elemento)): 	# si queremos los que tengan esa terminacion: '[a-j]$'

		print(elemento)

# si por ejemplo tenemos una lista con terminacion con codigos:

lista2 = ["ma1",
			"va1",
			"ma2",
			"se1",
			"ba1",
			"ma3",
			"va2",
			"ma4",
			"maA",
			"ma5",
			"maB",
			"maC"]

print()
print("elementos de lista2 de madrid con terminacion de codigo del 1 al 3, y A al B")
for i in lista2:

	if (re.findall('ma[1-3A-B]', i)):	 	# que nos filtre todos los elementos de madrid del 1 al 3, y A al B
										# si queremos que NO sean esos elementos, usamos 'ma[^0-3]' para que nos devuelva ma4, maA, ma5, maB por ejemplo!
		print(i)

# si por ejemplo varios elementos tienen . o : entre medio, en los corchetes ponemos [.:] y nos devolvera esos elementos


