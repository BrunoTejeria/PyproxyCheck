from typing import Union
import logging
from logging.handlers import FileHandler

class Config:
	def __init__(self):
		pass

	def logging_config(self) -> Union[bool, None]:
		try:
			# Configurar el logger
			logger = logging.getLogger()
			logger.setLevel(logging.DEBUG)

			# Crear un handler para escribir en un archivo con codificación UTF-8
			file_handler = FileHandler('archivo_log.log', encoding='utf-8')

			# Configurar el formato del log
			formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
			file_handler.setFormatter(formatter)

			# Agregar el handler al logger
			logger.addHandler(file_handler)

			# Retornar True
			return True
		except Exception as e:
			# Escribir Error y retornar None
			logging.error(f"No se pudo configurar logging.basicConfig: {e} | File: {__file__}")
			return None


