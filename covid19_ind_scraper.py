#!/usr/bin/env python
# coding: utf-8

# In[54]:


import requests as req
import json


# In[55]:


data_url = "https://api.covid19india.org/v4/data.json"


# In[56]:


res = req.get(data_url)


# In[57]:


with open('raw_data.json','wb') as file:
    file.write(res.content)


# In[58]:


with open('raw_data.json') as f:
    data = json.load(f)


# In[59]:


type(data)


# In[60]:


data["KL"]["districts"]["Thrissur"]['total']


# In[61]:


for dist in data["KL"]["districts"]:
    print(dist, "\n\n", data["KL"]["districts"][dist]['total'], "\n\n")


# In[ ]:




