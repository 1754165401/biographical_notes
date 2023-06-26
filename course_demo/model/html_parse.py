from bs4 import BeautifulSoup
import csv

def parse(htmls):
    i = 0
    for html in htmls:
        soup = BeautifulSoup(html, 'html.parser')
        list_main_section = soup.find('section', class_='list-main')
        list_sections = list_main_section.find_all('section', class_='list')
        name_list = ['章江新区', '章贡', '开发', '赣县', '南康', '站北', '瑞金', '信丰' '于都', '宁都', '龙南', '会昌', '崇义',
            '上犹', '兴国', '大余', '安远', '寻乌', '定南', '全南']

        filename = f'{name_list[i]}.csv'
        i = i + 1

    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['小区', '地址', '房型', '面积', '朝向', '层高', '建造年份', '单位面积价格', '总价格', '备注'])

        for section in list_sections:
            property_divs = section.find_all('a', class_='property-ex')

            for div in property_divs:
                property_info = []
                neighbourhood = div.find('p', class_='property-content-info-comm-name')
                property_info.append(neighbourhood.text.strip())
                address = div.find('p', class_='property-content-info-comm-address')
                property_info.append(address.text.strip())

                for p_tag in div.find('div', class_='property-content-info').find_all('p',class_='property-content-info-text'):
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