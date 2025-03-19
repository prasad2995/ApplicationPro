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

def add_underwriting_questions(driver, data):
    try:
        if data['Underwriting Questions'] == 'Yes':
            WebElements.click_button(driver, 'Yes')
        elif data['Underwriting Questions'] == 'No':
            WebElements.click_button(driver, 'No')
        sleep(2)
        Utilities.take_screenshot(sheet_name, 'add_underwriting_questions')

    except NoSuchElementException as e:
        logging.error(f'Error: Failed at selecting Underwriting Questions - {e}')
        Utilities.take_screenshot(sheet_name, 'error')


def Execute():
    try:
        data = ExcelLibrary.read_excel_data(sheet_name)
        WebElements.click_left_nav_menu(driver, 'Underwriting Questions')
        sleep(2)
        add_underwriting_questions(driver, data)
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