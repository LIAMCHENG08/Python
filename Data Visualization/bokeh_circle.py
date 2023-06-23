from bokeh.plotting import figure, show
import numpy as np

# 設定畫布
p = figure(plot_width=600, plot_height=400, x_range=[0.5,3], y_range=[0,7])

# 繪製不同樣式散點圖
p.circle_cross(1, 1, size=30, alpha=0.5, legend_label='circle_cross')
p.asterisk(1, 2, size=30, alpha=0.5, legend_label='asterisk')
p.circle_x(1, 3, size=30, alpha=0.5, legend_label='circle_x')
p.cross(1, 4, size=30, alpha=0.5, legend_label='cross')
p.diamond_cross(1, 5, size=30, alpha=0.5, legend_label='diamond_cross')
p.diamond(1, 6, size=30, alpha=0.5, legend_label='diamond')
p.inverted_triangle(2, 1, size=30, alpha=0.5, legend_label='inverted_triangle')
p.square(2, 2, size=30, alpha=0.5, legend_label='square')
p.square_cross(2, 3, size=30, alpha=0.5, legend_label='square_cross')
p.square_x(2, 4, size=30, alpha=0.5, legend_label='square_x')
p.triangle(2, 5, size=30, alpha=0.5, legend_label='triangle')
p.x(2, 6, size=30, alpha=0.5, legend_label='x')

# 顯示圖表
show(p)
