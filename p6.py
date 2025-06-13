#data visualization
#Time series

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams
import seaborn as sns
from seaborn import set_style

rcParams['figure.figsize']=12,8
sns.set_style('darkgrid')
address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/Superstore-Sales.csv"
df=pd.read_csv(address, index_col='Order Date', encoding='cp1252',parse_dates=True)
print(df.head())

df['Order Quantity'].plot()
plt.show()

df2=df.sample(n=100, random_state=25,axis=0)
plt.xlabel('Order date')
plt.ylabel('Oder quantity')
plt.title('Superstore sales')
df2['Order Quantity'].plot()
plt.show()

#statistical data graphics

address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
cars.index=cars.car_names
mpg=cars['mpg']
mpg.plot(kind='hist')
plt.show()

#using hist()

plt.hist(mpg)
plt.plot()
plt.show()

#using seaborn
sns.displot(mpg) #distribution of the variable mpg
plt.show()

#scatter plots
cars.plot(kind='scatter', x='hp',y='mpg',c=['darkgray'],s=150)
plt.show()

#scatter plot using seaborn
sns.regplot(x='hp',y='mpg',data=cars,scatter=True)
plt.show()

#generating a scatter plot matrix
sns.pairplot(cars)
plt.show()

#subsetting the cars to make the pairplot more readable
cars_subset=cars[['mpg','disp','hp','wt']]
sns.pairplot(cars_subset)
plt.show()

#boxplot

cars.boxplot(column='mpg',by='am')
cars.boxplot(column='wt',by='am')
plt.show()