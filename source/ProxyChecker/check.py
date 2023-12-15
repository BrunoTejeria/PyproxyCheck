import logging
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import (
	Fore,
	init as coloramaInit
)
coloramaInit(autoreset=True)


class Check():
	def __init__():
		pass


	def check_proxies(self, headers, url, proxies, ssl):
		self.headers: dict = headers
		self.proxies: list = proxies
		self.url: str = url
		self.ssl: str = ssl
		self.working_proxies:list = []
		def check(proxy: str) -> bool:
			try:
 				# Realizar una solicitud a través del proxy
				session = requests.session()
				session.proxies = {"http": proxy}
				session.timeout = self.timeout

				response = session.get(self.url)

				# Verificar el código de estado de la respuesta
				if response.status_code == 200:
					self.working_proxies.append(proxy)
					logging.info(f"Proxy funcionando: {proxy}")
					print(Fore.GREEN + f"Proxy funcionando: {proxy}")
				else:
					logging.info(f"Proxy no funcionando: {proxy}")
					print(Fore.RED + f"Proxy no funcionando: {proxy}")

			except Exception as e:
				# Manejar errores de conexión al proxy
				logging.error(f"Error al verificar el proxy {proxy}: {e}")
				return False

		checked_proxies = []
		count = 0
		num_checks = 200

		while count < len(self.proxies):
			# Seleccionar un lote de proxies para verificar
			proxies_to_check = self.proxies[count:count + num_checks]

			# Crear un ThreadPoolExecutor con el número deseado de hilos
			with ThreadPoolExecutor() as executor:
				# Ejecutar la función check para cada proxy en el lote
				results = list(executor.map(check, proxies_to_check))

				# Agregar los resultados a la lista de proxies verificados
				checked_proxies.extend(zip(proxies_to_check, results))

			# Incrementar el contador para el siguiente lote de proxies
			count += num_checks
		return self.working_proxies
  

  
