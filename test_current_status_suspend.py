from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import logging
import time
from check_status import status_code
dt=datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
logging.basicConfig(filename=f"E:\\Assignment\\Logs\\Current_status\\current_status.log.{dt}",
                    level=logging.INFO,
                    format='%(asctime)s-%(levelname)s-%(message)s',
                    force=True)
logging.info("Logs capture begins")
def test_resume_manually(login):
    browser=login
    wait = WebDriverWait(browser, 20)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[id='radix-:r4:'] svg"))).click()
        #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"//button[@data-baseweb='button'][.//svg[@title='Overflow']]"))).click()
        logging.info("clicked on the radix button")
        time.sleep(3)
        browser.save_screenshot(f".\\Screenshot\\Toresume\\Beforeresume_{dt}.png")
        time.sleep(2)
        textdata=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'Resume')]")))
        status=textdata.text
        assert status == "Resume", logging.info("The machine is disabled")
        print(status)
        logging.info(f'Current status is disabled.We can {status}')
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Resume')]"))).click()
        time.sleep(5)
        browser.save_screenshot(f".\\Screenshot\\Toresume\\Resume_{dt}.png")
        logging.info("clicked on the Resume button")
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Confirm']"))).click()
        time.sleep(30)
        logging.info("Checking with API code whether it is working or not")
        assert status_code()==200,logging.info("Failed, API is not working")
        logging.info("Passed, API is up and running")
        #code=status_code()
        '''
        if status_code()==200:
            logging.info("Passed,the API is up and running")
        else:
            logging.info("Failed,the API is not running")
        '''
        logging.info(f"Printing the current status is {status_code()}")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"button[id='radix-:r4:'] svg"))).click()
        time.sleep(5)
        browser.save_screenshot(f".\\Screenshot\\Toresume\\ResumeStatus_{dt}.png")
    except TimeoutException as e:
        logging.error("Timeout occurred while locating element")
        browser.save_screenshot(f".\\Screenshot\\Toresume\\Error_{dt}.png")
        raise e

    except NoSuchElementException as e:
        logging.error("Element not found")
        browser.save_screenshot(f".\\Screenshot\\Toresume\\Error_{dt}.png")
        raise e

    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")
        browser.save_screenshot(f".\\Screenshot\\Toresume\\Error_{dt}.png")
        raise e









