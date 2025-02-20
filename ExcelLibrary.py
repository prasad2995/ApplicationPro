from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
import WebElements
import GlobalVariables
import IntializeDriver
import os
import Screens.PageNavigator as PageNavigator

def read_excel_data(sheet_name):
    # Load the Excel sheet
    df = pd.read_excel(GlobalVariables.excel_path, sheet_name)

    # Convert each row to a dictionary and store in a list
    applications = df.to_dict(orient='records')

    # Example: Accessing the first application's details
    for app in applications:
        print(f"Processing Application: {app}")
    return app
