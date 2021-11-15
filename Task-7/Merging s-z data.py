#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas, sys
import pandas as pd


st = pd.read_csv(r'C:/User/aisha/OneDrive/Desktop/gg/s_t_data')
u = pd.read_csv(r'C:/Users/aisha/OneDrive/Desktop/gg/u_data')
v = pd.read_csv(r'C:/Users/aisha/OneDrive/Desktop/gg/v_data')
w = pd.read_csv(r'C:/Users/aisha/OneDrive/Desktop/gg/w_data')
x = pd.read_csv(r'C:/Users/aisha/OneDrive/Desktop/gg/x_data')
y = pd.read_csv(r'C:/Users/aisha/OneDrive/Desktop/gg/y_data')
z = pd.read_csv(r'C:/Users/aisha/OneDive/Desktop/gg/z_data')


df = pd.concat(map(pd.read_csv, [st,u,v,w,x,y,z]), ignore_index=True)


# In[ ]:




