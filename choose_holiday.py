import requests
import json
import sys

holidays = sys.stdin.read().strip()

data = {
        "model": "llama3.2:3b",
        #"prompt": f"You're an API that's heping me look for images in a database. I want an image that fits this holiday: {holiday}. Output max two words. The words should lead to a fitting image. Only output the search term. No quotataion marks, nothing more than the word(s). The image should be suitable as a background (no persons, no professions; preferably workplaces). OUTPUT MAX TWO WORDS!!!",
	"prompt": f"You're an API that's helping me choose one of these holidays. You're supposed to output the name of the holiday. Choose the holiday which is 1. the most relevant and 2. easy to find an image for. Here is the list: {holidays}. REMEMBER: YOU'RE AN API. ONLY OUTPUT THE NAME OF THE HOLIDAY. You're going to help me search for an image, so just choose the best fitting celebreation.",
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

print(response_json['response'])
