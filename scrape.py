import requests
from bs4 import BeautifulSoup
import re
import sys

#Get chosen date
date = sys.argv[1]

#Find the Wikipedia site for the chosen date
url = f'http://en.wikipedia.org/wiki/{date}'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

heading = soup.find('h2', string='Holidays and observances')

ul = heading.find_next('ul')

#Fill the list holidays with all holidays and observances for the chosen date
holidays = []
if ul:
	for li in ul.find_all('li'):
		holidays.append(li.text.strip())


holiday_lists = []

#Filter the holidays with lists (like christian feast days)
for holiday in holidays:
	if '\n' in holiday:
		holiday_lists.append(holidays.index(holiday))

#Since the heading for small lists includes the whole list, look for the last part
holiday_lists_ends = []
for index in holiday_lists:
	end = holidays[index][-10:]
	i = index
	i += 1
	while not holidays[i][-10:] == end:
		i += 1
	holiday_lists_ends.append(i)

#Set the holidays that are going to be removed to 0 as a placeholder
for i  in range(len(holiday_lists)):
	for j in range(holiday_lists[i], holiday_lists_ends[i] + 1):
		holidays[j] = 0

#Remove every instance of 0
while 0 in holidays:
	holidays.remove(0)

#Remove sources (Who needs thems anyways?)
for i in range(len(holidays)):
	holidays[i] = re.sub(r'\[[0-9]+\]','',holidays[i])

#Print the list
for holiday in holidays:
	print(holiday)
