#!/usr/bin/env python
# coding: utf-8

# In[ ]:



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
import pandas as pd
import time
import os

driver.get("https://www.medicineindia.org/pharmacies-chemists-drugstores-in-city/81/bhopal")

for i in range(1,500):
           names = driver.find_elements(By.XPATH,'//*[@id="main"]/div[2]/table/tbody[2]/tr["+str(i)"]/td[1]/a') 
           nums = driver.find_elements(By.XPATH,'//*[@id="main"]/div[2]/table/tbody[2]/tr["+str(i)"]/td[3]')
           links = driver.find_elements(By.XPATH,'//*[@id="main"]/div[2]/table/tbody[2]/tr["str(i)"]/td[1]/a') 
            
nameList=[]
numsList=[]
linksList=[]



for i in range(len(names)):
    name = names[i].text
    nameList.append(name)

for i in range(len(nums)):
    num=nums[i].text
    numsList.append(num)
    
for link in links:
    href = link.get_attribute('href')
    linksList.append(href)

    
data = {'Name': nameList,
        'Phone': numsList,
        'Link':linksList}

df = pd.DataFrame(data)
print(df)

df.to_csv('BhopalData.csv', mode='w', header=False)




