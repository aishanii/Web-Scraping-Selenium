#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
import pandas as pd
import time
import os




HospitalName=[]
Adress=[]
TotalBeds=[]
ICUbeds=[]
Oprooms=[]
interarrivals=[]
LandPhone=[]
Mobile=[]
Website=[]
Email=[]
HosPhoto=[]
Spec=[]
Interarrival=[]

NA = "NaN"
i = 0
url = 'https://www.indiahealthcare.org/?speciality=Chest%20%26%20Pulmonary'
driver.get(url)

# print(driver.current_window_handle)

names = driver.find_elements_by_class_name("hospital-name")
time.sleep(3)

for name in names:
    
    driver.execute_script("arguments[0].click();", name)
    i+=1
    time.sleep(2)
    

    HospitalName.append(name.text)
    driver.switch_to.window(driver.window_handles[i])
    time.sleep(1)
    

    Spec.append("Speciality : Cosmetic")

    try:
        address = driver.find_element_by_class_name("hospital-content").text
        Adress.append(address)
    except:
        Adress.append(NA)
        
    try:
       totalbeds=driver.find_element_by_id('beds_count').text
       TotalBeds.append(totalbeds)
    except:
        TotalBeds.append(NA)
        
        
    try:
        icubeds=driver.find_element_by_id('icu_beds').text
        ICUbeds.append(icubeds)
    except:
        ICUbeds.append(NA)
    
    
    
    try:
        oprooms=driver.find_element_by_id('operating_rooms').text
        Oprooms.append(oprooms)
    except:
        Oprooms.append(NA)
    
    
    
    try:
        interarrivals=driver.find_element_by_id('intl_patients').text
        Interarrival.append(interarrivals)
    except:
        Interarrival.append(NA)
    
    
    
    try:
        landphone=driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[1]/p[2]').text
        LandPhone.append(landphone)
    except:
        LandPhone.append(NA)
        
        
        
    try:
        mobile=driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[2]/p[2]').text
        Mobile.append(mobile)
    except:
        Mobile.append(NA)



    try:
        website=driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[3]/p[2]/b/a').text
        Website.append(website)
    except:
        Website.append(NA)
        
    
    
    
    try:
        email=driver.find_element_by_xpath('/html/body/section/hospital-data/div/div/div[2]/div[3]/div[4]/p[2]/b').text
        Email.append(email)
    except:
        Email.append(NA)

      
  
    try:
       #Accreditions Photo
        accrds = driver.find_elements_by_class_name('mr-4 > img')
        for acc in accrds:
            HosPhoto.append(acc.get_attribute('src'))
    except:
        HosPhoto.append(NA)
    
    driver.switch_to.window(driver.window_handles[0])
driver.quit()

data={'Hospital Name':HospitalName,
      'Speciality':Spec,
      'Hospital Adress':Adress,
      'Total Beds':TotalBeds,
      'ICU Beds':ICUbeds,
      'Operational Rooms':Oprooms,
      'International arrivals':Interarrival,
      'Landline Phone':LandPhone,
      'Mobile contact':Mobile,
      'Website':Website,
      'Email':Email
      }

df = pd.DataFrame(data)
print(df)
df.to_csv('Chest.csv', mode = 'a', header = True)


# In[ ]:




