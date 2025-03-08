from time import sleep
from selenium.common import NoSuchElementException
import Utilities
import WebElements
import GlobalVariables
import ExcelLibrary
import os
import Screens.PageNavigator as PageNavigator
import sys
import IntializeDriver
import logging
logging.basicConfig(level=logging.ERROR)

driver = IntializeDriver.driver

def add_existing_insurance(driver, data):
    try:
        if data['Physician Information'] == 'Yes':
            WebElements.click_button(driver, 'Yes')
        elif data['Physician Information'] == 'No':
            WebElements.click_button(driver, 'No')
        sleep(2)

    except NoSuchElementException as e:
        logging.error(f'Error: Failed at selecting Physician Information - {e}')


def Execute():
    sheet_name = os.path.splitext(os.path.basename(__file__))[0]
    try:
        data = ExcelLibrary.read_excel_data(sheet_name)
        WebElements.click_left_nav_menu(driver, 'Physician Information')
        sleep(5)
        add_existing_insurance(driver, data)
        next_screen = data.get('Next_Screen')  # Using .get() to avoid KeyError
        if next_screen:
            if next_screen == 'End':
                print(f'Application creation has stopped at {sheet_name} screen')
            else:
                PageNavigator.navigate_screens(next_screen)
        else:
            logging.warning(f'Warning: "Next_Screen" column is missing in {sheet_name} sheet')
    except:
        Utilities.take_screenshot(sheet_name, 'execute_error')
        logging.error(f'Application creation failed at {sheet_name} screen')