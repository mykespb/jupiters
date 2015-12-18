
# coding: utf-8

# Mikhail Kolodin.
# 
# Project: Internet temperature. 2015-12-18 1.5.1
# 
# IPython research for internet temperature. We use now only fontanka.ru website, later other sites and methods will be added.
# 
# Version with database recording. Now full archive of headers since 2000.
# 
# Here we count good and bad words in the database. No more downloading info from websites.

# In[1]:

import datetime
now = datetime.datetime.now()
import time

import sqlite3


# In[2]:

# main db
db = "mp-nettemp3-fru-2015.db"
conn = sqlite3.connect(db)
cur = conn.cursor()


# In[3]:

# temp db, later - also to main
dbc = sqlite3.connect(":memory:")
curc = dbc.cursor()


# In[ ]:

# calc data per days


# In[ ]:

conn.commit()


# In[ ]:

conn.close()

