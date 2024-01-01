from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

opt=Options()
opt.add_experimental_option("detach",True)

s=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(options=opt,service=s)

mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception,
                                                   NoSuchElementException,
                                                   ElementNotVisibleException,
                                                   ElementNotSelectableException]
                     )

driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div").click()

searchbox=driver.find_element(By.XPATH,"//textarea[@name='q']")
searchbox.send_keys("Selenium")
searchbox.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()
driver.quit()
