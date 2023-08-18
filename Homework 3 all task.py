#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('audi.csv')

# Pie Chart
plt.figure(figsize=(10, 5))
transmission_counts = df['transmission'].value_counts()
plt.subplot(1, 2, 1)
plt.pie(transmission_counts, labels=transmission_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Transmission Types')

# Barplot
plt.subplot(1, 2, 2)
sns.countplot(data=df, x='transmission')
plt.title('Distribution of Transmission Types')
plt.xlabel('Transmission Type')
plt.ylabel('Count')

plt.tight_layout()
plt.show()


# In[3]:


plt.figure(figsize=(10, 5))

# Scatterplot
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='mileage', y='price')
plt.title('Scatterplot of Mileage vs Price')

# Scatterplot with hue
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='mileage', y='price', hue='fuelType')
plt.title('Scatterplot of Mileage vs Price with Fuel Type')

plt.tight_layout()
plt.show()


# In[8]:


sns.pairplot(data=df, vars=['price', 'mileage', 'engineSize'])
plt.suptitle('Pair Plot of Numeric Columns', y=1.02)
plt.show()


# In[9]:


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='mileage', y='price', hue='fuelType')
plt.title('Scatterplot of Mileage vs Price with Fuel Type')

plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='engineSize', y='price', hue='fuelType')
plt.title('Scatterplot of Engine Size vs Price with Fuel Type')

plt.tight_layout()
plt.show()


# In[10]:


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='mileage', y='price', hue='fuelType')
plt.title('Scatterplot of Mileage vs Price with Fuel Type')
plt.xlabel('Mileage')
plt.ylabel('Price')

plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='engineSize', y='price', hue='fuelType')
plt.title('Scatterplot of Engine Size vs Price with Fuel Type')
plt.xlabel('Engine Size')
plt.ylabel('Price')

plt.tight_layout()
plt.show()


# In[12]:


plt.figure(figsize=(10, 5))

# Boxplot
plt.subplot(1, 2, 1)
sns.boxplot(data=df, x='fuelType', y='engineSize')
plt.title('Boxplot of Engine Size by Fuel Type')

# Violin plot
plt.subplot(1, 2, 2)
sns.violinplot(data=df, x='fuelType', y='engineSize')
plt.title('Violin Plot of Engine Size by Fuel Type')

plt.tight_layout()
plt.show()


# In[13]:


# a) Top 5 selling car models
top_models = df['model'].value_counts().head(5)
plt.figure(figsize=(10, 5))
sns.barplot(x=top_models.index, y=top_models.values)
plt.title('Top 5 Selling Car Models')
plt.xlabel('Car Model')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# b) Average selling price of top 5 selling car models
avg_prices = df.groupby('model')['price'].mean().loc[top_models.index]
plt.figure(figsize=(10, 5))
sns.barplot(x=avg_prices.index, y=avg_prices.values)
plt.title('Average Selling Price of Top 5 Selling Car Models')
plt.xlabel('Car Model')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.show()

# c) Total sale of top 5 selling car models
total_sales = df.groupby('model')['price'].sum().loc[top_models.index]
plt.figure(figsize=(10, 5))
sns.barplot(x=total_sales.index, y=total_sales.values)
plt.title('Total Sale of Top 5 Selling Car Models')
plt.xlabel('Car Model')
plt.ylabel('Total Sale')
plt.xticks(rotation=45)
plt.show()


# In[14]:


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.boxplot(data=df, x='fuelType', y='price')
plt.title('Boxplot of Price by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Price')

plt.subplot(1, 2, 2)
sns.violinplot(data=df, x='fuelType', y='price')
plt.title('Violinplot of Price by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Price')

plt.tight_layout()
plt.show()


# In[15]:


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.regplot(data=df, x='mileage', y='price')
plt.title('Regression Plot of Mileage vs Price')
plt.xlabel('Mileage')
plt.ylabel('Price')

plt.subplot(1, 2, 2)
sns.regplot(data=df, x='engineSize', y='price')
plt.title('Regression Plot of Engine Size vs Price')
plt.xlabel('Engine Size')
plt.ylabel('Price')

plt.tight_layout()
plt.show()


# In[ ]:




