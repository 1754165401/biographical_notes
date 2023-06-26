import requests
from bs4 import BeautifulSoup
from settings import headers_list,proxies_list
import random


def links_get():
    url = "https://ganzhou.anjuke.com/?from=AJK_Web_City"
    proxies = random.choice(proxies_list)
    headers = random.choice(headers_list)
    response = requests.get(url,headers=headers,proxies=proxies)

    main_soups = BeautifulSoup(response, 'html.parser')
    elements = main_soups.find_all(class_="areaheight")
    result_list = []
    for index, element in enumerate(elements):
        item_dict = {}
        title_element = element.find('h1')
        if title_element:
            title = title_element.get_text()
            item_dict['title'] = title
        links = element.find_all('a')

        for link in links:
            href = link['href']
            if index == 0:
                result_list.append(href)

    return result_list