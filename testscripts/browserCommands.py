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
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'YouTube').click()
time.sleep(5)
# driver.close()
driver.quit()