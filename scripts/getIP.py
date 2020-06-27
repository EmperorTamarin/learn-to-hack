import requests

url = "http://icanhazip.com"
response = requests.get(url)
content = response.text
print(content)

