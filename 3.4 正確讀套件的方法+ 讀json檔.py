#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.sin(3)


# In[3]:


np.cos(3)


# In[4]:


np.pi


# In[3]:


from numpy import*


# In[4]:


cos(3)


# In[5]:


pi


# In[6]:


from random import*


# In[7]:


randint(1,10)


# In[9]:


for i in range (50):
    print (randint(1,10),end=",")


# In[2]:


conda update pandas-datareader


# In[3]:


conda install pandas-datareader


# In[4]:


import pandas_datareader.data as web


# In[7]:


df=web.DataReader("AAPL","yahoo",start="2012-9-1",end="2017-8-31")


# In[8]:


df.head()


# In[10]:


import pandas as pd


# In[15]:


import pathlib


# In[20]:


df=pd.read_json('/Users/yetta/Desktop/碩一/壽險經營管理實務研討/專案/Twitters_DailyData/20120412.json')


# In[22]:


df.head()


# In[28]:


df=pd.read_json('/Users/yetta/Desktop/碩一/壽險經營管理實務研討/專案/Twitters_DailyData/20110308.json')


# In[29]:


df.head()


# In[1]:


import os 
import pandas as pd 
path='/Users/yetta/Desktop/Twitters_DailyData'
data=[]
print(os.walk(path))
for file in next(os.walk(path))[2]:
    whole_path_to_file=path+'/'+file
    data+=[pd.read_json(whole_path_to_file)]

print data
df_all=data[0]
for df in data[1:]:
    df_all=df_all.append(df)
print(df_all)


# In[ ]:




