# for que recorre lista con 2 string y un int
#for i in ["pildoras", "informaticas", 3]:
	# Recorrera 3 veces porque hay 3 elementos
#	print("Hola", end=" ") # imprimir juntos, osea decirle que no haga saltos de linea, si dejamos espacio en las comillas deja el espacio entre print

# recorrer string
#for i in "juan@pildorasinformaticas.com":
#	print(i, end=" ") 	 # imprimir caracter a caracter separado por espacio

# COMPROBAR CORREO ELECTRONICO:

contArroba = 0
contPunto = 0
"""
for i in "juan@pildorasinformaticas.com":

	if i=="@":
		contArroba +=1
	elif i==".":
		contPunto +=1

if contArroba == 1 and contPunto == 1:
	print("Mail correcto!")

else:
	print("Mail Incorrecto!!!")

"""

# COMPROBAR MAIL INGRESANDO POR INPUT:
mail = input("Ingrese su mail: ")

for i in mail:

	if i=="@":

		contArroba +=1

	elif i==".":

		contPunto +=1

print(f"Tu mail tiene {contArroba} arrobas y {contPunto} puntos!")

if contArroba == 1 and contPunto >= 1:
	print("Mail correcto!")

else:
	print("Mail incorrecto!!!")


# FALSE Y TRUE EN PYTHON VAN CON LA PRIMERA LETRA EN MAYUSCULAS: True False

# PYTHON 3 CONSIDERA A RANGE COMO UN TIPO, ENTONCES CREA UNA ESPECIE DE LISTA QUE VA DEL 0 AL 4 EN ESTE CASO, 5 ELEMENTOS. Y LOS RECORRE con el for
for i in range(5):
	print("Hola", i)

