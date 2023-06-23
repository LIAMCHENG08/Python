from bokeh.plotting import figure,show
import numpy as np
x=np.arange(5)
y=x**2

p=figure()

p.line(x,y)

show(p)
#%%
from bokeh.plotting import figure,show
import numpy as np

x=np.arange(1,11)
y1=x*2
y2=x*4
y3=x*6
y4=x*8
y5=x*10

p=figure()

p.line(x,y1,line_dash='solid',line_width=5,line_color='#D93F1A')

show(p)
#%%
from bokeh.plotting import figure,show
fruits=['apple','banana','grapes']
counts=[5,3,2]
color=['#F03329','#FA9A00','#FAE50E']

p=figure(x_range=fruits,title='水果數')

p.vbar(x=fruits,top=counts,width=0.6,fill_color=color,line_color=color)

p.xgrid.grid_line_color=None

p.y_range.start=0

show(p)
#%%
from bokeh.plotting import figure,show
import numpy as np

x=np.random.randint(1,51,10)
y=np.random.randint(1,51,10)
z=np.random.randint(1,51,10)

p=figure()

p.circle(x,x,size=20,color='#8100FA',alpha=0.5)
p.square(x,y,size=10,color='#12FA9D')

show(p)

#%%
from bokeh.plotting import figure,show

x=0
y=0
radius=1

start_angle=[0,1.8,2.5,3.7,5.6]
end_angle=[1.8,2.5,3.7,5.6,0]
color=['blue','green','yellow','red','violet']

p=figure()

p.wedge(x,y,radius,start_angle,end_angle,color=color)

show(p)




















