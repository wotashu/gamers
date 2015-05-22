
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd


# In[5]:

#import IGN
colHeader = ['game','date','reviewer','link','review']
IGN = pd.read_csv('IGN.csv', names = colHeader)
IGN['site'] = 'IGN'
IGN


# In[8]:

#import game spot reviews
colHeader2 = ['reviewer', 'date', 'game', 'link', 'review']
gamespot = pd.read_csv('gamespot.csv', names = colHeader2)
gamespot['site'] = 'GameSpot'
gamespot


# In[13]:

colHeader3 = ['deck', 'review', 'api', 'platforms', 'publish_date', 'game', 'reviewer', 'site_detail_url']
giantBomb = pd.read_csv('giantbomb.csv', names = colHeader3)
giantBomb['site'] = 'Giant Bomb'

# giantBomb_reviws = giantBomb[,c('game','api','reviewer','site_detail_url','review')]
# giantBomb_reviws

