from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import WebElements
import GlobalVariables
import IntializeDriver
import os
import Screens.PageNavigator as PageNavigator
import Utilities

driver = IntializeDriver.driver
sheet_name = os.path.splitext(os.path.basename(__file__))[0]

#xpaths
primary_address_line1_xpath = "//span[text()='Primary Address Line 1']/..//..//child::input"

#fuctions
def personal_information(driver, data):
    WebElements.wait_until_ele_load(driver, primary_address_line1_xpath)
    sleep(2)
    WebElements.enter_text(driver, 'Primary Address Line 1', data['Primary_Address_Line_1'])
    WebElements.enter_text(driver, 'Primary Address Line 2', data['Primary_Address_Line_2'])
    WebElements.enter_text(driver, 'City_1', data['City_1'])
    WebElements.select_value(driver, 'State_1', data['State_1'])
    WebElements.enter_text(driver, 'Zip Code', data['Zip_Code'])
    WebElements.enter_text(driver, 'Home Phone', data['Home_Phone'])
    if data['Insured_is_Owner'] == 'Yes':
        WebElements.select_checkbox (driver, 'Insured is Owner', data['Insured_is_Owner'])
        GlobalVariables.ownerIsInsured = data['Insured_is_Owner']
    if data['Insured_is_Payor'] == 'Yes':
        WebElements.select_checkbox(driver, 'Insured is Payor', data['Insured_is_Payor'])
        GlobalVariables.payorIsInsured = data['Insured_is_Payor']
    WebElements.enter_text(driver, 'Work Phone', data['Work_Phone'])
    WebElements.enter_text(driver, 'Cell Phone', data['Cell_Phone'])
    WebElements.select_value(driver, 'Preferred Method of Contact', data['Preferred_Method_of_Contact'])
    WebElements.enter_text(driver, 'Email Address', data['Email_Address'])
    WebElements.enter_text(driver, 'Social Security Number', data['Social_Security_Number'])
    WebElements.select_value(driver, 'Marital Status', data['Marital_Status'])
    WebElements.enter_text(driver, 'xpath=//input[@aria-label="Centimeters"]', data['Height'])
    WebElements.enter_text(driver, 'xpath=//input[@aria-label="Kilograms"]', data['Weight'])

    #Selection for question "Have you ever used any form of tobacco, nicotine-based products, nicotine substitutes, or nicotine delivery systems?*"
    WebElements.click_button(driver, data['Tobacco'])
    Utilities.take_screenshot(sheet_name, 'personal_information')


def employment_information(driver, data):
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # sleep(2)
    WebElements.select_value(driver, 'Work Status', data['Work_Status'])
    if data['Work_Status'] == 'Employed':
        WebElements.wait_until_ele_load(driver, "//label//span[text()='Occupational Duties']/..//parent::div//child::lf-select")
        WebElements.select_value(driver, 'Occupational Duties', data['Occupational_Duties'])
        WebElements.enter_text(driver, 'Employer Name', data['Employer_Name'])
        WebElements.enter_text(driver, 'Employer Address Line 1', data['Employer_Address_Line_1'])
        WebElements.enter_text(driver, 'Employer Address Line 2', data['Employer_Address_Line_2'])
        WebElements.enter_text(driver, 'City_2', data['City'])
        WebElements.select_value(driver, 'State_2', data['State_2'])
        WebElements.enter_text(driver, 'Zip Code', data['Zip_Code'])
    if data['Work_Status'] == 'Other':
        WebElements.enter_text(driver, 'Other', data['Other'])
    Utilities.take_screenshot(sheet_name, 'employment_information')


def additional_information(driver, data):
    WebElements.select_value(driver, 'Citizenship', data['Citizenship'])
    WebElements.select_value(driver, 'Country of Birth', data['Country_of_Birth'])
    if data['Country_of_Birth'] == 'United States Of America':
        WebElements.wait_until_ele_load(driver, "//label//span[text()='State of Birth']/..//parent::div//child::lf-select")
        WebElements.select_value(driver, 'State of Birth', data['State_of_Birth'])
    # WebElements.enter_text(driver, 'Driver License Number', data['Driver_License_Number'])
    # WebElements.enter_text(driver, 'State of Issue', data['State_of_Issue'])
    Utilities.take_screenshot(sheet_name, 'additional_information')





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
    data = read_excel_data(sheet_name)
    personal_information(driver, data)
    employment_information(driver, data)
    additional_information(driver, data)
    next_screen = data.get('Next_Screen')  # Using .get() to avoid KeyError
    if next_screen:
        if next_screen == 'End':
            print(f'Application creation has stopped on {sheet_name} screen')
        else:
            PageNavigator.navigate_screens(next_screen)
    else:
        print(f'Warning: "Next_Screen" column is missing in {sheet_name} sheet')

