
# coding: utf-8

# In[7]:

import pandas as pd


# In[8]:

# import Giant Bomb
gb = pd.read_csv("giantbomb/giantbomb_reviews.csv", encoding='utf-8')


# In[9]:

# import IGN
colHeader = ['game','date','reviewer','link','review']
IGN = pd.read_csv('IGN_1.csv', names = colHeader)
IGN['site'] = 'IGN'


# In[10]:

# import Game Spot
colHeader2 = ['reviewer', 'date', 'game', 'link', 'score', 'platforms', 'review']
gamespot = pd.read_csv('gamespot/GAMESPOT_UPDATED.csv', names = colHeader2)
gamespot['site'] = 'GameSpot'
gamespot['score_100'] = 10*gamespot['score']


# In[11]:

# convert date columns to datetime
gamespot["date"] = pd.to_datetime(gamespot.date, dayfirst=True)
IGN["date"] = pd.to_datetime(IGN.date, dayfirst=True)
gb["date"] = pd.to_datetime(gb.date, dayfirst=False)


# In[12]:

results = pd.concat([gb, IGN, gamespot], ignore_index=True)


# In[13]:

results.to_csv('results.csv', encoding='utf-8', index=False)


# In[14]:

results.shape


# In[15]:

from bs4 import BeautifulSoup
import urllib2
import requests
import re
import os
import numpy as np


# In[16]:

gb_means = gb
gb_means['review_length'] = np.nan


# In[17]:

for index, row in gb_means.iterrows():
    gb_means['review_length'][index] = len(row['review'].split())


# In[18]:

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
get_ipython().magic(u'matplotlib inline')
from pandas.tools.plotting import scatter_matrix
matplotlib.style.use('ggplot')


# In[19]:

grouped = gb_means.groupby(['site', 'reviewer'])
calculated_means = grouped.mean()


# In[20]:

results['review_length'] = np.nan
for index, row in results.iterrows():
    results.loc[index, 'review_length'] = len(row['review'].split())


# In[138]:

# group by site theen reviewer
grouped = results.groupby(['site', 'reviewer'])
# calculate mean of each review's scores and review lengths
calculated_means = grouped.mean()
# find number or reviews per reviewer
grouped_size = grouped.size().order()

by_reviewer_summary = grouped['review_length'].agg([np.sum, np.mean, np.std])


# In[139]:

# compute summary statistics on review length by reviewer
by_reviewer_summary = grouped['review_length'].agg([np.sum, np.mean, np.std])


# In[148]:

# bar chart by mean review length
by_reviewer_summary[['mean']].plot(kind='barh' )


# In[122]:

# group by site
by_site = results.groupby(['site'])
# summarize review length statistics sum, mean and standard deviation
by_site_summary = by_site['review_length'].agg([np.sum, np.mean, np.std])
print by_site_summary


# In[136]:

# bar chart by mean review length
by_site_summary['mean'].plot(kind='bar')


# In[50]:

calculated_means.to_csv('calculated_means.csv', encoding='utf-8', index=True)


# In[81]:

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
get_ipython().magic(u'matplotlib inline')
from pandas.tools.plotting import scatter_matrix
matplotlib.style.use('ggplot')


# In[54]:

# get scatter of scores and review length
x = results['score_100']
y = results['review_length']

# Get unique names of
uniq = list(set(results['site']))

# Set the color map to match the number of species
z = range(1,len(uniq))
hot = plt.get_cmap('hot')
cNorm  = colors.Normalize(vmin=0, vmax=len(uniq))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=hot)

# Plot each species
for i in range(len(uniq)):
    indx = results['site'] == uniq[i]
    plt.scatter(x[indx], y[indx], s=15, color=scalarMap.to_rgba(i))

plt.xlabel('Score out of 100')
plt.ylabel('length of review')
plt.title('Review Score vs. Length of review')
plt.legend()
plt.show()


# In[110]:

grouped = results.groupby(['site', 'reviewer'])
calculated_means = grouped.mean().median()


# In[32]:

sites = ['Giant Bomb', 'IGN', 'GameSpot']


# In[75]:

import seaborn as sns
sns.lmplot("review_length", "score_100", data=calculated_means, fit_reg=False)


# In[70]:

groups = results.groupby(['site'])
groups_mean = groups.mean()


# In[73]:

groups_mean


# In[ ]:



