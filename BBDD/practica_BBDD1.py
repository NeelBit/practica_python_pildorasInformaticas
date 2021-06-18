import sqlite3

# crear conexion, y si no esta creada la bbdd la crea.
miConexion = sqlite3.connect("PrimeraBBDD")

# ahora creamos cursor/puntero. para poder modificar
miCursor = miConexion.cursor()

# ahora creamos tabla por ejemplo: dentro de execute("aca van la intruccion sql") VARCHAR(50) ES EL TIPO QUE VA A ALMACENA Y 50 LA LONGITUD DE CARACTERES
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# insertar contenido a la tabla: INSERT INTO nombreTabla VALUES('prod', precio, 'seccion') .utilizamos comillas simples si estamos dentro de comillas dobles
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

"""

# crear lista con varias tuplas con registros para insertar: insertar lote de registros
variosProductos = [
	("CAMISETA", 15, "DEPORTES"),
	("JARRON", 90, "CERAMICA"),
	("CAMIÓN", 20, "JUGUETES")

]

# executemany() para agregar  . TANTOS ? COMO VALORES TENGA (producto, precio, seccion)
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?)", variosProductos)

"""

# LEER BASE DE DATOS: select * para que devuelva todos los registros
miCursor.execute("SELECT * FROM PRODUCTOS")

# almacenamos registros en una lista:
variosProductosRescatado = miCursor.fetchall()

# imprimimos lista con las tuplas de registros
print(variosProductosRescatado)

# recorrerlo con un for: para que imprima tupla a tupla
for prod in variosProductosRescatado:

	print(prod)
	print()

	# imprimir solo el producto:
	print("Nombre art: ", prod[0], " Precio: ", prod[1])


# cada ves que se hace un cambio en una tabla hay que verificar cambio: es como confirmar los cambios.
miConexion.commit()


miCursor.close()
miConexion.close()