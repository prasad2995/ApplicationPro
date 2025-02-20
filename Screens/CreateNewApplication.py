from selenium.webdriver.common.by import By
import pandas as pd
import os
from time import sleep
import WebElements
import GlobalVariables
import IntializeDriver
import Screens.PrimaryInsured as PrimaryInsured
import Screens.PageNavigator as PageNavigator

driver = IntializeDriver.driver

#xpaths
next_button_xpath = "//span[text()='Choose Client']/..//parent::div//child::div//button[text()='Next']"
first_name_xpath = "//span[text()='First Name']/..//..//child::input"
new_client_xpath = "//lf-radiobutton[@value='newClient']//child::span/.."
signed_state_next_button_xpath = "//span[text()='Select Signed State']/..//parent::div//child::div//button[text()='Next']"

#fuctions
def create_application(driver, data):
    try:
        WebElements.click_button(driver, 'Create Application')
        WebElements.wait_until_ele_load(driver, new_client_xpath)
        sleep(2)
        driver.find_element(By.XPATH, new_client_xpath).click()
        sleep(2)
        driver.find_element(By.XPATH, next_button_xpath).click()
        WebElements.wait_until_ele_load(driver, first_name_xpath)
        WebElements.enter_text(driver, 'First Name', data['First_Name'])
        WebElements.enter_text(driver, 'Last Name', data['Last_Name'])
        WebElements.enter_text(driver, 'Birth Date', data['Birth_Date'])
        WebElements.select_value(driver, 'Gender', data['Gender'])
        driver.find_element(By.XPATH, next_button_xpath).click()
        sleep(2)
        driver.find_element(By.XPATH, signed_state_next_button_xpath).click()
        sleep(2)
        WebElements.select_value(driver, 'Product Type', data['Product_Type'])
        WebElements.select_value(driver, 'Product', data['Product'])
        sleep(2)
        # WebElements.click_button(By.XPATH, 'Create Application ')
        driver.find_element(By.XPATH, "//button[text()='Create Application ']").click()
        sleep(5)
    except Exception as e:
        print(f'Error: Failed at Create Application screen - {e}')

def read_excel_data(sheet_name):
    try:
        # Load the Excel sheet
        df = pd.read_excel(GlobalVariables.excel_path, sheet_name)

        # Convert each row to a dictionary and store in a list
        applications = df.to_dict(orient='records')

        # Example: Accessing the first application's details
        for app in applications:
            print(f"Processing Application: {app}")
        return app
    except Exception as e:
        print(f'Error: Unable to read the data from excel - {e}')


def Execute():
    sheet_name = os.path.splitext(os.path.basename(__file__))[0]
    data = read_excel_data(sheet_name)
    create_application(driver, data)
    PageNavigator.navigate_screens(data['NextScreen'])

