# acceder a elementos que se encuentran dentro de otros elementos. bucle for anidado:


# cuando ponemos arterisco delante del parametro indicamos que va a recibir numero indefinido de argumentos!!! y en forma de tupla!!!
def devuelveCiudades(*ciudades):
	#recorre la tupla 
	for elemento in ciudades:
		""" yield from nos permite precindir de for anidados!!!
		for subElemento in elemento:

			yield subElemento
		"""		
		# osea el yield from recorre el elemento de los elementos.
		yield from elemento


ciudadesDevueltas = devuelveCiudades("madrid", "barcelona", "bs. as.", "resistencia")

print(next(ciudadesDevueltas))
print("Salto de linea!")
print(next(ciudadesDevueltas))