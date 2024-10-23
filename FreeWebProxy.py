import time
def proxy(driver, website):
    driver.get("https://plainproxies.com/resources/free-web-proxy")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/section/div/div/div/form/div/input").send_keys(website)
    driver.find_element(By.XPATH, '''/html/body/section/div/div/div/form/div/button''').click()
    time.sleep(5)
