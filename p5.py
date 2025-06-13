#data visualization 3
import pandas as pd
import numpy as np

from numpy.random import randn
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb
from seaborn import set_style

rcParams['figure.figsize']=10,10

sb.set_style('whitegrid')

x=range(1,11)
y=[1,2,3,4,0,5,4,3,2,1]
# plt.bar(x,y)

wide = [0.5,0.5,0.5,0.9,0.9,0.9,0.5,0.5,0.5,0.5]
color='salmon'

plt.bar(x,y,width=wide, color=color, align='center')  #width--> setting width of each bar , if width=0.5 --> every bars width is set to 0.5
plt.show()
#-------------------------------------

address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
mpg=cars['mpg']

df=cars[['cyl','mpg','wt']]
df.plot()
plt.show()

color_theme=['darkgray','lightsalmon','powderblue']
df.plot(color=color_theme)
z=[1,2,3,4,0,5]

plt.pie(z)
plt.show()
#-------------------------
color_theme=['#A9A9A9','#FFA07A','#B0E0E6','#FFE4C4','#BDB76B']
plt.pie(z,colors=color_theme)
plt.show()

#customizing line styles
x1=range(1,10)
y1=[9,8,7,6,5,4,3,2,1]
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()

#-----------------------

x1=range(1,10)
y1=[9,8,7,6,5,4,3,2,1]
plt.plot(x,y, ls='solid',lw=5)
plt.plot(x1,y1,ls='--',lw=10)
plt.show()

#----------------
plt.plot(x, y, marker = '1', mew=20)
plt.plot(x1,y1, marker = '+', mew=15)
plt.show()


#labeling and annotating

#labeling

#using functional method

x=range(1,11)
y=[1,2,3,4,0,5,4,3,2,1]

plt.bar(x,y)
plt.xlabel('your x-axis label')
plt.ylabel('your y-axis label')
plt.show()
#--------------------

import matplotlib.pyplot as plt
z=[1,2,3,4,5]
veh_type=['bicycle','motorbike','car','van','stroller']
plt.pie(z,labels=veh_type)
plt.show()

#using object oriented

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
rcParams['figure.figsize']=12,8
address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
mpg=cars.mpg
fig=plt.figure()
ax=fig.add_axes([.1,.1,0.8,0.8])
mpg.plot()

ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names,rotation=60,fontsize='medium')

ax.set_title('Miles Per Gallon of Cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

plt.show()
#---------------------------
#add legend using functional method

plt.pie(z)
plt.legend(veh_type,loc='best')
plt.show()

#add legend using object oriented method

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
rcParams['figure.figsize']=12,8
address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
mpg=cars.mpg
fig=plt.figure()
ax=fig.add_axes([.1,.1,.8,.8])
mpg.plot()

ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names,rotation=60,fontsize='medium')

ax.set_title('Miles Per Gallon of Cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

ax.legend(loc='best')

plt.show()

#---------------------

#annotating ur plot

print(mpg.max())#finding the max value of mpg and annotating there
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
rcParams['figure.figsize']=12,8
address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
mpg=cars.mpg
fig=plt.figure()
ax=fig.add_axes([.1,.1,.8,.8])
mpg.plot()

ax.set_xticks(range(32))
ax.set_xticklabels(cars.car_names,rotation=60,fontsize='medium')

ax.set_title('Miles Per Gallon of Cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

ax.set_ylim([0,45])
ax.annotate('Toyota Corolla',xy=(19,33.9), xytext=(21,35), arrowprops=dict(facecolor='black',shrink=0.05))
ax.legend(loc='best')

plt.show()

 