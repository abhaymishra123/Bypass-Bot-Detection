import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def proxy(driver, website):
    driver.get("https://plainproxies.com/resources/free-web-proxy")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div/div/form/div/input").send_keys(website)
    driver.find_element(By.XPATH, '''/html/body/section/div/div/div/form/div/button''').click()
    time.sleep(5)
def proxy(driver, website):
    driver.get("https://plainproxies.com/resources/free-web-proxy")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div/div/form/div/input").send_keys(website)
    driver.find_element(By.XPATH, '''/html/body/section/div/div/div/form/div/button''').click()
    time.sleep(5)