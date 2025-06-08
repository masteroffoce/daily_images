import requests
import json
import subprocess
import sys
import os

result = subprocess.run(['cat', os.path.expanduser('~/pixabay_api_key')], capture_output = True)
KEY = result.stdout.strip()

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
newrl = response.json()['hits'][0]['largeImageURL']

#subprocess.run(['xdg-open', newrl])
print(newrl)
