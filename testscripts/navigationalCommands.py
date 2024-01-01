from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

opt=Options()
opt.add_experimental_option("detach",True)

s=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(options=opt,service=s)
driver.get("https://demo.nopcommerce.com/")
time.sleep(2)
driver.get("https://www.facebook.com/")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()

driver.quit()


