
import sqlite3


import requests
import json
from bs4 import BeautifulSoup

class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'




html = requests.get(f'https://www.afisha.uz').text

soup = BeautifulSoup(html, 'html.parser')

articles = soup.find_all('h3')

json_data = []

for article in articles:
    title = article.find('a').text
    print(Style.MAGENTA + title)

teasers = soup.find_all('div', class_='item-3')
for teaser in teasers:
    inf = teaser.find('p', class_='desc').text
    img = teaser.find('p', class_='desc').text
    print(Style.GREEN + inf)
    print(Style.BLUE + img)

    json_data.append({
            'title':title,
            'teaser':inf,
            'image link':img
    })





with open('afisha.json', mode='w', encoding='UTF-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)



database = sqlite3.connect('ls7_homework.db')
cursor = database.cursor()
cursor.execute('''
    INSERT INTO json(title, inf)
    VALUES (?,?)
    ''', (title, inf))
database.commit()
database.close()