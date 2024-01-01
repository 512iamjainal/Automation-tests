from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

serv_obj = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
opt=Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countriesList=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countriesList))

for country in countriesList:
    if country.text=="India":
        country.click()
        break
