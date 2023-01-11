import requests,xlsxwriter
from bs4 import BeautifulSoup
from requests import Session
import time,random
import json
'''Пример парсинга бесконечного скрола Ajax запросов, тип контента text/HTML'''

base_url = 'https://scrapingclub.com/exercise/list_infinite_scroll/'

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}

list_card_url = []  #используется для парсинга каждой страницы
shop =dict()
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

        response = s.get(url) #получаем html страницы
        soup = BeautifulSoup(response.text, 'lxml') #разбираем информацию парсером

        if count == 1:
            pagination = int(soup.find('ul', class_="pagination invisible").find_all('li', class_="page-item")[-2].text)
        cards = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")
        for card in cards:  # получаем нужные ссылки
            shop[card.find('h4', class_='card-title').find('a').text] = [card.find('h5').text]
            card_url = 'https://scrapingclub.com' + card.find('a').get('href')
            resp = s.get(card_url)
            new_soup = BeautifulSoup(resp.text,'lxml')
            shop[card.find('h4', class_='card-title').find('a').text].append(new_soup.find('p', class_='card-description').text)
            list_card_url.append(card_url)
            # time.sleep(random.choice([3,2,1]))
        if count == pagination:
            break

        count+=1
    print(shop)
    for i,j in shop.items():
        print(f'{i}: {j[0]}, {j[1]}')

main(base_url)


# код для записи полученной информации в отдельный файл, но прежде полученную инфу shop нужно переделать в тип tuples
# def writer(main):
#     book = xlsxwriter.Workbook(r"F:pythonProject\test_project\parsing_web")
#     page = book.add_worksheet("товар")
#
#     row = 0
#     column = 0
#
#     page.set_column("A:A",20)
#     page.set_column("B:B",20)
#     page.set_column("C:C",50)
#
#     for item in writer(main):
#         page.write(row, column, item[0])
#         page.write(row, column, item[0])
#         page.write(row, column, item[0])
#         row+=1
#
#     book.close()
#
# writer(if __name__ == '__main__':
#     )