from main.Files.text import Text
from config import Config
from ProxyChecker.check import Check


class Root(Text, Config, Check):
	def __init__(self):
		self.logging_config()
		self.url = "https://google.com"
		self.ssl = False
		self.timeout = 2
		self.resultfile = "data/result.txt"
		self.proxies = self.read_lines("proxies.txt")
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
		}
		print(self.write_lines(self.resultfile, self.check_proxies(self.headers, self.url, self.proxies, self.ssl)))


main = Root()

