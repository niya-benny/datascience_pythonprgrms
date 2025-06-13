#data visualization 2
import pandas as pd
import numpy as np

from numpy.random import randn
from pandas import Series,DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

from pandas import DataFrame

address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
mpg=cars['mpg']

x=range(1,10)
y=[1,2,3,4,0,4,3,2,1]
plt.plot(x,y)
plt.show()

mpg.plot()
plt.show()

df=cars[['cyl','wt','mpg']]
df.plot()
plt.show()

#bar chart from a list
plt.bar(x,y)
plt.show()

#creating bar charts from Pandas object
mpg.plot(kind='bar')
plt.show()

#horizontal
mpg.plot(kind='barh')
plt.show()
#--------------
#pie chart
x=[1,2,3,4,0.5]
plt.pie(x)
plt.show()

#saving a plot
plt.pie(x)
plt.savefig('piechart.png')
plt.show()

#-------------
#defining elements of a plot

#figure size
rcParams['figure.figsize']=5,4

#defining axes,ticks and grids (using oop)
x=range(1,10)
y=[1,2,3,4,0,4,3,2,1]

fig=plt.figure()
ax=fig.add_axes([.1,.1,1,1])
ax.plot(x,y)
plt.show()
#------------------------------

x=range(1,10)
y=[1,2,3,4,0,4,3,2,1]

fig=plt.figure()
ax=fig.add_axes([.1,.1,1,1])
ax.set_xlim([1,9])
ax.set_ylim([0,5])

ax.set_xticks([0,1,2,3,4,5,6,8,9,10])
ax.set_yticks([0,1,2,3,4,5])
ax.plot(x,y)
plt.show()

#--------------------

fig=plt.figure()
ax=fig.add_axes([.1,.1,1,1])
ax.set_xlim([1,9])
ax.set_ylim(([0,5]))

ax.grid()
ax.plot(x,y)

plt.show()

#----------------------
fig=plt.figure()
#Creates one figure with 2 subplots arranged in 1 row, 2 columns
fig,(ax1,ax2)=plt.subplots(1,2)
ax1.plot(x)
ax2.plot(x,y)
plt.show()
#-----------------------------

