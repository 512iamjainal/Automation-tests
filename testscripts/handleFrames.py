from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt=Options()
opt.add_experimental_option("detach",True)

serv=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv,options=opt)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH,"/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]").click()
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()

outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.CSS_SELECTOR,"iframe[src='SingleFrame.html']")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("welcome")

driver.switch_to.parent_frame()


