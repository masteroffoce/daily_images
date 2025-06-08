import re

ex = "hel[23]loo."

ex = re.sub(r"\[[0-9]+\]","",ex)

print(ex)
