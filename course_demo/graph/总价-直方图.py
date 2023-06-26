import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_path = 'C:\\Windows\\Fonts\\STZHONGS.TTF'
font_prop = FontProperties(fname=font_path)

data = pd.read_csv('汇总2(层高、建筑年份无则为空).csv')

data['总价格'] = data['总价格'].str.replace('万', '').astype(float)

price_ranges = [0, 50, 100, 200, 300, float('inf')]
labels = ['50万以下', '50-100万', '100-200万', '200-300万', '300万以上']

data['价格区间'] = pd.cut(data['总价格'], bins=price_ranges, labels=labels, right=False)
grouped_data = data.groupby('价格区间').size()


plt.rcParams["font.family"] = font_prop.get_name()

plt.figure(figsize=(10, 6), dpi=150)

plt.bar(grouped_data.index, grouped_data.values)
plt.xlabel('价格区间', fontproperties=font_prop, fontsize=12)
plt.ylabel('数量', fontproperties=font_prop, fontsize=12)
plt.title('总价直方图', fontproperties=font_prop, fontsize=14)

plt.savefig('总价直方图.png', dpi=300, bbox_inches='tight', pad_inches=0.1)

plt.show()
