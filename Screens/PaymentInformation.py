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
sheet_name = os.path.splitext(os.path.basename(__file__))[0]

def add_payment_information(driver, data):
    try:
        WebElements.select_value(driver, 'Cash With Application', data['Cash With Application'])
        Utilities.take_screenshot(sheet_name, 'add_payment_information')
        sleep(2)

    except NoSuchElementException as e:
        logging.error(f'Error: Failed at adding Payment Information - {e}')


def Execute():
    try:
        data = ExcelLibrary.read_excel_data(sheet_name)
        WebElements.click_left_nav_menu(driver, 'Payment Information')
        sleep(5)
        add_payment_information(driver, data)
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