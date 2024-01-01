from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

opt=Options()
opt.add_experimental_option("detach",True)

s=Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
driver=webdriver.Edge(service=s,options=opt)
driver.maximize_window()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.find_element(By.XPATH,"//p[contains(@class,'fc-button-label')]").click()

#Self
# txt=driver.find_element(By.XPATH,"//a[contains(text(),'National Alumini')]/self::a").text
# print(txt)

#Parent
# txt=driver.find_element(By.XPATH,"//a[contains(text(),'National Alumini')]/parent::td").text
# print(txt)

#child
# txt=driver.find_elements(By.XPATH,"//a[contains(text(),'National Alumini')]/ancestor::tr/child::td")
# print(len(txt))

#ancestor
# txt=driver.find_element(By.XPATH,"//a[contains(text(),'National Alumini')]/ancestor::tr").text
# print(txt)

#descendant
# desc=driver.find_elements(By.XPATH,"//a[contains(text(),'National Alumini')]/ancestor::tr/descendant::*")
# print(len(desc))

#Following
# followings=driver.find_elements(By.XPATH,"//a[contains(text(),'National Alumini')]/ancestor::tr/following::*")
# print(len(followings))

#following-siblings
# fSiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'National Alumini')]/ancestor::tr/following-sibling::*")
# print(len(fSiblings))

#preceding
# precedings=driver.find_elements(By.XPATH,"//a[contains(text(),'National Alumini')]/ancestor::tr/preceding::tr")
# print(len(precedings))

#precedingsibling
precedingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'National Alumini')]/ancestor::tr/preceding-sibling::*")
print(len(precedingsiblings))

driver.close()