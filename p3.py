#data visualization
import matplotlib.pyplot as plt
import seaborn as sns

from pandas import DataFrame

data={'names':['steve','john','richard','sarah','rambo','michael','julie'],
      'age':[20,22,20,21,24,23,22],
      'gender':['Male','Male','Male','Female','Male','Male','Female'],
      'rank':[2,1,4,5,3,7,6]}
df=DataFrame(data)
print(df)

#matplotlib bar chart
plt.bar(df['names'],df['age'])
plt.xlabel("Names")
plt.ylabel("Age")
plt.title("Comparing ages")
plt.show()

#seaborn bar chart
plot=sns.barplot(data=df,x='names',y='age')
plot.set_title("Comparing age")
plt.show()

#matplotlib line plot
plt.plot(df['names'],df['age'])
plt.xlabel("Names")
plt.ylabel("Age")
plt.title("Comparing ages")
plt.show()

#seaborn line plot
plot=sns.lineplot(data=df,x='names',y='age')
plt.show()

#matplotlib pie chart
plt.pie(df['age'],labels=df['names'])
plt.title("age comparison")
plt.show()

#seaborn pie chart (no built in function for pie chart.)
colors=sns.color_palette('pastel')[0:5]
plt.pie(df['age'],labels=df['names'],colors=colors)
plt.show()

