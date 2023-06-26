from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType

# 准备数据
county_prices = {
    '上犹县': 5816.8,
    '于都县': 7152.2,
    '会昌县': 5193.9,
    '信丰县': 6898.4,
    '全南县': 7131.7,
    '兴国县': 6243.6,
    '南康区': 7591.5,
    '大余县': 4568.6,
    '宁都县': 5316.3,
    '安远县': 4081.1,
    '定南县': 4218.6,
    '寻乌县': 5665.5,
    '崇义县': 5609.6,
    '开发区': 10353.9,
    '瑞金市': 6358.9,
    '石城县': 5521.8,
    '章贡区': 8515.6,
    '章江新区': 14055.0,
    '赣县区': 7896.9,
    '龙南县': 7368.7
}

# 获取最低和最高房价
min_price = min(county_prices.values())
max_price = max(county_prices.values())

# 定义颜色范围和对应的房价区间
color_ranges = [
    {"min": min_price, "max": max_price * 0.4, "color": "#D7E8FF"},
    {"min": max_price * 0.4, "max": max_price * 0.6, "color": "#A4C2FF"},
    {"min": max_price * 0.6, "max": max_price * 0.8, "color": "#6F9EFF"},
    {"min": max_price * 0.8, "max": max_price, "color": "#227EFF"},
]

# 创建地图实例
map_chart = Map(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width='1000px', height='800px'))

# 设置地图参数
map_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="赣州市各县房价分布"),
    visualmap_opts=opts.VisualMapOpts(
        is_piecewise=True,
        pieces=color_ranges,
        pos_top="middle",
    ),
)

# 添加数据和标签
data = [(k, v) for k, v in county_prices.items()]
map_chart.add("", data, maptype="赣州")
map_chart.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

# 渲染图表并保存到文件
map_chart.render("ganzhou_house_prices.html")
