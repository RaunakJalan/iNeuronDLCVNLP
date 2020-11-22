import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

titanic_data = pd.read_csv('titanic_original.csv')

titanic_data.drop(titanic_data.tail(1).index,inplace=True)

sex = list(set(titanic_data.sex))
count = titanic_data.sex.value_counts()

#print(count)

#print(titanic_data.fare)

plt.pie(count, labels=sex, autopct='%1.2f%%')
plt.show()

sexvalues = list(titanic_data.sex)
sexValues = list(filter(lambda a: a != np.nan, sexvalues))

male_data = titanic_data[titanic_data.sex=='male']
female_data = titanic_data[titanic_data.sex=='female']

maleScatter = plt.scatter(male_data.age, male_data.fare, label='male', color='red', alpha=0.5)
femaleScatter = plt.scatter(female_data.age, female_data.fare, label='female', color='blue', alpha=0.5)
plt.legend(handles=[maleScatter, femaleScatter])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Age vs Fare')
plt.show()


