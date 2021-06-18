# Verificacion de acceso:
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
	print("Puedes pasar!")

elif edad > 110 or edad < 0: 	# si se utiliza otro if, al cumplirse la primera condicion de arriba, y esta no, se ejecuta tambien el else. osea si es mayor dice: puedes pasar no puedes pasar. porque el else corresponde a la segunda condicion
	print("Edad incorrecto")

else:		# el else acompaña al if mas cercano, osea el de arriba
	print("NO puedes pasar")