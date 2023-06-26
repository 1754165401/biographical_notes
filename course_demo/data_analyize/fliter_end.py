import pandas as pd


data = pd.read_csv("汇总表.csv", encoding='utf-8-sig')

filtered_data = data[data["建造年份"].notnull()]


empty_remark_rows = data[data["备注"].isnull()]
for index, row in empty_remark_rows.iterrows():
    data.loc[index, "建造年份":"备注"] = data.loc[index, "建造年份":"备注"].shift(1)


rows_with_wan = data[data["单位面积价格"].str.contains("万", na=False)]
data.loc[rows_with_wan.index, ["总价格", "备注"]] = data.loc[rows_with_wan.index, ["单位面积价格", "总价格"]].values
data.loc[rows_with_wan.index, "单位面积价格"] = data.loc[rows_with_wan.index, "层高"]
data.loc[rows_with_wan.index, "层高"] = ""

data.to_csv("汇总2(层高、建筑年份无则为空).csv", encoding='utf-8-sig', index=False)