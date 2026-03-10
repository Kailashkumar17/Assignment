from check_status import status_code
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import logging
dt=datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
logging.basicConfig(filename=f"E:\\Assignment\\Logs\\Toggleinvalid\\toggleinvalidnine.log.{dt}",
                    level=logging.INFO,
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    force=True)
logging.info("Toggle operation")
def test_toggle_invalidinput(login):
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
        time.sleep(60)
        if status_code()==200:
            logging.info(f"Passed. The API is up and running and code is {status_code()}")
        else:
            logging.info(f"Failed. The API is down and code is {status_code()}")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='radix-:r4:'] svg"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Configuration')]"))).click()
        logging.info("clicked on the configuration button")
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Advanced Settings']"))).click()
        logging.info("clicked on the Advanced settings button")
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[.//input[@name='autoSuspend']]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='auto_stop_minutes']"))).send_keys(Keys.CONTROL + "a", Keys.DELETE)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='auto_stop_minutes']"))).send_keys(9)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Save']"))).click()
        logging.info("sending the boundary values. should throw an error")
        #browser.save_screenshot(f".\\Screenshots\\Input_NINE_ERROR{dt}.png")
        #time.sleep(5)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Save']"))).click()
        browser.save_screenshot(f".\\Screenshot\\Invalid\\Input_NINE_ERROR{dt}.png")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"svg[title='Close']"))).click()
        time.sleep(5)
    except TimeoutException as e:
        logging.error("Timeout occurred while locating element")
        browser.save_screenshot(f".\\Screenshot\\Invalid\\Error_{dt}.png")
        raise e

    except NoSuchElementException as e:
        logging.error("Element not found")
        browser.save_screenshot(f".\\Screenshot\\Invalid\\Error_{dt}.png")
        raise e

    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        browser.save_screenshot(f".\\Screenshot\\Invalid\\Error_{dt}.png")
        raise e


