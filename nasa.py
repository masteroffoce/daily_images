import requests
import json
import subprocess

api_key = 'e8p0rp6XjpoBCVKaz2YAdKu8z1T2JgS3bNGTSRLg'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

response = requests.get(url)

if response.status_code == 200:
	data = response.json()

	image_url = data['url']
	explanation = data['explanation']
	title = data['title']

	print(f'title: {title}')
	print(f'explanation: {explanation}')
	print(f'url: {image_url}')
	subprocess.run( ['xdg-open', image_url])
else:
	print(f'Error: {response.status_code}')
