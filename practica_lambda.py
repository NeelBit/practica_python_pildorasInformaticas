"""
def areaTriangulo(base, altura):

	return (base*altura)/2

print("El area de un triangulo con base 5 y altura 7 es: ", areaTriangulo(5, 7), "y esto sigue!")

triangulo1 = areaTriangulo(5, 10)
triangulo2 = areaTriangulo(10, 20)

print(triangulo1)
print(triangulo2)
"""

# en funciones lambda en ves de return ponemos : 
"""
areaTrianguloLambda = lambda base, altura:(base*altura)/2

triangulo3 = areaTrianguloLambda(5, 7)
triangulo4 = areaTrianguloLambda(10, 20)

print(triangulo3)
print(triangulo4)"""

"""
alCubo = lambda num: num**3 # o podemos poner lambda num:pow(num, 3)

print(alCubo(3))
"""

destacarSalario = lambda comision: "¡{}! $".format(comision)

comisionAna = 11500

print(destacarSalario(comisionAna))