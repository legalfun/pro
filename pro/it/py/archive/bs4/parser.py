# [Олег Молчанов] Парсинг сайтов на Python_ Приемы работы с библиотекой BeautifulS
# 1. Elements & siblings
# 2. By CSS data finding
# 3. No selector data finding
# 4. By atribute data finding
# 5. By text tagg finding (content)


from bs4 import BeautifulSoup
import re


def main():
	html = open('index.html').read()
	soup = BeautifulSoup(html, 'lxml')

	# regexp = r'\d{2}.\d{2}.\d{4}' # for data finding

	# regexp = r'^\w\-\d$' # regular expression usage

	# div = soup.find('div', class_='links')
	# links = div.find_all('a')
	# div = soup.find('div', {'class': 'links'})
	# div = soup.find_all('a')
	# parent = find_parent()		# find like
	# parents = find_parents()	# find_all like
	# div = soup.find('h1').find_parent('div', class_='two')
	# text = soup.find('h1').next_sibling
	# text = soup.find('h1').previous_sibling
	# a = soup.find('a', href=re.compile('ya.ru'))
	# url = a.get('href')
	# div = soup.find('h1').parent
	# n = div.get('data-set')
	a = soup.find('div', text=re.compile(regexp))
	print(a)
	# print(n)
	# print(a)
	# print(text)
	# print(div)
	# print(links)
	# for a in div:
	# 	link = a.get('href')
	# 	print(link)





if __name__ == '__main__':
	main()