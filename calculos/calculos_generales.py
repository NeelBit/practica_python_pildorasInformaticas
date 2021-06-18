import random

def sumar(op1, op2):

	print(f"El resultado de la suma entre {op1} y {op2} es: ", op1 + op2)

def restar(op1, op2):

	print(f"El resultado de la resta entre {op1} y {op2} es: ", op1 - op2)

def multiplicar(op1, op2):

	print(f"El resultado de la multiplicacion entre {op1} y {op2} es: ", op1 * op2)


numeroCualquiera = random.randint(1, 100) # numero pseudoAleatorio entre 1 y 100

def dividir(dividendo, divisor):

	print(f"El resultado de dividir entre {dividendo} y {divisor} es: {dividendo/divisor}")

def potencia(base, exponente):

	print(f"El resultado de la potencia entre {base} y {exponente} es: {base ** exponente}")

def redondear(numero):

	print(f"El redondeo de {numero} es: {round(numero)}")

#redondear(8.732)