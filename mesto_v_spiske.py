import requests
from bs4 import BeautifulSoup
import json
import sys

with open('config.json', encoding="utf8") as config_file:
    try:
        config = json.load(config_file)
    except json.decoder.JSONDecodeError: #открываем файл конфигурации
        print('С файлом config.json что-то не так.')
        sys.exit()

link = config['link']

site = requests.get(link)

soup = BeautifulSoup(site.text, 'html.parser')

name = config['name']

place = soup.find_all('td', text = name)

num = config['num']

all_info = place[num-1].parent.find_all('td')

print(all_info[3].text)


