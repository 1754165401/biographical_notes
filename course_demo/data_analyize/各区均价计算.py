import csv

area_prices = {}

with open('汇总2(层高、建筑年份无则为空).csv', 'r', newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        address = row['地址']
        price = float(row['单位面积价格'].split('元/㎡')[0])

        area = address[:2]

        if area in area_prices:
            area_prices[area].append(price)
        else:
            area_prices[area] = [price]

average_prices = []
for area, prices in area_prices.items():
    average_price = round(sum(prices) / len(prices), 1)
    average_prices.append({'地区': area, '均价': average_price})

with open('各区平均房价.csv', 'w', newline='', encoding='utf-8-sig') as file:
    fieldnames = ['地区', '均价']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(average_prices)
