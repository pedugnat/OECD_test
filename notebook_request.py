
# coding: utf-8

# In[70]:


# uncomment if you don't have pandas_datareader installed
# ! pip install pandas_datareader


# In[14]:


# Classic imports
import numpy as np
import pandas as pd
import requests

# Specific imports
import pandas_datareader as pdr
from pandas_datareader import wb


# In[28]:


# This link proved very useful : 
# https://pydata.github.io/pandas-datareader/stable/remote_data.html#world-bank


# In[71]:


# Search in the available indicators which on matches our search
matches = wb.search('Statistical')
matches[['id', 'name', 'sourceNote']].values
# Seems like the 2nd indicator is the one we are interested in


# In[73]:


MY_IND = 'IQ.SCI.OVRL'
START_YEAR = 2010

matches = wb.download(indicator=MY_IND, country='all', start=START_YEAR, end=2019)


# In[74]:


# Sanity check : quick overview of the data
matches.head(20)


# In[75]:


# If you want to save the matches dataframe as csv, uncomment below
# matches.to_csv('first_data_stat_ind.csv')

