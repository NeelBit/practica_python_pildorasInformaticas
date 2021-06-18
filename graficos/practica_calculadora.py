from tkinter import *

raiz = Tk()
raiz.title("Calculadora")
raiz.iconbitmap("iconoCalculadora.ico")
raiz.config(bg="black")

# ----- FRAME ----- #
miFrame = Frame(raiz, bg="black")
miFrame.pack()

# VARIABLES GLOBALES
operacion = ""
resultado = 0


# ----- PANTALLA ----- #
numeroPantalla = StringVar()


pantalla = Entry(miFrame, textvariable=numeroPantalla) # asociar la variable al entry
 # pantalla en fila 1 columna 1 y que este separado vertical y horizontalmente. columnspan le decimo que junte o abarque varias columnas
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="black", fg="green", font="-weight bold", justify="right", relief="groove", bd=5)



# ----- PULSACIONES TECLADO ----- #
 # funcion que se llama al presionar un boton
def numeroPulsado(num):

	# como hacemos que cuando pulsamos una operacion deje de concatenar:
	global operacion
	# si operacion es diferente de cadena vacia
	if (operacion != ""):

		# si presiono alguna operacion no va a esta vacia, y por lo tanto no concatenes, pasa a la pantalla el num
		numeroPantalla.set(num)

		# le decimos que operacion valo de nuevo cadena vacia para que concatene de nuevo, y pasara al else hasta que vuelva a presionar.
		operacion = ""

	else: 

		numeroPantalla.set(numeroPantalla.get() + num) # necesario lambda para que pueda pasar parametro



# ----- OPERACION SUMA ----- #
def suma(num):

	global operacion # le indico que voy a utilizar la variable global

	global resultado

	resultado += int(num) # incrementa a resultado el valor que hay en pantalla

	operacion = "suma" # al pulsar el boton +, llama a esta funcion y almacena en la variablo global operacion la palabra suma

	numeroPantalla.set(resultado) # para que a medida que vemos el resultado lo deje en pantalla


# ----- OPERACION RESTA ----- #
def resta(num):

	global operacion

	global resultado

	resultado -= int(num)

	operacion = "resta"

	numeroPantalla.set(resultado)

# ----- OPERACION DIVISION ----- #
def division(num):

	global operacion

	global resultado

	resultado /= int(num)

	operacion = "division"

	numeroPantalla.set(resultado)

# ----- OPERACION MULTIPLICACION ----- #
def multiplicacion(num):

	global operacion

	global resultado

	resultado *= int(num)

	operacion = "multiplicacion"

	numeroPantalla.set(resultado)


# ----- RESULTADO = ----- #
def elResultado():

	global resultado

	numeroPantalla.set(resultado+int(numeroPantalla.get()))

	# reseteamos resultado
	resultado = 0


# ----- FILA 1 DE BOTONES ----- #
btn7 = Button(miFrame, text="7", width=3, bg="white", command=lambda:numeroPulsado("7"))
btn7.grid(row=2, column=1)

btn8 = Button(miFrame, text="8", width=3, bg="white", command=lambda:numeroPulsado("8"))
btn8.grid(row=2, column=2)

btn9 = Button(miFrame, text="9", width=3, bg="white", command=lambda:numeroPulsado("9"))
btn9.grid(row=2, column=3)

btnDividir = Button(miFrame, text="/", width=3, bg="gray", command=lambda:division())
btnDividir.grid(row=2, column=4)

# ----- FILA 2 DE BOTONES ----- #
btn4 = Button(miFrame, text="4", width=3, bg="white", command=lambda:numeroPulsado("4"))
btn4.grid(row=3, column=1)

btn5 = Button(miFrame, text="5", width=3, bg="white", command=lambda:numeroPulsado("5"))
btn5.grid(row=3, column=2)

btn6 = Button(miFrame, text="6", width=3, bg="white", command=lambda:numeroPulsado("6"))
btn6.grid(row=3, column=3)

btnMultiplicar = Button(miFrame, text="x", width=3, bg="gray", command=lambda:multiplicacion())
btnMultiplicar.grid(row=3, column=4)

# ----- FILA 3 DE BOTONES ----- #
btn1 = Button(miFrame, text="1", width=3, bg="white", command=lambda:numeroPulsado("1"))
btn1.grid(row=4, column=1)

btn2 = Button(miFrame, text="2", width=3, bg="white", command=lambda:numeroPulsado("2"))
btn2.grid(row=4, column=2)

btn3 = Button(miFrame, text="3", width=3, bg="white", command=lambda:numeroPulsado("3"))
btn3.grid(row=4, column=3)

btnResta = Button(miFrame, text="-", width=3, bg="gray", command=lambda:resta())
btnResta.grid(row=4, column=4)

# ----- FILA 4 DE BOTONES ----- #
btn0 = Button(miFrame, text="0", width=3, bg="white", command=lambda:numeroPulsado("0"))
btn0.grid(row=5, column=1)

btnComa = Button(miFrame, text=",", width=3, command=lambda:numeroPulsado("."))
btnComa.grid(row=5, column=2)

btnIgual = Button(miFrame, text="=", width=3, fg="green", command=lambda:elResultado())
btnIgual.grid(row=5, column=3)

btnSuma = Button(miFrame, text="+", width=3, bg="gray", command=lambda:suma(numeroPantalla.get()))
btnSuma.grid(row=5, column=4)







raiz.mainloop()