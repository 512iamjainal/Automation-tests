from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)

serv=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv, options=opt)

driver.get("https://www.orangehrm.com/")
driver.maximize_window()

# whyorange=driver.find_element(By.LINK_TEXT,"Why OrangeHRM")
# our=driver.find_element(By.XPATH,"//h4[normalize-space()='Our Customers']")
# case=driver.find_element(By.XPATH,"//div[@class='mob-list-section']//a[normalize-space()='Case Studies']")
#
# # #Mousehover
# act=ActionChains(driver)
# act.move_to_element(whyorange).move_to_element(our).move_to_element(case).click().perform()