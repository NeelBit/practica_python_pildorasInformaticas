import pickle
from serializar_objetos import Vehiculo

ficheroApertura = open("listaCochesBinario", "rb")

listaCochesCargado = pickle.load(ficheroApertura)

ficheroApertura.close()

for i in listaCochesCargado:

	i.estado() # estado ya tiene print, no es necesario por lo tanto aca