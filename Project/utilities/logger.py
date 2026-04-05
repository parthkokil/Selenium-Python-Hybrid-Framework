import logging
from datetime import datetime
import os
from utilities.config_reader import ConfigReader

"""
    Generates Logs inside logs folder 
    Author:Gitika
"""

def get_logger():
    logger = logging.getLogger("framework_logger")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    try:
        config = ConfigReader()
        relative_log_path = config.get_data("PATH", "logger_path")

        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        log_dir = os.path.join(project_root, relative_log_path)
        os.makedirs(log_dir, exist_ok=True)

        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        log_file = os.path.join(log_dir, f"log_{time_stamp}.log")

        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        return logger

    except Exception as e:
        raise Exception(f"Failed to initialize logger: {e}")