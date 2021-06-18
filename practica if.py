# funciona evaluacion que recibe una nota y va a devolver aprobado o no

print("Programa de evalación de notas de alumnos: ")

# Introducir datos (la nota) - input puede recibir una cadena como mensaje o no. devuelve STRING, por eso debemos utilizar int() para pasarlo a intero
notaAlumno = int(input("Ingrese la nota aquí!: "))

print(type(notaAlumno))

def evaluacion(nota):
	valoracion = "Aprobado"

	if nota <= 5:
		valoracion = "Desaprobado"

	return valoracion

print(evaluacion(notaAlumno)) 	# Tambien podemos poner aca el int() en ves de hacerlo al input(). ej: print(evaluacion(int(notaAlumno)))