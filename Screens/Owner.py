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

def add_owner(driver, data):
    try:
        WebElements.click_button(driver, 'Add Owner')
        WebElements.select_value(driver, 'Type', data['Type'])
        WebElements.select_value(driver, 'Relationship', data['Relationship'])
        WebElements.click_button(driver, 'OK')
        sleep(2)
        Utilities.take_screenshot(sheet_name, 'add_owner')

    except NoSuchElementException as e:
        logging.error(f'Error: Failed at Adding Owner - {e}')
        Utilities.take_screenshot(sheet_name, 'error')

def owner_relationship(driver, data):
    try:
        if data['Relationship'] == 'Insured':
            WebElements.click_button(driver, 'Save' )
            Utilities.take_screenshot(sheet_name, 'owner_relationship')
    except NoSuchElementException as e:
        logging.error(f'Error - Failed at relationship details - {e}')
        Utilities.take_screenshot(sheet_name, 'error')


def Execute():
    try:
        data = ExcelLibrary.read_excel_data(sheet_name)
        WebElements.click_left_nav_menu(driver, 'Owner')
        sleep(5)
        if GlobalVariables.ownerIsInsured == 'Yes':
            Utilities.take_screenshot(sheet_name, 'add_owner')
            print(f'Owner is the insured')
        else:
            add_owner(driver, data)
            owner_relationship(driver, data)
        next_screen = data.get('Next_Screen')  # Using .get() to avoid KeyError
        if next_screen:
            if next_screen == 'End':
                print(f'Application creation has stopped at {sheet_name} screen')
            else:
                PageNavigator.navigate_screens(next_screen)
        else:
            logging.warning(f'Warning: "Next_Screen" column is missing in {sheet_name} sheet')
    except:
        Utilities.take_screenshot(sheet_name, 'error')
        logging.error(f'Application creation failed at {sheet_name} screen')