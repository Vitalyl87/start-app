import requests

data = requests.get("https://ya.ru")

print(data.status_code)
print(data.headers)
print('hello!')
