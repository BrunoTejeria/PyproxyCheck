
class Config:
  def __init__(self):
    pass
  def logging_config(self) -> bool:
    try:
      logging.basicConfig(filename='logging.log', level=logging.INFO)
      return True
    except:
      return False
