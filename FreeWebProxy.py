import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def proxy1(driver, website):
    driver.get("https://plainproxies.com/resources/free-web-proxy")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div/div/form/div/input").send_keys(website)
    driver.find_element(By.XPATH, '''/html/body/section/div/div/div/form/div/button''').click()
    time.sleep(5)

def proxy2(driver,website):
    driver.get("https://hide.me/en/proxy")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="u"]').send_keys(website)
    driver.find_element(By.XPATH, '//*[@id="hide_register_save"]').click()
    time.sleep(5)

def proxy3(driver,website):
    driver.get("https://proxyium.com/")
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div[2]/form/div[2]/input').send_keys(website)
    driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div[2]/form/div[2]/button').click()
    time.sleep(5)