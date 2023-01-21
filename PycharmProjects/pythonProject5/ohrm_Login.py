from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver=webdriver.Chrome();

#Step1: Open url

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.implicitly_wait(20)

#Step2:Enter Username
driver.find_element(By.XPATH,"//*[@name='username']").send_keys("Admin")

#Step3: Enter Password

driver.find_element(By.XPATH,"//*[@name='password']").click()

#Step4: Click on login button

driver.find_element(By.XPATH,"//*[@type='submit']").click()

driver.implicitly_wait(20)

pageTitle=driver.title;

print(pageTitle)
#Verify Page title
assert "OrangeHRM" in pageTitle

driver.close()


