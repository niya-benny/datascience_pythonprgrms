import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series,DataFrame
import scipy
from scipy import stats
#to set the no.of digits after te decimal point when NumPy arrays are printed
np.set_printoptions(precision=2) #shows 2 decimal places for floating point numbers

a=np.array([1,2,3,4,5,6])
print(a)

print("\n")
b=np.array([[10,20,30],[40,50,60]])
print(b)

print("\n")
np.random.seed(25)
c=36*np.random.randn(6)
print(c)

print("\n")
d=np.arange(1,35)
print(d)

print(a*10)

print(c+a)

print(c-a)

print(c*a)
print(c/a)

#summary statistics

address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
print(cars.head())

#to sum the columns
print(cars.sum())

#to sum the rows
print(cars.sum(axis=1,numeric_only=True))

print(cars.median(numeric_only=True))

print(cars.mean(numeric_only=True))

print(cars.max())



#finding the row which has the max 'mpg' value
mpg=cars.mpg
ind=mpg.idxmax() #will give the index of the row which has max value
print(cars.loc[ind]) #gives Series

#to print the above as a row
mpg=cars.mpg
ind=mpg.idxmax() #will give the index of the row which has max value
print(cars.loc[[ind]]) #gives DataFrame


#variable distribution

#standard deviation
cars.std(numeric_only=True)

#variance
cars.var(numeric_only=True)

gear=cars.gear
print(gear.value_counts())

#entire statistical description
cars.describe()

#summarizing categorical variables


address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
cars.index=cars.car_names

print(cars.head())


carb=cars.carb
print(carb.value_counts())
#----------------------

cars_sub=cars[['cyl','vs','am','gear','carb']]
print(cars_sub.head())

gears_group=cars_sub.groupby('gear')
for name,group in gears_group:  #name->column value #group->rows that has that value
    print(f"\nGear: {name}")
    print(group)
print(gears_group.describe())


#------------------------

#transforming variables to categorical data type

cars['group']=pd.Series(cars.gear, dtype='category') #categorical values of gear is stored into a new column 'group'
#or
cars['group'] = cars['gear'].astype('category')

print(cars['group'].dtypes)
print(cars['group'].value_counts())


#describing categorical data with crosstabs

#crosstab--> cross tabulation of 2 or more features. shows frequency counts of features
print(pd.crosstab(cars['am'],cars['gear']))















