import requests

url = 'https://www.w3schools.com'

res = requests.get(url)

with open('w3school_home.html', mode='wt', encoding='utf8') as f:
    f.write(res.text)

with open('demo.txt', 'wt', encoding='utf8') as f:
    f.write('demo')
