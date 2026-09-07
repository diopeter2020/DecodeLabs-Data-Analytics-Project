#!/usr/bin/env python
# coding: utf-8

# # Decodelabs Data Analytics Project 1

# ## Data Cleaning 

# ## Objective

# #### The main objective of the project is to clean and transform a raw e-commerce dataset so that it becomes ready for Analisis

# ## Specifically, the project aims to:
# 
# 
# 

# #### a. Identify and handle missing values.
# #### b. Find and remove duplicates records.
# #### c. Identify and correct incorrect data formats, expecially dates, numbers and text.
# #### d. Ensure the dataset has zero duplicates.
# #### e. Ensure dates are correctly formated.

# ## Import libraries

# ## Load dataset

# In[95]:


import pandas as pd
import numpy as np
df = pd.read_excel("Dataset for Data Analytics.xlsx")
df.head()


# ## Check the Shape of the Dataset

# In[27]:


print("Dataset Shape")
df.shape


# ## Print All Columss Name 

# In[29]:


print("\nColumn Names:")
print(df.columns)


# ## Print Dataset Information

# In[32]:


print("\nDataset Information:")
df.info()


# ## Check Basic Statistics

# In[34]:


df.describe()


# ## Check for Missing Value
# ##### About 309 missig values found on the coupon code column

# In[37]:


print("\nMissing Values:")
print(df.isnull().sum())


# In[39]:


missing_percent = (df.isnull().sum() / len(df)) * 100
missing_report = pd.DataFrame({
"Missing Values": df.isnull().sum(),
 "Missing Percentage": missing_percent
})
missing_report


# ### Missing Values was replaced with NoCode

# In[42]:


df["CouponCode"]= df["CouponCode"].fillna("NoCode")
print("\nMissing Values after Cleaning:")
print(df.isnull().sum())


# In[44]:


df["CouponCode"].head(20)


# ### No duplicates rows 

# In[47]:


print("\nduplicate rows:")
print(df.duplicated().sum())


# In[49]:


print(df["OrderID"].duplicated().sum())
print("\nduplicate rows:")
print(df.duplicated().sum())


# In[53]:


df = df.drop_duplicates()
df = df.drop_duplicates(subset = "OrderID")
df


# In[55]:


print(df.duplicated().sum())
print(df["OrderID"].duplicated().sum())
      


# ### Clean white space 

# In[58]:


df["Product"] = df["Product"].str.strip().str.title()
df.head(2)


# In[60]:


df["ShippingAddresst"] = df["ShippingAddress"].str.strip().str.title()
df.head(2)


# ### Round Numeric column to 2 decimalplace

# In[63]:


df["UnitPrice"] = df["UnitPrice"].round(2)
df.head(2)


# In[65]:


df["TotalPrice"] = df["TotalPrice"].round(2)
df.head(2)


# ### The Clean dataset wa exported and saved as csv

# In[68]:


df.to_csv("Cleaned_dataset.csv", index = False)
df.head()


# In[70]:


print("Dataset saved successfully!")


# In[74]:


df.head(10)


# ## Conclussion

# ### The raw dataset was successfully cleaned and transformed making it ready and fit for analysis with no missing values and no duplicates rows
# 

# In[ ]:




