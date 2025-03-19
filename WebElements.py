from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import GlobalVariables
import IntializeDriver
import logging
import os
import webbrowser

# Initialize driver
driver = IntializeDriver.driver

# Set up logging
log_file = "execution_log.html"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(log_file, mode="w"), logging.StreamHandler()]
)

# Scroll to the element using ActionChains
actions = ActionChains(driver)


# Functions start here

def click_button(driver, button_name):
    index = '1'
    try:
        if "_" in button_name:
            button_name, index = button_name.rsplit("_", 1)

        possible_xpaths = [
            f"(//button//span[text()='{button_name}'])[{index}]",
            f"(//button[text()='{button_name}'])[{index}]"
        ]

        element = None
        for xpath in possible_xpaths:
            element = driver.find_element(By.XPATH, xpath)
            if element:
                actions.move_to_element(element).perform()
                element.click()
                logging.info(f'Clicked on "{button_name}"')
                return

        raise NoSuchElementException(f'{button_name} button not found')

    except NoSuchElementException as e:
        logging.error(f'Element not found: {e}')


def wait_until_ele_load(driver, element):
    try:
        WebDriverWait(driver, GlobalVariables.EleWaitTimeout).until(
            EC.element_to_be_clickable((By.XPATH, element)))
        logging.info(f'Element {element} is clickable now')

    except NoSuchElementException as e:
        logging.error(f'Element not found: {e}')


def enter_text(driver, element_name, input_text):
    try:
        if element_name.startswith("xpath="):
            element = element_name.replace("xpath=", "", 1).strip()
        elif "_" in element_name:
            element, index = element_name.split("_")
            element = f"(//span[text()='{element}']/..//..//child::input)[{index}]"
        else:
            element = f"//span[text()='{element_name}']/..//..//child::input"

        element = driver.find_element(By.XPATH, element)
        actions.move_to_element(element).perform()
        element.clear()
        element.send_keys(input_text)
        logging.info(f'Text "{input_text}" entered in "{element_name}" field')

    except NoSuchElementException as e:
        logging.error(f'{element_name} not found: {e}')


def select_checkbox(driver, element_name, state):
    try:
        element = f'//span[text()="{element_name}"]//..//..//lf-checkbox'
        checkbox = driver.find_element(By.XPATH, element)
        actions.move_to_element(checkbox).perform()
        if not checkbox.is_selected():
            checkbox.click()
            logging.info(f'Selected the checkbox "{element_name}"')
        else:
            logging.warning(f'Checkbox "{element_name}" is already selected')

    except Exception as e:
        logging.error(f'Error: Check box "{element_name}" is not selectable - {e}')



def select_value(driver, element_name, value):
    index = '1'
    try:
        if element_name.startswith("xpath="):
            element = element_name.replace("xpath=", "", 1).strip()
        elif "_" in element_name:
            element, index = element_name.split("_")
            element = f"(//label//span[text()='{element}']/..//parent::div//child::lf-select)[{index}]"
        else:
            element = f"//label//span[text()='{element_name}']/..//parent::div//child::lf-select"

        element = driver.find_element(By.XPATH, element)
        actions.move_to_element(element).perform()
        element.click()

        possible_xpaths = [
            f'//lf-dropdown-panel//span[text()="{value}"]',
            f'//lf-select//span[text()="{value}"]'
        ]

        for xpath in possible_xpaths:
            try:
                element = driver.find_element(By.XPATH, xpath)
                break
            except NoSuchElementException:
                continue

        if element:
            element.click()
            logging.info(f'Selected "{value}" in "{element_name}" dropdown')
        else:
            logging.warning(f'Value "{value}" is not available in "{element_name}" dropdown')

    except NoSuchElementException as e:
        logging.error(f'{element_name} not found: {e}')

def button_select_value(driver, element_name, value):
    index = '1'
    try:
        if element_name.startswith("xpath="):
            element = element_name.replace("xpath=", "", 1).strip()
        elif "_" in element_name:
            element, index = element_name.split("_")
            element = f"(//button//span[text()='{element}'])[{index}]"
        else:
            element = f"//button//span[text()='{element_name}']"

        element = driver.find_element(By.XPATH, element)
        actions.move_to_element(element).perform()
        element.click()

        element_xpath = f'//lf-tiered-menu-sub//span[text()="{value}"]'
        element = driver.find_element(By.XPATH, element_xpath)
        if element:
            element.click()
            logging.info(f'Selected "{value}" in "{element_name}" dropdown')
        else:
            logging.warning(f'Value "{value}" is not available in "{element_name}" dropdown')

    except NoSuchElementException as e:
        logging.error(f'{element_name} not found: {e}')


def click_left_nav_menu(driver, menu_name):
    try:
        element = f"//a[@role='tab']//span[text()='{menu_name}']"
        element = driver.find_element(By.XPATH, element)
        actions.move_to_element(element).perform()
        element.click()
        logging.info(f'Clicked on menu "{menu_name}"')

    except NoSuchElementException as e:
        logging.error(f'Error: Left navigation menu item "{menu_name}" not found - {e}')


def verify_text(text):
    try:
        element_name = f"//div[text()='{text}']"
        element = driver.find_element(element_name).is_displayed()
        if element:
            logging.info(f'The text "{element_name}" is available in UI')
        else:
            logging.error(f'The text "{element_name}" is not available in UI')

    except NoSuchElementException as e:
        logging.error(f'Error: Failed at verifying text - {e}')

def closeLastOpenedWindow():
    try:
        sleep(5)
        window_handles = driver.window_handles
        window_count = len(window_handles)  # Get the number of open windows
        logging.info(f'Total windows open: {window_count}')
        windowIndexNumber = window_count - 1

        driver.switch_to.window(window_handles[windowIndexNumber])
        driver.close()
        sleep(1)
        driver.switch_to.window(window_handles[0])

    except Exception as e:
        logging.error(f'Failed to switch between windows - {e}')


def signature():
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        # Locate the canvas element
        canvas = driver.find_element(By.ID, "signature")

        # # Get canvas location and size
        # canvas_location = canvas.location
        # canvas_size = canvas.size
        # start_x = canvas_location['x'] + 10  # Offset to start within the canvas
        # start_y = canvas_location['y'] + 10  # Offset to start within the canvas

        # Create an ActionChain for drawing
        actions = ActionChains(driver)
        actions.move_to_element_with_offset(canvas, 10, 10)  # Move to starting position
        actions.click_and_hold()  # Click and hold to simulate drawing

        for i in range(15):  # Adjust iterations for more curves
            actions.move_by_offset(15, -10)  # Move right-up
            actions.move_by_offset(10, 15)  # Move right-down
            actions.move_by_offset(-15, 10)  # Move left-down
            actions.move_by_offset(-10, -15)  # Move left-up

        actions.release()  # Release the mouse button
        actions.perform()  # Execute the action

        # Wait and close browser (Optional)
        logging.info(f'Signed successfully')

    except Exception as e:
        logging.error(f'Failed at signature - {e}')

def getText(driver, element):
    try:
        text = driver.find_element(By.XPATH, element).text
        logging.info(f'element {element} text is {text}')
        return text

    except Exception as e:
        logging.error((f'Failed to get the text - {e}'))