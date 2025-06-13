import pandas as pd
import numpy as np
from pandas import Series,DataFrame

df=DataFrame(np.arange(36).reshape(6,6))
print(df)

df2=DataFrame(np.arange(15).reshape(5,3))
print(df2)

print("\n",pd.concat([df,df2]))
print("\n",pd.concat([df,df2], axis=1))

#drop
print("\n",df.drop([0,2]))
#drop columns
print("\n",df.drop([0,2],axis=1))

#adding data
seriesobj=Series(np.arange(6))
seriesobj.name="added_variable" #name to the series
print(seriesobj)

#joining
variable_added=DataFrame.join(df,seriesobj)
print(variable_added)

#concat it to itself
print("\n")
added_datatable=pd.concat([variable_added, variable_added], ignore_index=True)
print(added_datatable)

sorteddf=df.sort_values(by=[5],ascending=[False])
print(sorteddf)

#grouping
address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
print(cars.head())

print("\n groupby")
#groupby a column
print("\n")
cars_groups=cars.groupby(cars['cyl'])
print(cars_groups)
print(cars_groups.mean(numeric_only=True))