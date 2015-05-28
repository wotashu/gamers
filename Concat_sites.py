
# coding: utf-8

# In[17]:

import pandas as pd


# In[18]:

# import Giant Bomb
gb = pd.read_csv("giantbomb/giantbomb_reviews.csv")


# In[19]:

# import IGN
colHeader = ['game','date','reviewer','link','review']
IGN = pd.read_csv('IGN_1.csv', names = colHeader)
IGN['site'] = 'IGN'


# In[47]:

# import Game Spot
colHeader2 = ['reviewer', 'date', 'game', 'link', 'score', 'platforms', 'review',] 
gamespot = pd.read_csv('gamespot/GAMESPOT_UPDATED.csv', names = colHeader2)
gamespot['site'] = 'GameSpot'
gamespot['score_100'] = 10*(gamespot['score'])


# In[48]:

gamespot.head()


# In[49]:

# convert date columns to datetime
gamespot["date"] = pd.to_datetime(gamespot.date, dayfirst=True)
IGN["date"] = pd.to_datetime(IGN.date, dayfirst=True)
gb["date"] = pd.to_datetime(gb.date, dayfirst=False)


# In[50]:

results = pd.concat([gb, IGN, gamespot], ignore_index=True)


# In[52]:

results.to_csv('results.csv', encoding='utf-8', index=False)


# In[45]:

results.shape


# In[46]:

from bs4 import BeautifulSoup
import urllib2
import requests
import re
import os
import numpy as np


# In[9]:

gb["review_lenght"] = len(gb["review"])


# In[16]:

len(gb.reviewer[2:3])

