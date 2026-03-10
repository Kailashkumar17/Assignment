import logging
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
from check_status import status_code
dt=datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
logging.basicConfig(filename=f"E:\\Assignment\\Logs\\Toogleoff\\toggleoffbehaviour.log.{dt}",
                    level=logging.INFO,
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    force=True)
logging.info("Toggle operation")
def test_toggle_OFF_behaviour(login):
    browser=login
    wait=WebDriverWait(browser, 20)
    try:

        logging.info(f"Click on the configuration")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='radix-:r4:'] svg"))).click()
        #time.sleep(5)
        logging.info("clicked on the radix button")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Resume')]"))).click()
        #time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Confirm']"))).click()
        #time.sleep(60)
        time.sleep(60)
        if status_code()==200:
            logging.info(f"Passed. API is up and running and status is {status_code()}")
        else:
            logging.info(f"Failed. API is down and status is {status_code()}")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='radix-:r4:'] svg"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Configuration')]"))).click()
        logging.info("clicked on the configuration button")
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Advanced Settings']"))).click()
        logging.info("clicked on the Advanced settings button")
        time.sleep(5)
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//label[.//input[@name='autoSuspend']]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//label[.//input[@name='autoSuspend']]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))).click()
        logging.info("Autosuspend button was enabled and disabled. So the machine will be in disabled state")
        browser.refresh()
        time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Workspace-1']"))).click()
        browser.save_screenshot(f".\\Screenshot\\Toggleoff\\Disablebutton_{dt}.png")
        time.sleep(5)
    except TimeoutException as e:
        logging.error("Timeout occurred while locating element")
        browser.save_screenshot(f".\\Screenshot\\Toggleoff\\Error_{dt}.png")
        raise e

    except NoSuchElementException as e:
        logging.error("Element not found")
        browser.save_screenshot(f".\\Screenshot\\Toggleoff\\Error_{dt}.png")
        raise e
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        browser.save_screenshot(f".\\Screenshot\\Toggleoff\\Error_{dt}.png")
        raise e



