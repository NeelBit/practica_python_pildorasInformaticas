
def areaTriangulo(base, altura):

	"""
	Calcula el área de un triangulo, recibe base y altura

	>>> areaTriangulo(3, 6)
	'El area del triangulo es: 9.0'

	>>> areaTriangulo(2, 5)
	'El area del triangulo es: 5.0'
	
	"""

	return "El area del triangulo es: " + str((base*altura)/2)

# >>> la funcion y abajo ponemos el resultado que deberia salir.

def compruebaMail(mail):

	"""
	La funcion compruebaMail, evalua un mail recibido por parametro. Debe contener un arroba
	y no debe estar al final.

	>>> compruebaMail('pildoras@a.co')
	True

	>>> compruebaMail('pil')
	False

	>>> compruebaMail('pi.l@')
	False

	>>> compruebaMail('pi.l@sfjasdf@')
	False

	"""

	arroba = mail.count("@")

	if (arroba != 1 or mail.rfind('@')==len(mail)-1) or mail.find('@')==0: 	# si arroba es distinto de 1 , ó si el arroba se encuentra al final!
													# esta ultima declaracion se puede omitir pero es para practicar.
		return False

	else:
		return True


import doctest

doctest.testmod()


cadena = "h@ola@"
print(cadena.rfind('@')) # rfind nos dice la posicion pero empieza a revisar desde el final

if(cadena.rfind('@') == len(cadena)-1):

	print("Sí hay un arroba al final")

else:

	print("NO hay arroba al final")