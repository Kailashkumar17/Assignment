from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from check_status import status_code
import time
import logging
dt=datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
logging.basicConfig(filename=f"E:\\Assignment\\Logs\\ToggleAutoresume\\toggleautoresume.log.{dt}",
                    level=logging.INFO,
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    force=True)
logging.info("Toggle operation")

def test_toggle_autoresume(login):
    browser=login
    try:
        wait = WebDriverWait(browser, 20)
        logging.info(f"Click on the configuration")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='radix-:r4:'] svg"))).click()
        #time.sleep(5)
        logging.info("clicked on the radix button")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Resume')]"))).click()
        #time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Confirm']"))).click()
        #time.sleep(60)
        time.sleep(30)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='radix-:r4:'] svg"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Configuration')]"))).click()
        logging.info("clicked on the configuration button")
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Advanced Settings']"))).click()
        logging.info(f"Autoenable button is enabled")
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[.//input[@name='enable_auto_start']]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))).click()
        time.sleep(10)
        if status_code()==200:
            logging.info(f"API is up and running and status code is {status_code()}")
        else:
            logging.error(f"API is failed to run")
        browser.refresh()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='radix-:r4:'] svg"))).click()
        browser.save_screenshot(f".\\Screenshot\\AutoResume\\Autoresumeenable_{dt}.png")
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Workspace-1']"))).click()
        time.sleep(3)
        browser.save_screenshot(f".\\Screenshot\\AutoResume\\AutoresumeenableDetails_{dt}.png")
        time.sleep(5)
    except TimeoutException as e:
        logging.error("Timeout occurred while locating element")
        browser.save_screenshot(f".\\Screenshot\\AutoResumedisable\\Error_{dt}.png")
        raise e

    except NoSuchElementException as e:
        logging.error("Element not found")
        browser.save_screenshot(f".\\Screenshot\\AutoResumedisable\\Error_{dt}.png")
        raise e

    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        browser.save_screenshot(f".\\Screenshot\\AutoResumedisable\\Error_{dt}.png")
        raise e


