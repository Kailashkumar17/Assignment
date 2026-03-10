import logging
import time
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from check_status import status_code

dt = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

logging.basicConfig(
    filename=f"E:\\Assignment\\Logs\\Resumeaftersuspend\\Resumeaftersuspend_{dt}.log",
    level=logging.INFO,
    format='%(asctime)s-%(levelname)s-%(message)s',
    force=True
)

def test_auto_resume_after_suspend(login):
    browser = login
    wait = WebDriverWait(browser, 20)
    try:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='radix-:r4:'] svg"))).click()
        logging.info("clicked on the radix button")
        textdata = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Resume')]")))
        status = textdata.text
        assert status == "Resume", logging.info("The machine is disabled")
        logging.info(f'Current status is disabled.We can {status}')
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Resume')]"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Confirm']"))).click()
        time.sleep(60)
        if status_code()==200:
            logging.info(f"Passed. The API is up and running and status code is {status_code()}")
        else:
            logging.info(f"Failed. The API is down and status code is {status_code()}")
        time.sleep(5)
        browser.save_screenshot(f".\\Screenshot\\Resumeaftersuspend\\Beforeresumeandsuspend{dt}.png")
        logging.info("clicked on the Resume button")
        logging.info("Now after clicking the resume the button, wait for 10 min and it should suspend after 10 min")
        #wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Confirm']"))).click()
        time.sleep(900)
        #browser.refresh()
        #time.sleep(10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[id='radix-:r4:'] svg"))).click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Resume')]"))).click()
        logging.info("Resuming after 10 min with trigger code")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Confirm']"))).click()
        time.sleep(10)
        logging.info("Checking the API is running or not")
        time.sleep(60)
        if status_code() == 200:
            logging.info(f"The machine has been resumed and the API is up and running and status code is {status_code()}")
        else:
            logging.info(f"The API is down and status code is {status_code()}")
        time.sleep(3)
        browser.save_screenshot(f".\\Screenshot\\Resumeaftersuspend\\Afterresumeandsuspend{dt}.png")
    except TimeoutException as e:
        logging.error("Timeout occurred")
        browser.save_screenshot(f".\\Screenshot\\Resumeaftersuspend\\Error_{dt}.png")
        raise e
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        browser.save_screenshot(f".\\Screenshot\\Resumeaftersuspend\\Error_{dt}.png")
        raise e

