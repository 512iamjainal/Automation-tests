import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(options=opt,service=serv_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()

time.sleep(1)
#for pressing the cookies button
driver.find_element(By.XPATH, "//button[contains(text(),'Allow all cookies')]").click()

time.sleep(1)
#CSS selector
#tag and id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("503590952")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("503590952")

#tag and class
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("503590952")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("503590952")

#tag and attribute
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("503590952")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("jerry")
time.sleep(1)
#tag class attribute
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[name=email]").send_keys("503590952")
driver.find_element(By.CSS_SELECTOR,".inputtext[name=pass]").send_keys("Simbaa@51297")
time.sleep(1)
driver.find_element(By.NAME,"login").click()