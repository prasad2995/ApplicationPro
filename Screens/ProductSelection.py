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

def product_selection(driver, data):
    try:
        print(f'No data to be filled in {sys._getframe().f_code.co_name}')

    except NoSuchElementException as e:
        logging.error(f'Error: Failed at Product Selection section - {e}')

def product_information(driver, data):
    try:
        WebElements.enter_text(driver, 'Face Amount', data['Face_Amount'])
        WebElements.select_value(driver, 'Class', data['Class'])
        WebElements.select_value(driver, 'Payment Mode', data['Payment_Mode'])
        Utilities.take_screenshot(sheet_name, 'product_information')

    except NoSuchElementException as e:
        logging.error(f'Error - Failed at Product Information section - {e}')
        Utilities.take_screenshot(sheet_name, 'error')



def rider(driver, data):
    try:
        if data['Waiver_of_Premium'] == 'Yes':
            WebElements.select_checkbox(driver, 'Waiver of Premium', data['Waiver_of_Premium'])
        if data['Accidental_Death_Benefit'] == 'Yes':
            WebElements.select_checkbox(driver, 'Accidental Death Benefit', data['Accidental_Death_Benefit'])
        if data['Accidental_Death_Benefit'] == 'Yes':
            sleep(2)
            WebElements.enter_text(driver, 'Amount_1', data['Accidental_Death_Benefit_Amount'])
        if data['Primary_Insured_Rider'] == 'Yes':
            WebElements.select_checkbox(driver, 'Primary Insured Rider', data['Primary_Insured_Rider'])
            sleep(2)
            WebElements.enter_text(driver, 'Amount_2', data['Primary_Insured_Rider_Amount'])
        if data['Childrens_Insurance_Rider'] == 'Yes':
            WebElements.select_checkbox(driver, 'Childrens Insurance Rider', data['Childrens_Insurance_Rider'])
            sleep(2)
            WebElements.enter_text(driver, 'Units', data['Childrens_Insurance_Rider_Units'])
        if data['Other_Insured_Rider'] == 'Yes':
            WebElements.select_checkbox(driver, 'Other Insured Rider', data['Other_Insured_Rider'])
        Utilities.take_screenshot(sheet_name, 'rider')

    except NoSuchElementException as e:
        logging.error(f'Error: Failed at rider selection - {e}')
        Utilities.take_screenshot(sheet_name, 'error')

def Execute():
    try:
        data = ExcelLibrary.read_excel_data(sheet_name)
        WebElements.click_left_nav_menu(driver, 'Product Selection')
        sleep(5)
        product_selection(driver, data)
        product_information(driver, data)
        rider(driver, data)
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