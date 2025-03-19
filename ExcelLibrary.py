import logging

import pandas as pd
import GlobalVariables
from faker import Faker

fake = Faker()

def read_excel_data(sheet_name):
    # Load the Excel sheet
    df = pd.read_excel(GlobalVariables.excel_path, sheet_name)

    # Convert each row to a dictionary and store in a list
    applications = df.to_dict(orient='records')

    # Example: Accessing the first application's details
    for app in applications:
        for key, value in app.items():
            if isinstance(value, str):
                if value.lower() == "randomname":
                    app[key] = fake.first_name()
                elif value.lower() == "randomaddress":
                    app[key] = fake.street_address()
                elif value.lower() == "randompostalcode":
                    app[key] = fake.postalcode()
                elif value.lower() == "randomstate":
                    app[key] = fake.state()
                elif value.lower() == "randomcity":
                    app[key] = fake.city()
                elif value.lower() == "randomphoneno":
                    app[key] = fake.basic_phone_number()
                elif value.lower() == "randomemail":
                    app[key] = fake.email()
                elif value.lower() == "randomssn":
                    app[key] = fake.ssn()

        logging.info(f'{sheet_name} data: {app}')
    return app
