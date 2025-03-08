import logging
import traceback
from ReportGenerator import generate_html_report
from Screens import LoginPage
import sys

# Define global exception handling
def log_exception(exc_type, exc_value, exc_traceback):
    """Logs all unhandled exceptions to the log file."""
    if issubclass(exc_type, KeyboardInterrupt):
        return  # Allow Ctrl+C to exit without logging

    error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    logging.error(f"Unhandled Exception:\n{error_message}")

# Set the exception hook to log uncaught exceptions
sys.excepthook = log_exception

try:
    logging.info("Execution started...")
    LoginPage.Execute()  # Your main test execution
    logging.info("Execution completed successfully.")

except Exception as e:
    logging.error(f"Critical error during execution: {e}", exc_info=True)

finally:
    # Ensure logs are saved and report is generated
    generate_html_report()
    LoginPage.end_execution()
