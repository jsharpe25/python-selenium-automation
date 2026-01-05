#HW 1
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_custrec_signin%3F_encoding%3DUTF8%26*Version*%3D1%26*entries*%3D0%26pldnCmp%3Drcol%26pldnCrt%3Dmy-impact%26redirect%3Dtrue&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0/')

#Amazon Logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

#Email Field
driver.find_element(By.ID, 'ap_email_login')

#Continue Button
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

#Conditions of Use Link
driver.find_element(By.XPATH, "//a[contains(@href, 'signin_notification_condition_of_use')]")

#Privacy Notice Link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

#Need Help Link
driver.find_element(By.XPATH, "//a[contains(text(), 'Need help?')]")

#Forgot Your Password Link
#No longer available

#Other Issues With Sign-In Link
#No longer available

#Create Your Amazon Account Button
#No longer available

#Create a Free Business Account Button
driver.find_element(By.XPATH, "//a[contains(@href, 'business/register')]")
