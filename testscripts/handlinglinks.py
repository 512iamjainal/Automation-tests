from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

serv_obj = Service(r"C:\Drivers\geckodriver-v0.33.0-win64\geckodriver.exe")

driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

#click on link
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#number of links
# links= driver.find_elements(By.TAG_NAME,"a")
links=driver.find_elements(By.XPATH,"//a")
print(len(links))

#print all links
for link in links:
    print(link.text)
