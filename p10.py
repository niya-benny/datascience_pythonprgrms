import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

data={'names':['steve','john','richard','sarah','rambo','michael','julie'],
      'age':[20,22,20,21,24,23,22],
      'gender':['Male','Male',np.nan,'Female',np.nan,'Male',np.nan],
      'rank':[2,1,4,5,3,7,6]}
df=DataFrame(data)
print(df)

df=df.drop('gender',axis=1)
print(df)


#Label encoding
label_encoder=LabelEncoder()
label_encoder.fit(df['names'])

label_encoded_names=label_encoder.transform(df['names'])
print(label_encoded_names)

#one-hot encoder

onehot_encoder=OneHotEncoder(sparse_output=False)
onehot_encoded_name = onehot_encoder.fit_transform(df[['names']])

columns = onehot_encoder.get_feature_names_out(['names'])
onehot_encoded_df=DataFrame(onehot_encoded_name,columns=columns)
onehot_encoded_df['names']=df[['names']]
print(onehot_encoded_df)

from sklearn.preprocessing import MinMaxScaler, scale

address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)

print(cars.head())

plt.plot(cars[['mpg']])
plt.show()

#normalization(btw 0 and 1)
minmax_scaler=MinMaxScaler()
minmax_scaler.fit(cars[['mpg']])

scaled_data=minmax_scaler.transform((cars[['mpg']]))
plt.plot(scaled_data)
plt.show()


#standardization(mean-> 0 std_deviation ->1)
standard_scalar=scale(cars[['mpg']])
plt.plot(standard_scalar)
plt.show()
