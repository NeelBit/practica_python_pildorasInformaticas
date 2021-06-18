print("Asignaturas optativas: ")
print("""
	informatica grafica
	pruebas de software
	usabilidad y accesibilidad""")

asignatura = input("Ingrese la asignatura escogida: ")
# solucion al tema de minuscula y mayuscular para que sea igual la comparacion:
asignaturaTodoMinuscula = asignatura.lower()

if asignaturaTodoMinuscula in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("felicidades has seleccionado " + asignaturaTodoMinuscula)

else: 
	print("Asignatura no valida! :(")