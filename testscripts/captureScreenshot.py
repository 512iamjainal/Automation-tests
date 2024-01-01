from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import os


serv_obj=Service(r"C:\Drivers\geckodriver-v0.33.0-win64\geckodriver.exe")
driver=webdriver.Firefox(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot(os.getcwd() + "\\homepage.png")
# driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
driver.get_full_page_screenshot_as_png()
driver.get_full_page_screenshot_as_base64()

driver.quit()

#NOT WORKING


