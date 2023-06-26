import os
import csv

output_file = "汇总表.csv"
header = ['小区', '地址', '房型', '面积', '朝向', '层高', '建造年份', '单位面积价格', '总价格', '备注']
with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    print(f"已创建汇总CSV文件 '{output_file}'")

for file_name in os.listdir(os.getcwd()):
    file_path = os.path.join(os.getcwd(), file_name)

    if os.path.isfile(file_path) and file_name.lower().endswith(".csv"):
        if file_name == output_file:
            continue

        with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                with open(output_file, 'a', newline='', encoding='utf-8-sig') as output_csv:
                    writer = csv.writer(output_csv)
                    writer.writerow(row)

        print(f"已合并文件 '{file_name}' 到汇总CSV文件")

print("完成CSV文件合并操作。")
