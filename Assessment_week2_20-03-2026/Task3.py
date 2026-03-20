from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/signup")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Abhishek")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("test12346@gmail.com")

driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()

wait.until(EC.presence_of_element_located((By.ID, "id_gender1"))).click()

newsletter = driver.find_element(By.ID, "newsletter")
newsletter.click()

offers = driver.find_element(By.ID, "optin")
offers.click()

print("Newsletter selected:", newsletter.get_attribute("checked"))
print("Offers selected:", offers.get_attribute("checked"))

driver.quit()