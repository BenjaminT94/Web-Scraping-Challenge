#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://redplanetscience.com/'
browser.visit(url)
html=browser.html
soup=BeautifulSoup(html,'html.parser')


# In[4]:


# Part 1: NASA Mars News
# Scraping the latest news title
news_title=soup.find_all('div', class_='content_title')[0].text
# Scraping the latest news paragraph
news_paragraph=soup.find_all('div', class_='article_teaser_body')[0].text


# In[5]:


news_title


# In[6]:


news_paragraph


# In[50]:


# Part 2: JPL Mars Space Images - Featured Image
url="https://spaceimages-mars.com/"
featured_image_url="https://spaceimages-mars.com/image/featured/mars3.jpg"
browser.visit(url)


# In[51]:


html=browser.html
soup=BeautifulSoup(html, 'html.parser')


# In[52]:


# Using splinter to locate the correct class and index of the featured image
relative_path = soup.find_all('img')[1]["src"]
featured_image_url = url + relative_path
print(featured_image_url)


# In[53]:


# Part 3: Mars Facts
# Reading the HTML into pandas
url = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(url)
tables


# In[54]:


# Cleaning up the DataFrame and keeping only what's necessary
mars_facts_df = tables[1]
mars_facts_df.columns = ["Description", "Data"]
mars_facts_df


# In[55]:


# Converting the cleaned-up DataFrame back to HTML
mars_html= mars_facts_df.to_html()
mars_html
# Removing all the \n in the HTML and printing
mars_html.replace('\n', '')
print(mars_html)


# In[78]:


# Part 4: Mars Hemispheres
# Mars hemisphere name and image to be scraped
url = 'https://marshemispheres.com/'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[79]:


# Scraping hemispheres site and organizing the hemisphere image urls into an empty list
hemispheres=soup.find('div',class_='container')
items=hemispheres.find_all('div',class_='item')
hemisphere_urls=[]


# In[90]:


for item in items:
    try:
        # Extract title
        hem=item.find('div',class_='description')
        title=hem.h3.text
        # Extract image url
        hem_url=hem.a['href']
        browser.visit(url+hem_url)
        html=browser.html
        soup=BeautifulSoup(html,'html.parser')
        image_source=url+soup.find('li').a['href']
        if (title and image_src):
        # Print results of title and image link
            print('--------------------')
            print(title)
            print(image_src)
        # Create dictionary for title and url
        dict={'title':title,'image_url':image_source}
        hemisphere_urls.append(dict)
    except Exception as e:
        print(e)


# In[102]:


hemisphere_urls


# In[ ]:




