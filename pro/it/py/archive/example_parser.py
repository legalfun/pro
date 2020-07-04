import os
import re

import requests
from bs4 import BeautifulSoup

# заголовки, что бы сайт думал что используется такой браузер
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

# сам запрос 
r = requests.get('https://vkusvill.ru/goods/mozhno-v-post/', headers=headers)

# берем ответ сайта r.text и находим теги 'a' с классом 'ProductCard__link' и выводим в цикле текст каждого
soup = BeautifulSoup(r.text, 'lxml')
products = soup.find_all('a', class_='ProductCard__link')
for product in products:
	print(product.text)