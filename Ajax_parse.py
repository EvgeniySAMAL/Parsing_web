import requests
'''Пример парсинга Ajax запросов, тип контента json'''


url = 'https://scrapingclub.com/exercise/ajaxdetail/'

response = requests.get(url).json()

print(response['title'])
print(response['price'])
print(response['description'])
print(response)

