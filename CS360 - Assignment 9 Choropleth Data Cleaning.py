#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[2]:


dataframe = pd.read_csv(r'C:\Users\seans\Documents\School\CS 360 - Data Visualization\csv datasets\PovertyEstimates.csv')


# In[3]:


dataframe


# In[4]:


dataframe.columns


# In[6]:


dataframe['Stabr'].value_counts()


# In[7]:


cleanDF = dataframe[['Stabr','Value']].copy()


# In[10]:


cleanDF = cleanDF.rename(columns={'Stabr': 'state', 'Value': 'value'})


# In[11]:


cleanDF


# In[12]:


filtered_df = cleanDF[cleanDF['state'] != 'US']


# In[14]:


# filtered datafram has state acronyms instead of full name
filtered_df


# In[15]:


filtered_df.to_csv('povertyestimatescleaned.csv', header=True, index=False)


# In[3]:


df = pd.read_csv(r'C:\Users\seans\WebstormProjects\CS 360 - Assignment 9\data\povertyestimatescleaned.csv')


# In[4]:


df


# In[6]:


states_list = {"AL":"Alabama", "AK":"Alaska", "AZ":"Arizona", "AR":"Arkansas", "CA":"California", "CO":"Colorado", "CT":"Connecticut", 
          "DC":"Washington DC", "DE":"Delaware", "FL":"Florida", "GA":"Georgia", "HI":"Hawaii", "ID":"Idaho", "IL":"Illinois", 
          "IN":"Indiana", "IA":"Iowa", "KS":"Kansas", "KY":"Kentucky", "LA":"Louisiana", "ME":"Maine", "MD":"Maryland",
          "MA":"Massachusetts", "MI":"Michigan", "MN":"Minnesota", "MS":"Mississippi", "MO":"Missouri", "MT":"Montana",
          "NE":"Nebraska", "NV":"Nevada", "NH":"New Hampshire", "NJ":"New Jersey", "NM":"New Mexico", "NY":"New York", 
          "NC":"North Carolina", "ND":"North Dakota", "OH":"Ohio", "OK":"Oklahoma", "OR":"Oregon", "PA":"Pennsylvania", 
          "RI":"Rhode Island", "SC":"South Carolina", "SD":"South Dakota", "TN":"Tennessee", "TX":"Texas", "UT":"Utah", "VT":"Vermont",
          "VA":"Virginia", "WA":"Washington", "WV":"West Virginia","WI":"Wisconsin", "WY":"Wyoming"}
 
df["States_long"] = df.state.map(states_list)
df[["state", "States_long"]]


# In[7]:


df.to_csv('povertyestimatescleaned.csv', header=True, index=False)

