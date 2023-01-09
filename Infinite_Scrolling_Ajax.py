import requests
from bs4 import BeautifulSoup
from requests import Session
import time,random
'''Пример парсинга бесконечного скрола Ajax запросов, тип контента text/HTML'''

base_url = 'https://scrapingclub.com/exercise/list_infinite_scroll/'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

def main(base_url):
    s = Session()
    s.headers.update(headers)

    count = 1
    pagination = 0
    while True:

        if count > 1:
            url = base_url + '?page='+ str(count)
        else:
            url = base_url

        response = s.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        if count == 1:
            pagination = int(soup.find('ul', class_="pagination invisible").find_all('li', class_="page-item")[-2].text)
        cards = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")
        for card in cards:
            name = card.find('h4', class_="card-title").text
            cost = card.find('h5').text
            print(name,cost)
            print(count)
        time.sleep(random.choice([5,7,9]))
        if count == pagination:
            break

        count+=1
        # with open('data.html','w', encoding='utf-8') as r:
        #     r.write(response.text)


main(base_url)