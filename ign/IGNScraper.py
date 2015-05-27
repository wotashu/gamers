
# coding: utf-8

# In[2]:

from bs4 import BeautifulSoup
from urllib2 import urlopen, Request, HTTPError, URLError
from time import sleep # be nice
import re
import os
import unicodedata
import numpy as np


# In[200]:

def make_soup(url):
    req = Request(url, headers ={'User-Agent':'Chrome'})
    try:
        html = urlopen(req).read()
        return BeautifulSoup(html, "lxml")
    except (URLError, HTTPError) as e:
#         print e.fp.read()
        print "Error"


def get_review_links(section_url):
    soup = make_soup(section_url)

    games = soup.findAll("div", { "class":"up-com grid_7" })

    link = []
    for i in range(len(games)):
        li = games[i].find("ul", { "class":"item-quickLinks clear" }).find('a', href = True)
        link.append(li['href'])
        link = list(set(link))
        
    return link


def get_review(section_url):
    soup = make_soup(section_url)
    if (soup != None): 
        reviewer = soup.find("div", { "id":"creator-name" }).text
        reviewer = unicodedata.normalize('NFKD', reviewer).encode('ascii','ignore')
        reviewer = reviewer.strip()

        reviewDate = soup.find("span", { "class":"review-date" }).text
        reviewDate = unicodedata.normalize('NFKD', reviewDate).encode('ascii','ignore')
        reviewDate = reviewDate.strip()

        title = soup.find("h2", { "class":"object-name" }).text
        title = unicodedata.normalize('NFKD', title).encode('ascii','ignore')
        title = title.strip()

        body = soup.find("div", { "id":"review-body" })
        texts = body.findAll("p")
        review = []
        for i in texts:
            review.append(unicodedata.normalize('NFKD', i.text).encode('ascii','ignore'))
    else: 
        print "page inaccessible:" + section_url
        title = ''
        reviewer = ''
        reviewDate = ''
        review = ''
    return title, reviewer, reviewDate, review 


# In[119]:

url  = ("http://www.ign.com/games/reviews")
urls = []
for i in range(50):
    urls.append(url + '?startIndex=' + str(25*i))
urls


# In[206]:

titles = []
reviewDates = []
reviews = []
reviewers = []
review_link = []
for url in range(len(urls)):
    links = get_review_links(urls[url])
    for link in links:
        print link
        title, reviewer, reviewDate, review = get_review(link)
        titles.append(title)
        reviewDates.append(reviewDate)
        reviews.append(review)
        reviewers.append(reviewer)
        review_link.append(link)


# In[211]:

# put all lists together
IGN = titles, reviewDates, reviewers, review_link, reviews

# output to a csv file, results needs to be transposed as the list is by default verticalled stacked
import csv
with open("IGN.csv", "wb") as f:
    writer = csv.writer(f) 
    for row in IGN:
        writer.writerow(row)

