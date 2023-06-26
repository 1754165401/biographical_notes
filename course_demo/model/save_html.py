import random
import time
import requests
from settings import headers_list,proxies_list


def save_html_sources(links):
    html_sources = []
    for link in links:
        proxies = random.choice(proxies_list)
        headers = random.choice(headers_list)
        response = requests.get(link,headers=headers,proxies=proxies)
        html_source = response.text

        html_sources.append(html_source)
        time.sleep(20)

    return html_sources