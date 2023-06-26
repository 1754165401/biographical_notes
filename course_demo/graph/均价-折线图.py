import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm



font_path = 'C:\\Windows\\Fonts\\STZHONGS.TTF'
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

folder_path = os.getcwd()

file_list = os.listdir(folder_path)
csv_files = [file for file in file_list if file.endswith('.csv')]

averages = []
file_names = []

for file in csv_files:
    file_path = os.path.join(folder_path, file)

    df = pd.read_csv(file_path)

    df['单位面积价格'] = df['单位面积价格'].str.extract('(\d+)')
    df['单位面积价格'] = pd.to_numeric(df['单位面积价格'])

    average_price = df['单位面积价格'].mean()

    averages.append(average_price)
    file_names.append(os.path.splitext(file)[0])


plt.plot(file_names, averages, marker='o', linestyle='-', color='b')
plt.xlabel('赣州市各区均价折线图', fontproperties=font_prop, fontsize=14)
plt.ylabel('单位面积价格平均值（元/㎡）', fontproperties=font_prop, fontsize=12)
plt.title('每个区单位面积价格平均值', fontproperties=font_prop, fontsize=12)
plt.xticks(rotation=45, fontsize=8)

for i, j in zip(file_names, averages):
    plt.text(i, j, f'{j:.2f}', ha='center', va='bottom', fontsize=8)

plt.savefig('均价折线图.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()
