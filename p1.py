
import pandas as pd
import numpy as np
from pandas import Series,DataFrame

numbers=(DataFrame(np.arange(0,90,3).reshape(10,3), index = ['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10'], columns = ['c1','c2','c3']))
print(numbers)

#selecting using iloc
print(numbers.iloc[1,2])

#assigning
numbers.iloc[1,2]=20
print(numbers )

#fancy indexing
print("\n")
print(numbers.iloc[[1,2,4],[1,2]])

#masking using boolean
mask=numbers>30
print(mask)

print(numbers[mask])

numbers[numbers>30]=0
print(numbers)

#slicing


print(numbers.iloc[2:6,1:3])

#Missing values

data={'name':['niy','par','ameesha','jof','bhadra','ahana','sreya'],
      'age':[20,22,20,21,24,23,22],
      'gender':['Male','Male','Male','Female','Male','Male','Female'],
      'rank':[2,1,4,5,3,7,6]}

ranking_df=DataFrame(data)
ranking_df.iloc[2:5,1]=np.nan
ranking_df.iloc[3:6,3]=np.nan
ranking_df.iloc[3,:]=np.nan
print(ranking_df)

#check which all are missing
print(ranking_df.isnull())

#check which all are not missing
print(ranking_df.notnull())

#check a particular column's missing values
print("\n")
boolseries=pd.isnull(ranking_df['age'])
print(ranking_df[boolseries])

#fill
print(ranking_df.fillna(0))

#filling the missing values with the prior values
print("\n",ranking_df.fillna(method='pad'))

#filling the missing values with the succeeding values
print("\n",ranking_df.fillna(method='bfill'))

#making equally spaced
print(ranking_df.interpolate(method='linear'))

#drop the rows with missing values
print("\n",ranking_df.dropna())

#drop only the rows which have all missing values
print("\n",ranking_df.dropna(how='all'))

#drop the columns which have atleast one missing value
print("\n",ranking_df.dropna(axis=1))

#drop the rows which have atleast one missing value
print("\n",ranking_df.dropna(axis=0))

#removing duplicates
df=DataFrame({'column 1':[1,1,2,2,3,3,3],
              'column 2':['a','a','b','b','c','c','c'],
              'column 3':['A','A','B','B','C','C','C']})
print(df)

#true if it is the same as the prior elements
print(df.duplicated())

#removing duplicates
print(df.drop_duplicates())

df2=DataFrame({'column 1':[1,1,2,2,3,3,3],
              'column 2':['a','a','b','b','c','c','c'],
              'column 3':['A','A','B','B','C','D','C']})
print(df2)
#drop only the duplicates in a particular column
print("\n",df2.drop_duplicates(['column 3']))