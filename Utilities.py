import pyautogui
import datetime
from time import sleep

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
screenshot_path = f"C:/Users/srinivasa.punnam/OneDrive - Sapiens/Desktop/Prasad Punnam/Testing/Temp/Screenshots/error_screenshot_{timestamp}.png"

def take_screenshot():
    # sleep(3)
    pyautogui.screenshot(screenshot_path)