from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import WebElements
import GlobalVariables
import IntializeDriver
import os
import Screens.PageNavigator as PageNavigator




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