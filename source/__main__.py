from main.Files.text import Text
from config import Config


class Root(Text, Config):
    def __init__(self):

        self.read_all("ggg.txt")


main = Root()

