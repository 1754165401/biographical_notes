import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_path = 'C:\\Windows\\Fonts\\STZHONGS.TTF'
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

df = pd.read_csv('汇总2(层高、建筑年份无则为空).csv')


room_type_column = df['房型']

room_counts = room_type_column.apply(lambda x: int(x.split('室')[0])).value_counts()
hall_counts = room_type_column.apply(lambda x: int(x.split('厅')[0].split('室')[-1])).value_counts()
bathroom_counts = room_type_column.apply(lambda x: int(x.split('卫')[0].split('厅')[-1])).value_counts()

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].bar(room_counts.index, room_counts.values)
axes[0].set_xlabel('室')
axes[0].set_ylabel('出现次数')
axes[0].set_title('房型属性统计（室）')

axes[1].bar(hall_counts.index, hall_counts.values)
axes[1].set_xlabel('厅')
axes[1].set_ylabel('出现次数')
axes[1].set_title('房型属性统计（厅）')

axes[2].bar(bathroom_counts.index, bathroom_counts.values)
axes[2].set_xlabel('卫')
axes[2].set_ylabel('出现次数')
axes[2].set_title('房型属性统计（卫）')

plt.tight_layout()
plt.savefig('房型直方图.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()
