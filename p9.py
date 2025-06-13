
#outlier detection
#uncover anomalies that present
'''univariate method---> Tukey Boxplots -->
Boxplot whiskers are se at 1.5 IQR; if u see data point past these whiskers, they're outliers'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
from pandas.core.interchange.dataframe_protocol import DataFrame
from pylab import rcParams

from p2 import address

#identifying otliers from Tukey boxplots

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))  # Wider figure
rcParams['figure.figsize']=5,4
sns.set_style('whitegrid')
address = "C:/Users/Niya.Benny/PycharmProjects/PythonProject/iris.csv"
df = pd.read_csv(address, header=None, sep=',', usecols=[1, 2, 3, 4])
df.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
df = df.apply(pd.to_numeric, errors='coerce')
x = df.iloc[:, 0:3].values
y = df.iloc[:, 3].values

df.boxplot(return_type='dict')
plt.tight_layout()
plt.show()

#Tukey boxplots
df.boxplot(return_type='dict')
plt.plot()
plt.show()

Sepal_width= x[:,1]
iris_outliers=(Sepal_width>4)
print(df[iris_outliers])

print("\n")

Sepal_width= x[:,1]
iris_outliers=(Sepal_width<2.05)
print(df[iris_outliers])

pd.options.display.float_format='{:.1f}'.format
X_df=pd.DataFrame(x)
print(X_df.describe())


#multivariate

address = "C:/Users/Niya.Benny/PycharmProjects/PythonProject/iris.csv"
df = pd.read_csv(address, header=None, sep=',', usecols=[1, 2, 3, 4,5])
df.columns = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width','Species']
for col in df.columns[:-1]:  # All except 'Species'
    df[col] = pd.to_numeric(df[col], errors='coerce')
sns.boxplot(x='Species',y='Sepal Length',data=df,hue='Species',palette='hls',legend=False)

plt.show()

#scatterplot matrix

sns.pairplot(df,hue='Species',palette='hls')
plt.show()

#applying tukey outlier labeling

pd.options.display.float_format = '{:.1f}'.format
X_df=pd.DataFrame(x)
print(X_df.describe())

