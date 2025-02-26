from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd
import WebElements
import GlobalVariables
import IntializeDriver
import os
import Screens.PageNavigator as PageNavigator

driver = IntializeDriver.driver

# XPaths
username_xpath = "//input[@id='userName']"
password_xpath = "//input[@id='password']"

def login(driver, data):
    try:
        driver.maximize_window()
        driver.get(data['Application_URL'])  # Use URL from dictionary
        WebElements.wait_until_ele_load(driver, username_xpath)
        driver.find_element('xpath', username_xpath).send_keys(data['UserName'])
        driver.find_element('xpath', password_xpath).send_keys(data['Password'])
        WebElements.click_button(driver, 'Login')
        WebElements.wait_until_ele_load(driver, "//button//span[text()='Create Application']")
        print('Login successful')
    except NoSuchElementException as e:
        print(f'Login failed. Element not found {e}')
    except TimeoutException as e:
        print(f'Timeout occurred during login: {e}')

def read_excel_data(sheet_name):
    # Load the Excel sheet
    df = pd.read_excel(GlobalVariables.excel_path, sheet_name)

    # Convert each row to a dictionary and store in a list
    applications = df.to_dict(orient='records')

    # Example: Accessing the first application's details
    for app in applications:
        print(f"Processing Application: {app}")
        # Return the entire application dictionary
        return app



def Execute():
    sheet_name = os.path.splitext(os.path.basename(__file__))[0]
    data = read_excel_data(sheet_name)
    login(driver, data)
    PageNavigator.navigate_screens(data['Next_Screen'])

def end_execution():
    driver.quit()
