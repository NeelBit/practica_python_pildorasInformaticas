miLista = ["Maria", "Pepe", "Julieta", "Fulanito"]

# Imprime toda la lista
print(miLista[:])

# imprime elemento solo, dado un indice
print(miLista[1])

# Para acceder y empezar a contar desde el final, se utiliza en negativo. Ej: -2 --> Julieta
print(miLista[-2])

# Imprimir porcion de lista, queda excluido el último indice!
print(miLista[0:2])

# Imprimir ultimos elementos, es decir, desde 2 hasta el final
print(miLista[2:])

# AÑADIR ELEMENTOS:
miLista.append("Cosito") 		# agregar elemento  al final
print(miLista[:])

miLista.insert(2, "Sandra")		# agregar elemento en indice dado
print(miLista[:])

miLista.extend(["nel", "anteUltimoNombre", "ultimoNombre", 9]) 	# agregar varios elementos al final
print(miLista[:])

# Que nos devuelta el indice de un elemento dado (del primer elemento que se encuentra en la lista) --> recordar que sandra se agrego en el indice 2
print(miLista.index("Pepe")) 

# Saber si un elemento se encuentra o no en la lista:
print("Cosito" in miLista)

print(9 in miLista)

# ELIMINAR ELEMENTOS:
# Eliminar elemento dado
miLista.remove("Julieta")
print(miLista[:])

# elimina el último elemento
miLista.pop()
print(miLista[:])


miLista2 = [0, 1, 2, 3, 4]
print(miLista2[:])

# Unir o sumar listas:
miLista3 = miLista + miLista2
print(miLista3[:])

# Repetir o multiplicar elementos:
miLista4 = ["cero", "uno", "dos"] * 3
print(miLista4[:])