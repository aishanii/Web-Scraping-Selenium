#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install webdriver_manager')
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


DrugName= []
BrandName= []
GenericName= []
DrugType=[]
Route=[]
DosageForm=[]
DrugFacts=[]
Link=[]


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.healthgrades.com/drugs/fda/a-z")
driver.implicitly_wait(5)

L=driver.find_elements_by_xpath("//*[@class='Drugs-searchAZ-alphabetical']/a")
l=[]
for i in range(25,26): #this is for alphabet ex: for A-1 and B-2 and for Z-26.....
    l.append(L[i].get_attribute('href'))

for i in range(len(l)):
    driver.get(l[i])
    a=driver.find_elements_by_xpath("//*[@class='DrugSectionList-items']/li/a")

    A=[]
    for j in range(len(a)):
        A.append(a[j].get_attribute('href'))
        
    for k in range(len(A)):
        driver.get(A[k])
        #DrugName
        try:
           d=driver.find_element_by_xpath("/html/body/div[3]/div/main/div/div/div[1]/h1").text
           dn=dn.split('\n')
           d=dn[0]
        except:
            dn='NA'
        
        #BrandName
        try:
            bn=driver.find_element_by_xpath("//html/body/div[3]/div/main/div/div/div[2]/div[2]/ps-drugs-aka/div/div/section[1]/p[1]/span").text
        except:
            bn='NA'
            
        #Geniric Name
        try:
            gn=driver.find_element_by_xpath("/html/body/div[3]/div/main/div/div/div[2]/div[2]/ps-drugs-aka/div/div/section[1]/p[2]/span").text
        except:
            gn='NA'
            
        #dRUG Tyoe
        try:
            d=driver.find_element_by_xpath("/html/body/div[3]/div/main/div/div/div[2]/div[2]/ps-drugs-aka/div/div/section[1]/p[3]").text
            D=d.split(': ')
            dt=D[1]
        except:
            dt='NA'
            
        #Route
        try:
            r=driver.find_element_by_xpath("/html/body/div[3]/div/main/div/div/div[2]/div[2]/ps-drugs-aka/div/div/section[1]/p[4]/span").text
        except:
            r='NA'
        
        #Dosage Form
        try:
            f=driver.find_element_by_xpath("/html/body/div[3]/div/main/div/div/div[2]/div[2]/ps-drugs-aka/div/div/section[1]/p[5]").text
            F=f.split(': ')
            df=F[1]
        except:
            df='NA'
        
        #Drugfacts
        try:
            drugf=driver.find_element_by_xpath("/html/body/div[3]/div/main/div/div/div[2]/div[2]/div[1]").text
        except:
            drugf='NA'
        
        Link.append(A[k])
        
        
        
        DrugName.append(d)
        BrandName.append(bn)
        GenericName.append(gn)
        DrugType.append(dt)
        Route.append(r)
        DosageForm.append(df)
        DrugFacts.append(drugf)

 
data={'Drug Name':DrugName,
      'Brand Name':BrandName,
      'Generic Name':GenericName,
      'Drug Type':DrugType,
      'Route':Route,
      'Dosage Form':DosageForm,
      'Drug Facts':DrugFacts,
      'Link':Link
      }

df=pd.DataFrame(data)
print(df)
df.to_csv('z_data.csv', mode = 'a', header = False)
        
        
        


# In[ ]:




