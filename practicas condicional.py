# ctrl + alt + b : para ejecutar python 

# python tiene concatenacion de operadores en condiciones: 0<edad<100 seria edad mayor que cero y menor que 100. Lee de izquierda a derecha, osea si edad no es mayor a cero, ignora el resto
# concatenacion de comparadores de operacion!
salarioPresidente = int(input("Ingrese salario Presidente: "))
print("Salario presidente: " + str(salarioPresidente)) 		# CONCATENAR CON STRING CAUSA PROBLEMAS, ENTONCES USAMOS LA FUNCION STR() PARA PASAR A STRING LA VARIABLE

salarioDirector = int(input("Ingrese salario Director: "))
print("Salario director: " + str(salarioDirector))

salarioJefeDeArea = int(input("Ingrese salario del Jefe de Area: "))
print("Salario del Jefe de Area: " + str(salarioJefeDeArea))

salarioAdministrativo = int(input("Ingrese salario Administrativo: "))
print("Salario Administrativo: " + str(salarioAdministrativo))

if salarioPresidente>salarioDirector>salarioJefeDeArea>salarioAdministrativo: 	# CONCATENACION DE COMPARADORES DE OPERACION
	print("Todo en orden")

else:
	print("Algun sueldo no corresponde")