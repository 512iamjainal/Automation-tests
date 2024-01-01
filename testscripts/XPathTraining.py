from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service(r"C:\Drivers\geckodriver-v0.33.0-win64\geckodriver.exe")

driver=webdriver.Firefox(service=serv_obj)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#Abs XPath
# driver.find_element(By.XPATH,"/html[1]/body[1]/div[6]/div[1]/div[2]/div[2]/form[1]/input[1]").send_keys("MacBook")
# driver.find_element(By.XPATH,"/html[1]/body[1]/div[6]/div[1]/div[2]/div[2]/form[1]/button[1]").click()

#Rel XPath
# driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys("MacBook")
# driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()

#OR
# driver.find_element(By.XPATH,"//input[@name='q' or @id='small-earchterms']").send_keys("MacBook")
# driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()

#AND
# driver.find_element(By.XPATH,"//input[@name='q' and @id='small-searchterms']").send_keys("MacBook")
# driver.find_element(By.XPATH,"//button[@type='submit' and @class='button-1 search-box-button']").click()

#contains() and starts-with()
# driver.find_element(By.XPATH,"//input[contains(@class,'search')]").send_keys("MacBook")
# driver.find_element(By.XPATH,"//button[starts-with(@class,'button')]").click()

#text()
driver.find_element(By.XPATH,"//input[contains(@class,'search')]").send_keys("MacBook") #using contains() bcz of the searchbox
driver.find_element(By.XPATH,"//button[text()='Search']").click()