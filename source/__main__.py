from main.Files.text import Text
from config import Config
from ProxyChecker.check import Check

class Root(Text, Config, Check):
    """
    Clase principal que hereda funcionalidades de las clases Text, Config y Check.


    Métodos
    -------
    __init__()
        Constructor de la clase. Inicializa la configuración del logger y lee la configuración del archivo.

    Ejemplo
    -------
    root_instance = Root()
    """

    def __init__(self):
        """
        Constructor de la clase.
        """

        # Verificar y configurar el logging
        if self.logging_config():
            # Leer la configuración desde el archivo
            if self.read_config():
                # Realizar la verificación de proxies
                self.check_proxies(
                    url=self.url,
                    ssl=self.ssl,
                    headers=self.headers,
					proxies=self.read_lines(self.file)
                )

# Crear una instancia de la clase Root
main = Root()
