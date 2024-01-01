from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(options=opt,service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#id and name locators
# driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo IdeaCentre 600 All-in-One PC")
driver.find_element(By.NAME,"q").send_keys("Lenovo IdeaCentre 600 All-in-One PC")

#Linktext and partial linktext
# driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Regi").click()

#class name
# sliders=driver.find_elements(By.CLASS_NAME,"")
# print(len(sliders))

#tagname
# links= driver.find_elements(By.TAG_NAME,"a")
# print(len(links))

# driver.close()