from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://stackoverflow.com/users/signup')

#Create your account
driver.find_element(By.XPATH, "//h1[text()='Create your account']")

#By clicking "Sign up," . . .
driver.find_element(By.CSS_SELECTOR, ".js-terms")

#Email
driver.find_element(By.CSS_SELECTOR, "#email")

#Password
driver.find_element(By.CSS_SELECTOR, "#password")

#Eye icon
driver.find_element(By.CSS_SELECTOR, ".js-show-password")

#Sign up
driver.find_element(By.CSS_SELECTOR, "#submit-button")

#Sign up with Google
driver.find_element(By.CSS_SELECTOR, "button.s-btn__google.bar-md")

#Sign up with GitHub
driver.find_element(By.CSS_SELECTOR, "button.s-btn__github.bar-md")

#Get Stack Overflow . . .
driver.find_element(By.XPATH, "//a[contains(text(), 'Get Stack Overflow')]")
