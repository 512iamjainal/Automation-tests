from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach", True)

ser=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=ser, options=opt)

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("Selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

#accepting cookies
driver.find_element(By.XPATH,"//a[@id='cookieChoiceDismiss']").click()

#clicking all selenium links
list_links=driver.find_elements(By.XPATH,"//a[contains(text(),'Selenium')]")

for link in list_links:
    if link.text=="Selenium":
        link.click()
