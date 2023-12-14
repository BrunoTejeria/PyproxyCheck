import logging



class Text:
  def __init__(self):
    pass



  def read_all(self, file: str) -> str:
    """
    Funcion para abrir docuento de texto y leerlo por completo
    """
    try:
      with open(file, "r", "UTF-8") as f:
        logging.INFO(f"Archivo abierto | Archivo: {file}")
        return f.read()
    except Exception as e:
      logging.error(f"Error al leer archivo: Error: {e}")



  def read_lines(self, file: str) -> list:
    pass

  def write(self, file: str, content: str) -> bool:
    pass

  def write_lines(self, file: str, content: list) -> bool:
    pass
