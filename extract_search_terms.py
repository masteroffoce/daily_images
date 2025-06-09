import requests
import json
import sys

#holiday = "Coal Miner's Day (India)"
holiday = sys.stdin.read().strip()
data = {
	"model": "llama3.2:3b",
	"prompt": f"You're an API that's heping me look for images in a database. I want an image that fits this holiday: {holiday}. Output max two words. The words should lead to a fitting image. Only output the search term. No quotataion marks, nothing more than the word(s). The image should be suitable as a background (no persons, no professions; preferably workplaces). OUTPUT MAX TWO WORDS!!! Under the output, make two newlines and motivate your choice.",
	"stream": False,
	"options": {
		"num_predict": -1,
		"seed": 0,
		"temperature": 0.7
	}
}

url = "http://localhost:11434/api/generate"

response = requests.post(url,json=data)

response_json = json.loads(response.text)

answer = response_json['response'] 

holiday = answer.partition('\n')[0]

if '-m' in sys.argv or '--motivate' in sys.argv:
	print(answer)
else:
	print(holiday)
