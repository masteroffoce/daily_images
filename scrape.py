import requests
from bs4 import BeautifulSoup

url = 'http://en.wikipedia.org/wiki/May_4'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

heading = soup.find('h2', string='Holidays and observances')

ul = heading.find_next('ul')

holidays = []
if ul:
	for li in ul.find_all('li'):
		holidays.append(li.text.strip())

print(holidays)
