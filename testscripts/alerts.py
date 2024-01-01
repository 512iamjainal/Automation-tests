import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)

serv=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv,options=opt)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#opens alert window
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(3)

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("Welcome")
# alertwindow.accept()
alertwindow.dismiss()
