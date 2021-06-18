import re

# MATCH SIEMPRE VA A BUSCAR AL PRINCIPIO

nombre1 = "Sandra Lopez"
nombre2 = "Antonio Gomez"
nombre3 = "Maria Lopez"
nombre4 = "Lara fulana"
nombre5 = "jara mengano"

lista = [nombre1, nombre2, nombre3]

# MATCH SIEMPRE NOS VA A BUSCAR AL COMIENZO DE UN STRING

if re.match("sandra", nombre1, re.IGNORECASE): # dentro del primer parametro podemos combinar con patrones de busqueda
								# como TERCER parametro podemos poner ignorecase para ignorar mayuscula o minuscula

	print("Hemos encontrado el nombre:", nombre1)

else:
	print("no hemos encontrado")


print()

# BUSCAR EN GOOGLE PATRONES DE BUSQUEDA PYTHON !

if (re.match(".ara", nombre5, re.IGNORECASE)):

	print("Hemos encontrado")

else:
	print("no hemos encontrado coincidencias")


print()

cadena1 = "Julia cadena71"
cadena2 = "456cadenita"
cadena3 = "cadena789cadenototaaaaaaaaaaaaaaa71a"


print("\\d nos busca numeros en la cadena, en match se fija que este al comienzo \n\\d digit")

if (re.match("\d", cadena2, re.IGNORECASE)):

	print("encontrado con \\d numero, y match para indicar al inicio")
else:
	print("no encontrado")

print()
print("patron search buscar en toda la cadena de texto si el patron se encuentra o no se encuentra")
print()

# match buscar al inicio de cadena - search buscar en toda la cadena:

if (re.search("4", cadena2, re.IGNORECASE)):

	print("Se encontro")

else: 
	print("NO se encontro")

# buscar en cadenas que tengan lopez:
print("buscar con search en cadena que contengan algo")

if (re.search("lopez", nombre3, re.IGNORECASE)):

	print("encontrado lopez")

else:
	print("no encontrado")


print()
print("buscar el 71 en cadenas de texto: ")

if (re.search("71", cadena3)):

	print("se encontro")

else:
	print("no se encontro!")