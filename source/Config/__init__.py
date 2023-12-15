from typing import Union
import logging
from logging import FileHandler
from colorama import (
	Fore,
	init as coloramaInit
)
import configparser
import json




class Config:
	"""
    Clase para configurar diversos aspectos del entorno de ejecución.


    Métodos
    -------
    __init__()
        Constructor de la clase Config. Inicializa la instancia de Colorama.

    logging_config()
        Configura el archivo 'logging.log' para el registro de debug y manejo de errores.

	read_config()
		Lee la configuración de 'config.cnf'

    Ejemplo
    -------
    config_instance = Config()
    config_instance.logging_config()
	config_instance.read_config()
    """
	def __init__(self):
		"""
		Constructor de la clase.
		"""
		self.Colorama.reset()



	def logging_config(self) -> bool:
		"""
		Function:
		--------
		- Configurar archivo logging.log para debug y manejo de errores.

		Returns:
		-------
		- True or False: Si se completa la función exitosamente retorna True, si no retorna False.

		"""
		try:
			# Configurar el logger
			logger = logging.getLogger()
			logger.setLevel(logging.DEBUG)

			# Crear un handler para escribir en un archivo con codificación UTF-8
			file_handler = logging.FileHandler('logging.log', encoding='utf-8')

			# Configurar el formato del log
			formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
			file_handler.setFormatter(formatter)

			# Agregar el handler al logger
			logger.addHandler(file_handler)

			# Añadir una línea para verificar si el logger se configura correctamente
			print("Logger configurado correctamente")
			logger.info(f"Logger configurado correctamente | File: {__file__}")

			# Retornar True
			return True
		except Exception as e:
			# Escribir Error y retornar False
			logging.error(f"No se pudo configurar logging.basicConfig: {e} | File: {__file__}")
			return False
	def read_config(self) -> bool:
		try:
			# Crear un objeto ConfigParser
			config = configparser.ConfigParser()

			# Leer la configuración desde el archivo
			config.read('config.cnf')

			# Obtener valores específicos
			self.url = config.get('checker', 'url')
			self.ssl = config.getboolean('checker', 'ssl')
			self.timeout = config.getint('checker', 'timeout')
			self.file_result = config.get('checker', 'file-result')
			self.file = config.get('checker', 'file')
			headers_str = config.get('checker', 'headers')
			# Parsear la cadena de headers como un diccionario
			
			self.headers = json.loads(headers_str)

			return True
		except Exception as e:
			logging.error(f"Error en funcion read_config(): {e} | File: {__file__}")




	class Colorama:
		"""
		Clase que encapsula el uso de la biblioteca colorama para el manejo de colores en la consola.


		Métodos
		-------
		reset()
			Intenta inicializar colorama con autoreset activado.

		Ejemplo
		-------
		colorama_instance = Colorama()
		if colorama_instance.reset():
			print(f"{Fore.GREEN}Este texto está en verde.{Style.RESET_ALL}")
		else:
			print("Error al inicializar colorama.")
		"""

		def __init__(self):
			"""
			Constructor de la clase.
			"""
			pass

		def reset(self):
			"""
			Intenta inicializar colorama con autoreset activado.

			Returns
			-------
			bool
				True si la inicialización fue exitosa, False si hubo un error.
			"""
			try:
				# Inicializar colorama con autoreset
				colorama_init(autoreset=True)
				return True
			except Exception as e:
				logging.error(f"Error en función de reseteo automático de colorama: {e} | File: {__file__}")
				return False


