# Las claves no se repiten!

miDiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londes", "España":"Madrid", "producto 1":5, 23:"Jordan"}
print(miDiccionario)

# Ver la capital de Francia. Clave Francia: valor París . Corchetes para acceder y la clave
print(miDiccionario["Francia"])

# Ver el valor de la clave España:
print(miDiccionario["España"])

# Ver el valor de la clave producto 1:
print(miDiccionario["producto 1"])

# AÑADIR ELEMENTO:
miDiccionario["Italia"] = "Lisboa" 	# error aproposito
print(miDiccionario)

# MODIFICAR VALOR DE CLAVE:
miDiccionario["Italia"] = "Roma"
print(miDiccionario)

# ELIMINAR ELEMENTO: del y la clave
del miDiccionario["Reino Unido"]
print(miDiccionario)

# utilizar tupla para asignar valores.
miTupla = ("Argentina", "Paraguay", "Chile")

miDiccionarioLatino = {miTupla[0]:"Bs. As.", miTupla[1]:"Asuncion", miTupla[2]:"Santiago de Chile"}
print(miDiccionarioLatino)

# utilizar lista para asignar valores:
miLista = [2, 4, 6, 8]

miDiccionarioNum = {miLista[0]:"dos", miLista[1]:"cuatro", miLista[2]:"seis", miLista[3]:"ocho"}
print(miDiccionarioNum)

# acceder a un valor: por ejemplo el valor de la clave 6
print(miDiccionarioNum[6])

# ALMACENAR UNA lista COMO VALOR DE UN CODIGO: TAMBIEN PODEMOS ALMACENAR DICCIONARIO DENTRO DE DICCIONARIO
miDiccionarioConLista = {23:"jordan", "nombre":"michael", "equipo":"chicago", "anillos":[1991, 1992, 1993]}
print(miDiccionarioConLista)

# para acceder al valor de la clave equipo:
print(miDiccionarioConLista["equipo"])

# ALGUNOS METODOS UTILES PARA DICCIONARIOS!! :
# Claves:
print(miDiccionarioLatino.keys())

# Valores:
print(miDiccionarioLatino.values())

# longitud:
print(len(miDiccionarioLatino))