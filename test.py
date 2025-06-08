import subprocess
import os

filepath = os.path.expanduser('~/pixabay_api_key')
print(filepath)
result = subprocess.run(['cat', filepath], capture_output = True, text = True)

KEY = result.stdout

print(KEY)
