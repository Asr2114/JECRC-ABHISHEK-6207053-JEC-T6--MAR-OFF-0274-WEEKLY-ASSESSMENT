from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

time.sleep(2)

username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
username.send_keys('abhishek23')

password = driver.find_element(By.CSS_SELECTOR, "input#password")
password.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

time.sleep(2)

elemental_link = driver.find_element(By.CSS_SELECTOR, "#page-footer a")
print(elemental_link.text)

time.sleep(3)

driver.quit()