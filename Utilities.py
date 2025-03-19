import pyautogui
import datetime
from time import sleep
import logging
import os
import webbrowser
from faker import Faker
import GlobalVariables
from Screens import PageNavigator

# Generate timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_path = f"C:/Users/srinivasa.punnam/OneDrive - Sapiens/Desktop/Prasad Punnam/Testing/Temp/Screenshots/"

# Set up logging
log_file = "execution_log.html"

def take_screenshot(screen, type):
    sleep(1)
    # Create a timestamped directory if it doesn't exist
    save_path = os.path.join(screenshot_path, f"{timestamp}_{GlobalVariables.First_Name}_{GlobalVariables.Last_Name}")
    os.makedirs(save_path, exist_ok=True)  # Ensure directory exists

    # Find the next available number for naming
    existing_files = [f for f in os.listdir(save_path) if f.endswith('.png')]
    count = len(existing_files) + 1  # Get next sequential number

    # Define screenshot file path
    file_path = os.path.join(save_path, f"{count}_{screen}_{type}.png")
    # Capture and save the screenshot
    pyautogui.screenshot(file_path)

def generate_html_report():
    with open(log_file, "r") as f:
        logs = f.readlines()

    html_content = """
    <html>
    <head>
        <title>Execution Log Report</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h2 { color: #333366; }
            .info { color: green; }
            .warning { color: orange; }
            .error { color: red; }
            .log-container { background: #f4f4f4; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h2>Execution Log Report</h2>
        <div class="log-container">
    """

    for log in logs:
        if "INFO" in log:
            html_content += f'<p class="info">{log}</p>'
        elif "WARNING" in log:
            html_content += f'<p class="warning">{log}</p>'
        elif "ERROR" in log:
            html_content += f'<p class="error">{log}</p>'
        else:
            html_content += f'<p>{log}</p>'

    html_content += """
        </div>
    </body>
    </html>
    """

    with open("execution_log.html", "w") as f:
        f.write(html_content)

    # Open the log file in the browser after execution
    webbrowser.open("execution_log.html")

def next_screen(next_screen, sheet_name):
    if next_screen:
        if next_screen == 'End':
            print(f'Application creation has stopped at {sheet_name} screen')
        else:
            PageNavigator.navigate_screens(next_screen)
    else:
        logging.warning(f'Warning: "Next_Screen" column is missing in {sheet_name} sheet')

def randomName(name_type):
    fake = Faker()

    if name_type == 'firstname':
        result = fake.first_name()
    if name_type == 'lastname':
        result = fake.last_name()
    if name_type == 'address':
        result = fake.address()
    if name_type == 'address':
        result = fake.postcode()

    logging.info(f'The {name_type} is {result}')
    return result