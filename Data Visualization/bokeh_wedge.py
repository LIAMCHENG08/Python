from bokeh.plotting import figure, show
from math import pi
import pandas as pd
from bokeh.transform import cumsum
from bokeh.palettes import Category20c

# 設定資料
x = {"apple" : 15,
     "grapes" : 30,
     "strawberries" : 45,
     "pears" : 10
     }

# 將x做成dataframe，先重置index，再重新命名欄名：第一欄為水果種類，第二欄是水果數量
data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'fruits'})
# 計算資料的權重
data['angle'] = data['value']/data['value'].sum() * 2*pi
# 設定圓餅顏色
data['color'] = Category20c[len(x)]


# 設定畫布
p = figure()

# 繪製圓餅圖
p.wedge(x=0, y=0, radius=0.5, 
        start_angle=cumsum('angle', include_zero=True),
        end_angle=cumsum('angle'),
        source=data,
        fill_color="color")

# 顯示圖表
show(p)

"""
官網提供的顏色說明
https://docs.bokeh.org/en/3.0.2/docs/reference/palettes.html

include_zero=True的說明
https://docs.bokeh.org/en/2.4.2/docs/reference/models/expressions.html
"""