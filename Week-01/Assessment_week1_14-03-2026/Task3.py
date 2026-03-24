from selenium import webdriver
import time

driver = webdriver.Chrome()

websites = [
    "https://www.thesouledstore.com",
    "https://www.nike.com",
    "https://www.bbc.com/news",
    "https://www.python.org"
]

for site in websites:
    time.sleep(3)
    driver.get(site)
    print("Page Title:", driver.title)

driver.quit()