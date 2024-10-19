import requests
resp = requests.get('https://bilibili.com/')
html = resp.text
print(html)