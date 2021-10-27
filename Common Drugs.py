#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import time

start = time.time()
one_mg = list(pd.read_csv(r'C:\Users\aisha\Downloads\1mg.csv')['Product Name'])

pharmeasy = list(pd.read_csv(r'C:\Users\aisha\Downloads\G-K_Pharmeasy.csv')['medName'])

netmeds = list(pd.read_csv(r'C:\Users\aisha\Downloads\G-K_netmeds.csv')['Medname'])

end = time.time()
print("Time needed = ",end - start)
print("---------------------------------------------------")

List = []
count = 1
for i in one_mg:
    if i in pharmeasy or i in netmeds:
        print(count, " : ", i)
        List.append(i)
        count += 1

dic = {"Common Drugs": List}

df = pd.DataFrame(dic)
df.to_csv('Common_Drugs_G-K.csv')


# In[ ]:




