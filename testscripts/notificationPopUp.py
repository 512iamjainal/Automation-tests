from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions
ops.add_argument("--disable-notifications")

opt = Options()
opt.add_experimental_option("detach", True)

ser = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=ser, options=opt and ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()
