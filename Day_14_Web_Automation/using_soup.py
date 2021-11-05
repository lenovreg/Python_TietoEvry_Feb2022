import requests
from bs4 import BeautifulSoup as bs

url = "https://mdn.github.io/beginner-html-site/"

response = requests.get(url)
print(response.status_code)  # 200 would be good 404 would be bad

print(response.text[:500])  # first 500 characters
