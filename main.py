import requests
from bs4 import BeautifulSoup
import html5lib

url = "https://www.amazon.com/Samsung-Electronics-Unlocked-Smartphone-Long-Lasting/dp/B08BX7N9SK/ref=sr_1_3?crid=3KN9LN7EDRN2X&dchild=1&keywords=iphone%2B12%2Bpro%2Bmax&qid=1611168296&sprefix=iphone%2Caps%2C629&sr=8-3&th=1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#title = soup.find(id='title').get_text()

price = soup.find(id='priceblock_ourprice').get_text()

print(price.strip())
#print (soup.prettify())