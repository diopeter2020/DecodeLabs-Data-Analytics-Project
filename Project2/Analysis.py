#!/usr/bin/env python
# coding: utf-8

# # DecodeLabs Data Analytics Project 2

# ## Exploratory Data Analysis (EDA)

# ## Objective

# #### The main objective of the project is to clean and transform a raw e-commerce dataset so that it becomes ready for Analisis

# ## Specifically, the Project aims to:

# #### a. Understanding the structure and characteristics of the data
# #### b. Performing exploratory data analysis (EDA)
# #### c. Calculating descriptive statistics
# #### d. Identifying patterns and trends
# #### e. Detecting potential outliers
# #### f. Analysing product sales performance
# #### g. Examining relationships between numerical variables
# #### h. Creating visualizations to communicate findings
# 

# ## Import libraries

# ## Load dataset

# In[183]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("Cleaned_dataset.csv")
df.head()


# ## Perform Basic Statistics on Numeric columns

# In[127]:


print("/nBasic Statistics")
print(df.describe())


# ## Print anad Exeimine The Data columns and Data Types

# In[129]:


print("/nDataset Information:")
print(df.info())


# ## Count Numbers of Transactions

# In[131]:


print("Count:")
print(df["TotalPrice"].count())


# ## Calculate the Mean Value

# In[133]:


print("Mean:")
print(df["TotalPrice"].mean())


# ## Calculate the Median Value

# In[135]:


print("Median:")
print(df["TotalPrice"].median())


# ## Calculate the Total Sales Value

# In[136]:


print("/nTotal Sales:")
print(df["TotalPrice"].sum())


# ## Find The Most Sold Product

# In[140]:


print("/nMost Sold Product:")
print(df["Product"].value_counts().head)


# ## Find Top 5 CustomerID

# In[143]:


print("/nTop 5 CustomerID:")
print(df["CustomerID"].value_counts().head())


# ## Find Top 5 ShippingAddres

# In[145]:


print("/nTop 5 ShippingAddres:")
print(df["ShippingAddress"].value_counts().head())


# ## IQR-Value Base Check

# In[147]:


Q1 = df["TotalPrice"].quantile(0.25)	
Q3 = df["TotalPrice"].quantile(0.75)	
IQR = Q3 - Q1


# In[149]:


lower_bond = Q1 - 1.5 * IQR
upper_bond = Q3 + 1.5 * IQR
outliers = df[(df["TotalPrice"] < lower_bond) | (df["TotalPrice"] > upper_bond)]


# ## 8 Outliers Found

# In[151]:


print("/nNumber of Outliers:")
print(len(outliers))


# In[153]:


print("/nOutliers:")
print(outliers)


# ### Histogram Showing The Distributions Of TotalPrice Frequency

# In[155]:


plt.hist(df["TotalPrice"], bins=20)
plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.show


# ## Boxplot of Total Price

# In[157]:


plt.figure(figsize=(8,5))
plt.boxplot(df["TotalPrice"])
plt.title("Boxplot of Total Price")
plt.ylabel("Total Price")
plt.grid(True)
plt.show


# ### correlation Heatmap

# In[159]:


correlation = df.select_dtypes(include=np.number).corr()


# In[161]:


plt.figure(figsize=(8,6))
plt.imshow(correlation, cmap="coolwarm",interpolation="nearest")
plt.colorbar()
plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)
plt.title("correlation Heatmap")
plt.tight_layout()
plt.show()


# ## Top 5 Product by Sales

# In[163]:


print("/n Top 5 Product by Sales:")
sales_by_product = df.groupby("Product")['TotalPrice'].sum().reset_index()
sales_by_product


# ## line Graph Showing The Distribution of Sales By Months And Year

# In[165]:


df['Date'] = pd.to_datetime(df['Date'])
df.groupby(df['Date'].dt.to_period('M'))['TotalPrice'].sum().plot()


# In[167]:


df['Date'] = pd.to_datetime(df['Date'])
df.groupby(df['Date'].dt.to_period('M'))['TotalPrice'].sum()


# ## TotalPrice Group By ReferralSource 

# In[179]:


df.groupby('ReferralSource')['TotalPrice'].sum().reset_index()


# ## OrderID Group By ReferralSource

# In[175]:


df.groupby('ReferralSource')['OrderID'].count().reset_index()


# ## Conclussion

# #### This project strengthened my ability to move from raw data to meaningful insights by combining data preparation, exploratory analysis, descriptive statistics, visualization, and analytical thinking.
