
import logging

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

# Agregar algunos mensajes de prueba
logger.debug('Este es un mensaje de depuración')
logger.info('Este es un mensaje de información')
logger.warning('Este es un mensaje de advertencia')
logger.error('Este es un mensaje de error')
logger.critical('Este es un mensaje crítico')

# Añadir una línea para verificar si los mensajes se están escribiendo en el archivo
print("Mensajes escritos en el archivo")

# Cerrar el logger
logger.removeHandler(file_handler)