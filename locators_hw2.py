#HW 2
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.target.com/')

driver.find_element(By.ID, 'account-sign-in').click()
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

sleep(3)

expected_text = 'Sign in or create account'
actual_text = driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
print(actual_text)

assert expected_text in actual_text, f'Expected text {expected_text} not in actual text {actual_text}'
print('Test case PASSED')

driver.find_element(By.ID, 'login').click()

driver.quit()
