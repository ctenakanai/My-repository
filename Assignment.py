#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np

df = pd.read_csv("data_assignment.csv")
df.head()


# In[30]:


df.dtypes


# In[35]:


df["Date"] = df["Date"].replace(to_replace=r'T.*', value='', regex=True)
df["Date"] = pd.to_datetime(df["Date"])

df.head()


# In[12]:


df['Id']
degree_counts = df['Id'].value_counts()
degree_counts


# In[17]:


df.duplicated().sum()


# In[28]:


df["Date"] = df["Date"].replace(to_replace=r'T.*', value='', regex=True)
df["Date"] = pd.to_datetime(df["Date"])

df.head()


# In[41]:


df["Date"] = df["Date"].replace(to_replace=r'T.*', value='', regex=True)
df["Date"] = pd.to_datetime(df["Date"]).dt.date

df.head()


# In[43]:


df.shape
df.columns
df['Classification']
degree_counts = df['Classification'].value_counts()
degree_counts


# In[46]:


classificationDF = df[["Classification", "SubClassification"]]
classificationDF = classificationDF.loc[df['Classification'] == "Mining, Resources & Energy"]
classificationDF = classificationDF.groupby("Classification")["SubClassification"].value_counts()
classificationDF


# In[48]:


df.shape
df.columns
df['Id']
degree_counts = df['Id'].value_counts()
degree_counts


# In[50]:


df.columns


# In[52]:


df['Title']
degree_counts = df['Title'].value_counts()
degree_counts


# In[54]:


df['Company']
degree_counts = df['Company'].value_counts()
degree_counts


# In[56]:


df['Date']
degree_counts = df['Date'].value_counts()
degree_counts


# In[58]:


df['Location']
degree_counts = df['Location'].value_counts()
degree_counts


# In[60]:


df['Area']
degree_counts = df['Area'].value_counts()
degree_counts


# In[62]:


df['Classification']
degree_counts = df['Classification'].value_counts()
degree_counts


# In[64]:


df['SubClassification']
degree_counts = df['SubClassification'].value_counts()
degree_counts


# In[66]:


df['Requirement']
degree_counts = df['Requirement'].value_counts()
degree_counts


# In[68]:


df['FullDescription']
degree_counts = df['FullDescription'].value_counts()
degree_counts


# In[70]:


df['LowestSalary']
degree_counts = df['LowestSalary'].value_counts()
degree_counts


# In[72]:


df['HighestSalary']
degree_counts = df['HighestSalary'].value_counts()
degree_counts


# In[74]:


df['JobType']
degree_counts = df['JobType'].value_counts()
degree_counts


# In[76]:


df.duplicated().sum()

