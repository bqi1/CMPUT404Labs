import requests

# print(requests.__version__)

# r = requests.get('https://www.google.com')
r = requests.get('https://raw.githubusercontent.com/bqi1/CMPUT404Labs/master/Script.py')
print(r.text)