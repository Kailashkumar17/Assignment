import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import config


@pytest.fixture(scope="session")
def login():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(config.url)
    time.sleep(5)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='username']"))).send_keys(config.username)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@type='password']"))).send_keys(config.password)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']"))).click()
    time.sleep(5)


    yield browser

    time.sleep(10)
    wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='bx dj by dk c0 c1 dl dm']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH,"//div[normalize-space()='Logout']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Got it!']"))).click()
    browser.quit()

    




