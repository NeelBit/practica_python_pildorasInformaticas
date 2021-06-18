from setuptools import setup

setup(

	name = "paqueteCalculos",
	version = "0.1",
	description = "Paquete de redondeo y potencia",
	author = "Nel",
	#author_email = "mail",
	#url = "sitio"

	packages = ["calculos", "calculos.redondeo_potencia"]

	)

# PARA INSTALLAR PAQUETE, en consola desde ubicacion dist: pip3 install nombreDelpaquete.tar.gz
# PARA DESINTALAR PAQUETE, en consola en cualquier ubicacion: pip3 uninstall nombreDelPaqueteEjPaqueteCalculos
