import requests
import json
import subprocess
import sys

KEY = '50727327-bd98892090324aaa696e307bc'

URL = 'https://pixabay.com/api'

#search_term = 'coal mining'
#search_term = sys.argv[1]
search_term = sys.stdin.read().strip()

params = {
	'key': KEY,
	'q': search_term,
	'image_type': 'photo',
}

response = requests.get(URL, params=params)
newrl = response.json()['hits'][0]['pageURL']

#subprocess.run(['xdg-open', newrl])
print(newrl)
