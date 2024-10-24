'''Some website denied the access if you make request with headless(i.e without GUI) and on jupyter server ,we cant make request with GUI 
or without headless , In this case , we  can use pyvirtualdisplay which provide viirtual display and that enable us to make request with 
GUI   '''



from pyvirtualdisplay import Display
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

with Display():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('GUIrequiredwebsite.com')