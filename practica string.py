nombreUsuario = input("Ingresa tu nombre de usuario: ")

print("En mayusculas: .upper() " + nombreUsuario.upper())

print("En minusculas: .lower() " + nombreUsuario.lower())

print("En formato title() : " + nombreUsuario.title())

print("El numero de caracteres de la cadena es: ", len(nombreUsuario))

print("En la primera posicion que se encuentre la \"e\": ", nombreUsuario.find("e"))

print("Cuantas veces aparece la letra \"e\": ", nombreUsuario.count("e") )

print("La diferencia entre str.title() y str.capitalize() es que la primera añade mayusculas inicial a todas las palabras y capitalize unicamente a la primera palabra!")

print("En formato capitalize() : " + nombreUsuario.capitalize())

print("Reemplazar todas las \"e\" por 3 : ", nombreUsuario.replace("e", "3"))

edad = input("Introduce tu edad: ")

print("Ver si es numero, str.isdigit() : ", edad.isdigit())


if (edad.isdigit()):

# se pasa a int para que pueda hacer la evaluacion!!!!!!!!
	if (int(edad) < 18):
		print("eres menor de edad")

	else:
		print("Eres mayor de edad")

else:
	print("Edad no es un digito")


while (edad.isdigit() != True):

	print("Vuelve a introducer tu edad, no has puesto un numero")

	edad = input("Introduce edad: ")

print("Bien hecho tienes: ", edad, " años!")