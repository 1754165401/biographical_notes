import os
import csv
from bs4 import BeautifulSoup


current_directory = os.getcwd()

html_files = [file for file in os.listdir(current_directory) if file.endswith('.html')]

with open('章江新区.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['小区', '地址', '房型', '面积', '朝向', '层高', '建造年份', '单位面积价格', '总价格', '备注'])

    for html_file in html_files:
        file_path = os.path.join(current_directory, html_file)


        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')

            list_main_section = soup.find('section', class_='list-main')

            list_sections = list_main_section.find_all('section', class_='list')

            for section in list_sections:
                property_divs = section.find_all('a', class_='property-ex')

                for div in property_divs:
                    property_info = []

                    neighbourhood = div.find('p', class_='property-content-info-comm-name')
                    property_info.append(neighbourhood.text.strip())

                    address = div.find('p', class_='property-content-info-comm-address')
                    property_info.append(address.text.strip())

                    for p_tag in div.find('div', class_='property-content-info').find_all('p',
                                                                                          class_='property-content-info-text'):
                        text = p_tag.get_text(strip=True)
                        property_info.append(text)

                    for price_tag in div.find_all('div', class_='property-price'):
                        first_text = price_tag.find('p', class_='property-price-average').get_text(strip=True)
                        property_info.append(first_text)

                        second_text = price_tag.find('p', class_='property-price-total').get_text(strip=True)
                        property_info.append(second_text)

                    note = div.find('div', class_='property-content-title').get_text(strip=True)
                    property_info.append(note)

                    writer.writerow(property_info)

print("数据已保存到 properties.csv 文件中。")
