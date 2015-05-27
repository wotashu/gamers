
# coding: utf-8

# In[1]:

import pandas as pd


# In[60]:

# import Giant Bomb
gb = pd.read_csv("giantbomb/giantbomb_reviews.csv")


# In[5]:

# import IGN
colHeader = ['game','date','reviewer','link','review']
IGN = pd.read_csv('IGN_1.csv', names = colHeader)
IGN['site'] = 'IGN'


# In[36]:

# import Game Spot
colHeader2 = ['reviewer', 'date', 'game', 'link', 'review']
gamespot = pd.read_csv('gamespot.csv', names = colHeader2)
gamespot['site'] = 'GameSpot'


# In[56]:

# convert date columns to datetime
gamespot["date"] = pd.to_datetime(gamespot.date, dayfirst=True)
IGN["date"] = pd.to_datetime(IGN.date, dayfirst=True)
gb["date"] = pd.to_datetime(gb.date, dayfirst=False)


# In[57]:

results = pd.concat([gb, IGN, gamespot], ignore_index=True)


# In[58]:

results.to_csv('results.csv', encoding='utf-8', index=False)

