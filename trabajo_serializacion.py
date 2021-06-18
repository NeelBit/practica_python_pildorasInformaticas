import pickle
"""
# creamos lista
listaNombre = ["nombre1", "nombre2", "nombre3", "nombre4", "nombre5"]

# creamos archivo con permisos de escritura y lectura binaria: w (write) b (binaria)
ficheroBinario = open("fichero_binario_listaNombre", "wb")

# hacemos volcado de la lista, al fichero externo: primer parametro el objeto que queremos pasar y segundo parametro el objeto del fichero
pickle.dump(listaNombre, ficheroBinario)

# cerramos el fichero:
ficheroBinario.close()

# podemos borrarlo de la memoria:
del ficheroBinario

"""
# UNA VES QUE YA CREAMOS EL ARCHIVO, VAMOS A VERLO:

ficheroBinarioLectura = open("fichero_binario_listaNombre", "rb")

lista = pickle.load(ficheroBinarioLectura)

print(lista)

ficheroBinarioLectura.close()