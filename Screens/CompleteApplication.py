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
complete_application_text = "All required information has been gathered. Please click continue to proceed with the application. "

def verify_complete_application():
    try:
        # WebElements.verify_text(complete_application_text)
        WebElements.click_button(driver, 'Next')
        sleep(2)
        WebElements.wait_until_ele_load(driver, '//button//span[text()="Review Forms"]')
        WebElements.click_button(driver, 'Review Forms')
        sleep(5)
        WebElements.closeLastOpenedWindow()
        WebElements.click_button(driver, 'Next')

    except Exception as e:
        logging.error(f'Error: Failed at selecting Complete Application screen - {e}')

def signature(driver):
    try:
        sleep(5)
        WebElements.enter_text(driver, 'City', 'California')
        WebElements.select_value(driver, 'Signature Method', 'Mouse/Finger/Stylus')
        sleep(2)
        WebElements.select_checkbox(driver,'I have read the Terms of Use and eSignature Consent', 'Yes')
        sleep(2)
        WebElements.signatue()
        WebElements.click_button(driver, 'Apply My Signature ')
        sleep(5)
        logging.info(f'Signed successfully')
        WebElements.click_button(driver, 'OK')
        sleep(2)
        WebElements.click_button(driver, 'Next')

    except Exception as e:
        logging.error(f'Failed a signature - {e}')

def agent_report():
    try:
        sleep(5)
        for i in range(4):
            sleep(1)
            WebElements.click_button(driver, 'No')
        sleep(2)
        WebElements.click_button(driver, 'Next')
        sleep(5)
        WebElements.click_button(driver, 'Review Forms - Agent')
        WebElements.closeLastOpenedWindow()
        WebElements.click_button(driver, 'Next')
        sleep(2)
        # Attachements
        WebElements.click_button(driver, 'Next')
        sleep(5)
        signature(driver)
        WebElements.button_select_value(driver, 'Submit', 'Submit to Underwriting')
        sleep(20)
        WebElements.click_button(driver, 'OK')

    except Exception as e:
        print(f"Error in agent_report: {e}")





def Execute():
    sheet_name = os.path.splitext(os.path.basename(__file__))[0]
    try:
        data = ExcelLibrary.read_excel_data(sheet_name)
        WebElements.click_left_nav_menu(driver, 'Complete Application')
        sleep(5)
        verify_complete_application()
        signature(driver)
        agent_report()
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

