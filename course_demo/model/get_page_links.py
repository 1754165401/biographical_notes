import time

import requests
from settings import proxies_list,headers_list
import random
def get_page_links(links):
    page_links = []
    page = 1
    for url in links:
        headers = random.choice(headers_list)
        proxies = random.choice(proxies_list)
        while True:
            page_link = f"{url}p{page}"
            response = requests.get(page_link,headers=headers,proxies=proxies,allow_redirects=False)

            if response.status_code == 301:
                page_links.append(page_link)
                page += 1
            else:
                break
            time.sleep(20)
    return page_links
