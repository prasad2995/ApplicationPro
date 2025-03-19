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

def add_beneficiary(driver, data):
    try:
        WebElements.button_select_value(driver, 'Add Beneficiary', data['Relationship'])
        sleep(2)

    except Exception as e:
        logging.error(f'Error: Failed at adding Beneficiary - {e}')
        Utilities.take_screenshot(sheet_name, 'error')

def beneficiary_relationship(driver, data):
    try:
        WebElements.select_value(driver, 'Beneficiary Level', data['Beneficiary Level'])
        WebElements.enter_text(driver, 'Percentage', data['Percentage'])
        WebElements.click_button(driver, 'Save')

        Utilities.take_screenshot(sheet_name, 'beneficiary_relationship')

    except Exception as e:
        logging.error(f'Error - Failed at entering relationship details - {e}')
        Utilities.take_screenshot(sheet_name, 'error')



def Execute():
    try:
        data = ExcelLibrary.read_excel_data(sheet_name)
        WebElements.click_left_nav_menu(driver, 'Beneficiary')
        sleep(2)
        add_beneficiary(driver, data)
        beneficiary_relationship(driver, data)
        next_screen = data.get('Next_Screen')  # Using .get() to avoid KeyError
        if next_screen:
            if next_screen == 'End':
                print(f'Application creation has stopped at {sheet_name} screen')
            else:
                PageNavigator.navigate_screens(next_screen)
        else:
            logging.warning(f'Warning: "Next_Screen" column is missing in {sheet_name} sheet')
    except Exception as e:
        Utilities.take_screenshot(sheet_name, 'error')
        logging.error(f'Application creation failed at {sheet_name} screen - {e}')