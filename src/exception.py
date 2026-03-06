import logging
import os
import sys
from datetime import datetime


# Create log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


def error_messages_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = (
        f"Error occurred in script: {file_name} "
        f"at line number: {line_number} "
        f"with error message: {str(error)}"
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_messages_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message