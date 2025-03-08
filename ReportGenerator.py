import logging
import os
import webbrowser
from datetime import datetime

# Define the local folder where logs should be saved
log_dir = r"C:\Users\srinivasa.punnam\OneDrive - Sapiens\Desktop\Prasad Punnam\Testing\Temp\Logs"

# Ensure the directory exists
os.makedirs(log_dir, exist_ok=True)

# Create a timestamp for unique filenames
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define log file path
log_file = os.path.join(log_dir, f"execution_log_{timestamp}.log")

# Configure logging to ensure all logs go to both the file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode="w", encoding="utf-8"),  # Log to file
        logging.StreamHandler()  # Log to console
    ]
)

# Flush logs immediately after writing
logging.getLogger().setLevel(logging.INFO)


def generate_html_report():
    """Generate an HTML report from the log file and open it in the browser."""
    try:
        # Ensure all logs are flushed to the file before reading
        logging.shutdown()

        # Read log file
        with open(log_file, "r", encoding="utf-8") as f:
            logs = f.readlines()

        # HTML report structure
        html_content = f"""
        <html>
        <head>
            <title>Execution Log Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h2 {{ color: #333366; }}
                .info {{ color: green; }}
                .warning {{ color: orange; }}
                .error {{ color: red; }}
                .log-container {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
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

        # Save HTML report
        html_file_path = os.path.join(log_dir, f"ExecutionReport_{timestamp}.html")
        with open(html_file_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        # Open the report automatically in the default web browser
        webbrowser.open(html_file_path)

    except Exception as e:
        logging.error(f"Error generating HTML report: {e}")

