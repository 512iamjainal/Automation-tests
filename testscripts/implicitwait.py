from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

opt=Options()
opt.add_experimental_option("detach",True)

s=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(options=opt,service=s)
driver.implicitly_wait(10)  #seconds #implicitly wait
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div").click()

searchbox=driver.find_element(By.XPATH,"//textarea[@name='q']")
searchbox.send_keys("Selenium")
searchbox.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver.quit()
