import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://www.nike.com/t/air-jordan-3-retro-mens-shoes-bPRc5V/DN3707-160").content
price = BeautifulSoup(r, 'html.parser')
d = price.findAll("div", {"data-test":"product-price"})

print(d)
