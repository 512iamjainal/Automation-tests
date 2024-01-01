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

#find_element()
#1  Locator matching with single web element
# element= driver.find_element(By.CSS_SELECTOR,"input#small-searchterms")
# element.send_keys("MacBook")

#2  Locator matching with multiple web elements
# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)

#3  element not available then thow NoSuchElementException
# login_element=driver.find_element(By.LINK_TEXT,"Log")
# login_element.click()

#find_elements() returns multiple elements
#1  locator matching with single element
# elements = driver.find_elements(By.CSS_SELECTOR,"input#small-searchterms")
# print(len(elements))
# print(elements[0].send_keys("iphone"))

#2  locator matching with multiple element
# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))
# # print(elements[0].text)
# for i in elements:
#     print(i.text)

#3  element not available
elements=driver.find_elements(By.LINK_TEXT,"Log")
print("elements returned:", len(elements))