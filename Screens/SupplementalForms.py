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

def add_supplemental_forms(driver, data):
    try:
        if data['Supplemental Forms'] == 'Yes':
            WebElements.click_button(driver, 'Yes')
        elif data['Supplemental Forms'] == 'No':
            print(f'Supplemental forms are not added')
        sleep(2)
        Utilities.take_screenshot(sheet_name, 'add_supplemental_forms')

    except Exception as e:
        logging.error(f'Error: Failed at selecting Supplemental Forms - {e}')
        Utilities.take_screenshot(sheet_name, 'error')


def Execute():
    try:
        data = ExcelLibrary.read_excel_data(sheet_name)
        WebElements.click_left_nav_menu(driver, 'Supplemental Forms')
        sleep(5)
        add_supplemental_forms(driver, data)
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