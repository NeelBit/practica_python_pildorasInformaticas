print("Programa para saber si se recibe beca")

distanciaEscuela = int(input("Introduce la distancia de la que vives de la escuela: "))
print(distanciaEscuela)

numHermanos = int(input("Introduce la cantidad de hermanos que tengas: "))
print(numHermanos)

salarioFam = int(input("Introduce tu salario familiar: "))
print(salarioFam)

# si tiene salario menor a 20000 lo mismo sera beneficiario. osea f y f o v da v
if distanciaEscuela>40 and numHermanos>2 or salarioFam<=20000:
	print("Felicidades eres beneficiario de la Beca!")

else:
	print("NO cumples los requisitos para la beca :(")

