#ctrl + s = guardar
#ctrl + b = ejecutar

def suma(num1, num2):
	print(num1 + num2)

def multiplica_dos(uno,dos):
	resultado = uno*dos
	
	return resultado

suma(5, 5)
suma(10.0, 10)
suma(20, 20.1)

def texto(texto1, texto2):
	print(texto1 + texto2)

texto("hola", " mundo")
texto("como ", "estas?")

numeroo = multiplica_dos(10, 5)
print(numeroo)

numeroString = str(numeroo)
print(type(numeroString))

print(texto("el result de los numeros restados es: ", numeroString))