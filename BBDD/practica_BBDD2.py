import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

"""
# 3 comillas simples muy util para dividir en varios renglones la instruccion
# primary key hay que agregarlo al campo que sea clave.
miCursor.execute('''

	CREATE TABLE PRODUCTOS (
	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))

''')

productos = [
	
	("AR01", "PELOTA", 20, "JUGUETERIA"),
	("AR02", "PANTALON", 30, "CONFECCION"),
	("AR03", "DESTORNILLADOR", 10, "FERRETERIA"),
	("AR04", "JARRON", 40, "CERAMICA")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?, ?)", productos)
"""

# añadimos un producto
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'REMERA', 15, 'CONFECCION')")


# prueba para intentar añadir producto a la lista con clave repetida: ERROR INTEGRITY : UNIQUE
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR02', 'TREN', 20, 'JUGUETERIA')")



# AUTOMATIZAR PRIMARY KEY: por convencion suele denominarse ID el campo automatico
# si además existe otro campo que no queremos que repita contenido agregamos UNIQUE, por ejemplo en NOMBRE_ARTICULO
# con las instrucciones de arriba entonces estamos indicando que no se repitan informacion en esos 2 campos

"""

miCursor.execute('''

	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	SECCION VARCHAR(20))

''')

productos = [ # COMO LE INDICAMOS PRIMARY KEY AUTOINCREMENT YA NO DEBEMOS PASAR EL CAMPO ID
	
	("PELOTA", 20, "JUGUETERIA"),
	("PANTALON", 30, "CONFECCION"),
	("DESTORNILLADOR", 10, "FERRETERIA"),
	("JARRON", 40, "CERAMICA"),
	("PANTALONes", 45, "CONFECCION")

]

# insertamos registros, pasamos la lista a la BBDD - como parametro donde va el ID autoincrementable pasamos NULL
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL, ?, ?, ?)", productos)

"""

# ya tenemos la base de datos creada vamos READ:
# miCursor.execute("SELECT * FROM PRODUCTOS") # para ver todos

"""
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='CONFECCION'")

rescateProduct = miCursor.fetchall()

print(rescateProduct)
"""

# HACER UPDATE ACTUALIZAR base de datos: modificar el precio de pantalon a 40 por ejemplo
#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=40 WHERE NOMBRE_ARTICULO='PANTALON'")

# PARA BORRAR REGISTRO: vamos a borrar PANTALONes NUNCA OLVIDARSE LA CLAUSULA WNERE EN UN DELETE - tambien podemos usar ID=5 como criterio en ves de NOMBRE_ARTICULO
#miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO='PANTALONes'")



miConexion.commit()

miConexion.close()