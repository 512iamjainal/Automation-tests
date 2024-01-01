from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

serv_obj = Service(r"C:\Drivers\geckodriver-v0.33.0-win64\geckodriver.exe")

driver = webdriver.Firefox(service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH, "//a[contains(text(),'OK')]").click()

# 1 Specific checkbox from list
# driver.find_element(By.XPATH,"//input[@id='monday']").click()
# ------------------------------------------------------------
# 2 Multiple checkbox selection
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

# Approach1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# Approach2
for checkbox in checkboxes:
    checkbox.click()
# ----------------------------------------------
# 3 Select chosen checkboxes
# for checkbox in checkboxes:
#     weekname=checkbox.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday' or weekname=='wednesday':
#       checkbox.click()
# -----------------------------------------------------
# 4 select last 2 checkboxes
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

# 5 first 2 checkboxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

# 6 clearing all checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

# driver.quit()
