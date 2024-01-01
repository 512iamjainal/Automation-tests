import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service(r"C:\Drivers\geckodriver-v0.33.0-win64\geckodriver.exe")

driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

drpcountry = Select(driver.find_element(By.TAG_NAME,"select"))

#select option from the dropdown
# drpcountry.select_by_index(3)
# drpcountry.select_by_value('ATG')
# drpcountry.select_by_visible_text("Kenya") #used very often

#capture all the options and print them
alloptions=drpcountry.options
# print("total num of options: ", len(alloptions))

# for option in alloptions:
#     print(option.text)

#Select option from dropdown without using built-in method

for option in alloptions:
    if option.text=="Poland":
        option.click()
        break