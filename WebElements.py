from time import sleep

from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import GlobalVariables


# Functions starts from here

def click_button(driver, button_name):
    try:
        # Try different XPath variations
        possible_xpaths = [
            f"//button//span[text()='{button_name}']",
            f"//button[text()='{button_name}']"
        ]

        element = None
        for xpath in possible_xpaths:
            element = driver.find_element(By.XPATH, xpath)
            if element:
                element.click()
                print(f'Clicked on "{button_name}"')

    except NoSuchElementException as e:
        print(f'Element not found. {e}')


def wait_until_ele_load(driver,element):
    try:
        WebDriverWait(driver, GlobalVariables.EleWaitTimeout).until(
            EC.element_to_be_clickable(('xpath', element)))

    except NoSuchElementException as e:
        print(f'element not found. {e}')


def choose_button(driver, element):
    try:
        element = "//lf-radiobutton[@value='newClient']//child::span/.."
        driver.find_element('xpath', element).click()
        print(f'{element} selected')

    except NoSuchElementException as e:
        print(f'{element} not found. {e}')


def enter_text(driver, element, input_text):
    try:
        if element.startswith("xpath="):
            element = element.replace("xpath", "", 1).strip()
        else:
            element = "//span[text()='" + element + "']/..//..//child::input"

        driver.find_element('xpath', element).send_keys(input_text)
        print(f'Text is entered in {element} field')

    except NoSuchElementException as e:
        print(f'{element} not found. {e}')


def select_checkbox(driver, element_name, state):
    try:
        element = "//lpla-fd-checkbox[@label='"+ element_name +"']//lf-checkbox"
        checkbox = driver.find_element(By.XPATH, element)
        if not checkbox.is_selected():
            checkbox.click()
            print(f'Selected the checkbox {element_name}')
        else:
            print(f'{element_name} is already selected')

    except Exception as e:
        print(f'Error: Check box is not selectable - {e}')


def select_value(driver, element, value):
    try:
        element_xpath = "//label//span[text()='"+ element +"']/..//parent::div//child::lf-select"
        driver.find_element(By.XPATH, element_xpath).click()

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
            print(f'Selected the value {element}')
        else:
            print(f'{element} not found to select')
    except NoSuchElementException as e:
        print(f'{element} not found. {e}')
