import requests

url = 'https://api.pwnedpasswords.com/range/' + '9C9BB'
res = requests.get(url)
print(res)
