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

driver = IntializeDriver.driver
# Scroll to the element using ActionChains
actions = ActionChains(driver)

# Functions starts from here

def click_button(driver, button_name):
    index = '1'

    try:
        if "_" in button_name:
            button_name, index = button_name.rsplit("_", 1)
        # Try different XPath variations
        possible_xpaths = [
            f"(//button//span[text()='{button_name}'])[{index}]",
            f"(//button[text()='{button_name}'])[{index}]"
        ]

        element = None
        for xpath in possible_xpaths:
            element = driver.find_element(By.XPATH, xpath)
            if element:
                # Scroll to the element
                actions.move_to_element(element).perform()
                element.click()
                print(f'Clicked on "{button_name}"')
                return  # Exit the function after clicking

        raise NoSuchElementException(f'{button_name} button not found')

    except NoSuchElementException as e:
        logging.ERROR(f'Element not found. {e}')


def wait_until_ele_load(driver,element):
    try:
        WebDriverWait(driver, GlobalVariables.EleWaitTimeout).until(
            EC.element_to_be_clickable(('xpath', element)))

    except NoSuchElementException as e:
        logging.ERROR(f'element not found. {e}')


def choose_button(driver, element):
    try:
        element = "//lf-radiobutton[@value='newClient']//child::span/.."
        driver.find_element('xpath', element).click()
        print(f'{element} selected')

    except NoSuchElementException as e:
        logging.ERROR(f'{element} not found. {e}')


def enter_text(driver, element_name, input_text):
    try:
        if element_name.startswith("xpath="):
            element = element_name.replace("xpath=", "", 1).strip()
        elif "_" in element_name:
            element, index = element_name.split("_")
            element = f"(//span[text()='{element}']/..//..//child::input)[{index}]"
        else:
            element = f"//span[text()='{element_name}']/..//..//child::input"

        element = driver.find_element('xpath', element)
        actions.move_to_element(element).perform()
        element.clear()
        element.send_keys(input_text)
        print(f'Text entered in {element_name} field')

    except NoSuchElementException as e:
        logging.ERROR(f'{element_name} not found. {e}')


def select_checkbox(driver, element_name, state):
    try:
        # element = "//lpla-fd-checkbox[@label='"+ element_name +"']//lf-checkbox"
        element = f'//span[text()="{element_name}"]//..//..//lf-checkbox'
        checkbox = driver.find_element(By.XPATH, element)
        actions.move_to_element(checkbox).perform()
        if not checkbox.is_selected():
            checkbox.click()
            print(f'Selected the checkbox {element_name}')
        else:
            logging.warning(f'{element_name} is already selected')

    except Exception as e:
        logging.ERROR(f'Error: Check box is not selectable - {e}')


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
            print(f'Selected the {value} in {element_name} dropdown')
        else:
            logging.warning(f'{value} is not available to select in {element_name} dropdown')

    except NoSuchElementException as e:
        logging.ERROR(f'{element_name} not found. {e}')


def click_left_nav_menu(driver, menu_name):
    try:
        element = f"//li[@role='menuitem']//span[text()='{menu_name}']"
        element = driver.find_element(By.XPATH, element)
        actions.move_to_element(element).perform()
        element.click()

    except NoSuchElementException as e:
        logging.ERROR(f'Error: Left navigation menu item {menu_name} is not found - {e}')
