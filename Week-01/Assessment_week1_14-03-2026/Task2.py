from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

time.sleep(2)

search = driver.find_element(By.ID, "searchInput")

english = driver.find_element(By.CSS_SELECTOR, "#js-link-box-en")

logo = driver.find_element(By.CSS_SELECTOR, ".central-featured-logo")

languages = driver.find_elements(By.CSS_SELECTOR, ".central-featured a")
print("Total language links:", len(languages))

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

print("Final Page Title:", driver.title)

driver.quit()