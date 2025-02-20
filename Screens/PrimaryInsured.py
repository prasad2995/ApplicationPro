from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import AppPro.WebElements as WebElements
import AppPro.GlobalVariables as GlobalVariables
import AppPro.IntializeDriver as IntializeDriver
import os
import AppPro.Screens.PageNavigator as PageNavigator

driver = IntializeDriver.driver

#xpaths
primary_address_line1_xpath = "//span[text()='Primary Address Line 1']/..//..//child::input"


#fuctions
def personal_information(driver, data):
    WebElements.wait_until_ele_load(driver, primary_address_line1_xpath)
    WebElements.enter_text(driver, 'Primary Address Line 1', data['Primary_Address_Line_1'])
    WebElements.enter_text(driver, 'Primary Address Line 2', data['Primary_Address_Line_2'])
    WebElements.enter_text(driver, 'City', data['City'])
    WebElements.select_value(driver, 'State', data['State'])
    WebElements.enter_text(driver, 'Zip Code', data['Zip_Code'])
    WebElements.enter_text(driver, 'Home Phone', data['Home_Phone'])
    if data['Insured_is_Owner'] == 'Yes':
        WebElements.select_checkbox (driver, 'Insured is Owner', data['Insured_is_Owner'])
    if data['Insured_is_Payor'] == 'Yes':
        WebElements.select_checkbox(driver, 'Insured is Payor', data['Insured_is_Payor'])
    WebElements.enter_text(driver, 'Work Phone', data['Work_Phone'])
    WebElements.enter_text(driver, 'Cell Phone', data['Cell_Phone'])
    WebElements.select_value(driver, 'Preferred Method of Contact', data['Preferred_Method_of_Contact'])
    WebElements.enter_text(driver, 'Email Address', data['Email_Address'])
    WebElements.enter_text(driver, 'Social Security Number', data['Social_Security_Number'])
    WebElements.select_value(driver, 'Marital Status', data['Marital_Status'])
    WebElements.enter_text(driver, 'xpath=//input[@aria-label="Centimeters"]', data['Height'])
    WebElements.enter_text(driver, 'xpath=//input[@aria-label="Kilograms"]', data['Weight'])
    sleep(10)



def read_excel_data(sheet_name):
    # Load the Excel sheet
    df = pd.read_excel(GlobalVariables.excel_path, sheet_name)

    # Convert each row to a dictionary and store in a list
    applications = df.to_dict(orient='records')

    # Example: Accessing the first application's details
    for app in applications:
        print(f"Processing Application: {app}")
    return app


def Execute():
    sheet_name = os.path.splitext(os.path.basename(__file__))[0]
    data = read_excel_data(sheet_name)
    personal_information(driver, data)
    if 'Next Screen' in data:
        if data['NextScreen']:
            PageNavigator.navigate_screens(data['NextScreen'])
        else:
            print(f'Warning: Next Screen column is missing in {sheet_name} sheet')
    else:
        print(f'Error - ')
