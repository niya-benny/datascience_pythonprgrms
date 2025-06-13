

#parametric and non-parametric correlation analysis

#parametric
#Pearson Correlation

import pandas as pd
import numpy as numpy

import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams
import scipy
from scipy.stats import pearsonr

rcParams['figure.figsize']=12,8
sns.set_style('darkgrid')

address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]

# sns.pairplot(cars)
# plt.show()

#pairplot of a subset of cars
x=cars[['mpg','hp','qsec','wt']]
print(sns.pairplot(x))

# using scipy to find pearson correlation coefficient
mpg=cars['mpg']
hp=cars['hp']
qsec=cars['qsec']
wt=cars['wt']

'''pearsonr(mpg, hp) returns two values:
   pearsonr_coefficient: The correlation strength
   p_value: The probability that this correlation happened by chance
    (low p-value means the correlation is statistically significant)'''

pearsonr_coefficient, p_value=pearsonr(mpg,hp)
print("PearsonR Correlation Coefficient %0.3f" % (pearsonr_coefficient) )

'''  % outside the string is used to inject the value (pearsonr_coefficient) into that placeholder " %0.3f"  '''

pearsonr_coefficient, p_value=pearsonr(mpg,qsec)
print("PearsonR Correlation Coefficient %0.3f" % (pearsonr_coefficient) )

pearsonr_coefficient, p_value=pearsonr(mpg,wt)
print("PearsonR Correlation Coefficient %0.3f" % (pearsonr_coefficient) )

#using pandas to calculate the pearson correlation coefficient
corr=x.corr()
print(corr)
plt.show()


#using seaborn
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.show()


#non-parametric

#Spearman's rank correlation

from scipy.stats import spearmanr

address="C:/Users/Niya.Benny/PycharmProjects/PythonProject/mtcars.csv"
cars=pd.read_csv(address)
cars.columns=["car_names","mpg","cyl","disp","hp","drat","wt","qsec","vs","am","gear","carb"]
print(cars.head())

# sns.pairplot(cars)
# plt.show()

x=cars[['cyl','vs','am','gear']]
sns.pairplot(x)
plt.show()

cyl=cars['cyl']
vs=cars['vs']
am=cars['am']
gear=cars['gear']

spearmanr_coefficient, p_value=spearmanr(cyl,vs)
print("Spearman rank correlation coefficient %0.3f" % (spearmanr_coefficient))

spearmanr_coefficient, p_value=spearmanr(cyl,am)
print("Spearman rank correlation coefficient %0.3f" % (spearmanr_coefficient))

spearmanr_coefficient, p_value=spearmanr(cyl,gear)
print("Spearman rank correlation coefficient %0.3f" % (spearmanr_coefficient))
print(("\n"))


#chi-square test for independence
#if p-value>0.05 ---> variables are independent
#if not, the variables are correlated

from scipy.stats import chi2_contingency

table=pd.crosstab(cyl,am)
chi2,p,dof,expected = chi2_contingency(table.values)
print('Chi-square statistic %0.3f p_value %0.3f' %(chi2,p))


table=pd.crosstab(cyl,vs)
chi2,p,dof,expected = chi2_contingency(table.values)
print('Chi-square statistic %0.3f p_value %0.3f' %(chi2,p))

table=pd.crosstab(cyl,gear)
chi2,p,dof,expected = chi2_contingency(table.values)
print('Chi-square statistic %0.3f p_value %0.3f' %(chi2,p))
