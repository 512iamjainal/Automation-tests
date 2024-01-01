from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

opt=Options()
opt.add_experimental_option("detach",True)

s=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(options=opt,service=s)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Flenovo-ideacentre-600-all-in-one-pc")
driver.maximize_window()

# is_displayed() and enabled()
searchbox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# print(searchbox.is_displayed())
# print(searchbox.is_enabled())

# is_selected()
print("default radio buttons' status")
maleRd=driver.find_element(By.XPATH,"//input[@id='gender-male']")
femaleRd=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(maleRd.is_selected())
print(femaleRd.is_selected())

maleRd.click()

print("After selecting male radio button")
print(maleRd.is_selected())
print(femaleRd.is_selected())

femaleRd.click()

print("After selecting female radio button")
print(maleRd.is_selected())
print(femaleRd.is_selected())

time.sleep(1)
driver.close()