# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


dataset = pd.read_csv('kc_house_data.csv')

price = dataset.price

# Bedroom count 
dataset.bedrooms.value_counts().plot(kind='bar')
plt.title('number of Bedrooms')
plt.xlabel('Bedrooms')
plt.ylabel('Count')
sns.despine

# Longitude and Latitude 
plt.figure(figsize=(10,10))
sns.jointplot(x=dataset.lat, y=dataset.long, size=10)
plt.ylabel('Longitude')
plt.xlabel('Latitude')
plt.show()
sns.despine

# Living size of property 
plt.scatter(dataset.price, dataset.sqft_living)
plt.title("Price vs Sqft Living")
plt.show()

# Longitude vs Price
plt.scatter(dataset.price, dataset.long)
plt.title("Price vs Longitude of the Area")
plt.show()

# Latitude vs Price
plt.scatter(dataset.price, dataset.lat)
plt.title("Price vs Latitude of the Area")
plt.show()