
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
screenshot_path = f"error_screenshot_{timestamp}.png"
pyautogui.screenshot(screenshot_path)