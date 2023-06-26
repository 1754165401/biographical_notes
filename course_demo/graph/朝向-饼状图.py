import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

font_path = 'C:\\Windows\\Fonts\\STZHONGS.TTF'
font_prop = font_manager.FontProperties(fname=font_path)

data1 = pd.read_csv("章江新区.csv")
data2 = pd.read_csv("章贡.csv")
data3 = pd.read_csv("南康.csv")
data4 = pd.read_csv("开发.csv")

orientation1 = data1["朝向"]
orientation2 = data2["朝向"]
orientation3 = data3["朝向"]
orientation4 = data4["朝向"]

orientation_counts1 = orientation1.value_counts()
orientation_counts2 = orientation2.value_counts()
orientation_counts3 = orientation3.value_counts()
orientation_counts4 = orientation4.value_counts()

plt.rcParams["font.family"] = font_prop.get_name()

fig, axes = plt.subplots(2, 2, figsize=(12, 8), dpi=150)

axes[0, 0].set_title("朝向 - 章江新区")
orientation_counts1.plot(kind="pie", autopct="%1.1f%%", ax=axes[0, 0])
axes[0, 0].set_ylabel('')

axes[0, 1].set_title("朝向 - 章贡")
orientation_counts2.plot(kind="pie", autopct="%1.1f%%", ax=axes[0, 1])
axes[0, 1].set_ylabel('')

axes[1, 0].set_title("朝向 - 南康")
orientation_counts3.plot(kind="pie", autopct="%1.1f%%", ax=axes[1, 0])
axes[1, 0].set_ylabel('')

axes[1, 1].set_title("朝向 - 开发")
orientation_counts4.plot(kind="pie", autopct="%1.1f%%", ax=axes[1, 1])
axes[1, 1].set_ylabel('')


plt.tight_layout()
plt.savefig("朝向分析.png", dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.savefig('朝向饼状图.png', dpi=300, bbox_inches='tight', pad_inches=0.1)
plt.show()
