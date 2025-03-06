import requests

url = "http://numbersapi.com/43"

data = requests.get(url)

print(data.text)
