import logging


class Text:
    def __init__(self):
        pass

    def read_all(self, file: str) -> str:
        """
        Function:
        - Leer documento de texto por completo.

        Parameters:
        - file (str): Ruta del archivo a leer.

        Returns:
        - str or None: String del contenido del archivo o None si hay un error.

        """
        try:
            with open(file, "r", encoding="utf-8") as f:
                logging.info(f"Archivo abierto | Archivo: {file}")
                return f.read()

        except FileNotFoundError as e:
            logging.error(f"No se encontró el archivo {file}: {e} | File: {__file__}")
            return None

        except Exception as e:
            logging.error(f"No se pudo leer el archivo: {e} | File: {__file__}")
            return None

    def read_lines(self, file: str) -> list:
        """
        Function:
        - Leer lineas de documento de texto.

        Parameters:
        - file (str): Ruta del archivo a leer.

        Returns:
        - list or None: Lista de líneas del archivo o None si hay un error.

        """
        try:
            with open(file, "r", encoding="utf-8") as f:
                logging.info(f"Archivo abierto | Archivo: {file}")

                # Retorna una lista de líneas del archivo
                return f.readlines()

        except FileNotFoundError as e:
            logging.error(f"No se encontró el archivo {file}: {e} | File: {__file__}")
            return None

        except Exception as e:
            logging.error(f"No se pudo leer el archivo: {e} | File: {__file__}")
            return None

    def write(self, file: str, content: str, mode="w") -> bool:
        """
        Function:
        - Escribir un str en un archivo

        Parameters:
        - file (str): Ruta del archivo a leer.
        - content (str): Contenido el cual se escribirá en el archivo.
        - mode (str) -> ["w","a"]: Modo de escritura del archivo que solo puede ser write o append.

        Returns:
        - True or False: Si se completa la función exitosamente retorna True, si no retorna False.

        """

        # Chequear si el modo el write o append.
        options = ["w", "a"]
        if mode is not None and mode not in options:
            raise ValueError(f"La opción proporcionada no es válida. Debe ser {options}")


        try:
            with open(file=file, mode=mode, encoding="utf-8") as f:
                f.write(content)
                return True
        except FileNotFoundError as e:
            return False
        except Exception as e:
            return False

    def write_lines(self, file: str, content: list) -> bool:
        pass
