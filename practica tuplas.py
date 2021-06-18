miTupla = (1, 2, 3, 4, 5, "hola", "como", "te", "va", 5)
print(miTupla)

# Al indice se accede por corchetes!
print(miTupla[4])

# CONVERTIR TUPLA EN LISTA:
miLista = list(miTupla)
print(miLista)

# CONVERTIR LISTA EN TUPLA:
miTupla2 = tuple(miLista)
print(miTupla2)

# Comprobar si tiene elemento la tupla: (igual que en las listas)
print(5 in miTupla2)

# Contar la cantidad de veces que se repite cierto elemento: en lista o tupla
print(miTupla2.count(5))
print(miLista.count(5))

# SABER LA LONGITUD (cantidad de elementos): de tupla o lista
print(len(miTupla2))
print(len(miLista))

# crear tupla unitaria, es decir, 1 solo elemento
miTuplaUnitaria = ("un elemento", )
print(miTuplaUnitaria)
print(len(miTuplaUnitaria))

miTupla3 = ("cer0", "un1", "do2", "tre3")
print(miTupla3)

# desempaquetado de tupla, osea pasar a variables el contenido: creo las variables y es igual a la tupla. Tiene que tener la misma cantidad de variables que de contenido en la tupla!
cero, uno, dos, tres = miTupla3

print(tres) 	#variable

# Si permite el uso de index las tuplas desde las ultimas versiones de python.
print(miTupla3.index("do2"))