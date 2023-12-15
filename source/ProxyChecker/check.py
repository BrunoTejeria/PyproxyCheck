import logging
import requests
from concurrent.futures import ThreadPoolExecutor

class Check():
	def __init__():
		pass


	def check_proxies(self, headers, url, proxies, ssl):
		self.headers: dict = headers
		self.proxies: list = proxies
		self.url: str = url
		self.ssl: str = ssl
		def check(proxy):
			try:
				# Realizar una solicitud a través del proxy
				if self.ssl == True:
					response = requests.get("https://google.com", proxies={"http": self.proxies}, timeout=self.timeout, headers=self.headers)
				else:
					response = requests.get("https://youtube.com", proxies={"http": self.proxies}, timeout=self.timeout, headers=self.headers)


				# Verificar el código de estado de la respuesta
				if response.status_code == 200:
					logging.info(f"proxy working: {proxy}")
					return True
				else:
					logging.info(f"proxy not working: {proxy}")
					return False

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

		# Imprimir los resultados
		for proxy, result in checked_proxies:
			if result:
				print(f"Proxy {proxy} está funcionando correctamente.")
			else:
				print(f"Error al verificar el proxy {proxy}.")
		return checked_proxies
  

  
