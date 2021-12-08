#!/usr/bin/env python
# coding: utf-8

# In[20]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

start = time.time()

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('''https://www.healthgrades.com/usearch?what
=Family%20Medicine&where=Los%20Angeles%2C%20CA&pt=34.053490
%2C-118.245323&pageNum=1&sort.provider=bestmatch&state=CA ''')

# User Input of the location and Name
# Just Hit Enter during Input to Use the default values

name = input("Enter Doctor Name/Speciality : ")
if len(name) == 0:
    name = "Family Medicine"
    
location = input("Enter the Location : ")
if len(location) == 0:
    location = "Los Angeles"



location_box=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[1]/form/div/div[2]/div/div/div/input')

location_box.send_keys(f'{location}')
time.sleep(2)

search_button=driver.find_element(By.XPATH,'//*[@id="usearch-container"]/div[1]/form/div/div[3]/button[2]')
search_button.click()



print("\nSearching For : ")
print(name, "In ", location)


# Get the Name, Ratings/Votes Of the Fetched Result
print("--------------------------------------------------------")



for _ in range(2):
    cards = driver.find_elements(By.XPATH,'//*[@id="search-results"]/div[1]/div/main/div[1]/div/ul/li[1]/div/div[1]/div[2]/div')
    for card in cards:
        print("Name : ", card.find_element_by_class_name("provider-name__lnk").text)
        print("Rating : ", card.find_element_by_class_name("star-rating__reviews").text)
    #next = driver.find_element(By.XPATH,'//*[@id="search-results"]/div[1]/div/main/div[1]/div/div[1]/nav/ul/li[10]/a/svg')
    #next.click()
    time.sleep(2)



# In[ ]:




