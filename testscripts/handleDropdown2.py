from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

serv_obj = Service(r"C:\Drivers\geckodriver-v0.33.0-win64\geckodriver.exe")

driver = webdriver.Firefox(service=serv_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='country']"))

alloptions=drpcountry.options
for opt in alloptions:
    if opt.text=="United Kingdom":
        opt.click()
        break

driver.quit()
