import logging
from datetime import datetime
import os
from utilities.config_reader import ConfigReader


"""
Method Name   : get_framework_logger
Author        : Gitika
Description   : Creates and returns a configured framework-level logger instance which writes logs to a timestamped log file
Return Type   : logging.Logger
Parameters    : None
"""

def get_framework_logger():
    # Create or retrieve the framework logger instance
    framework_logger = logging.getLogger("framework_logger")

    # Prevent duplicate handlers if logger is already configured
    if framework_logger.handlers:
        return framework_logger

    # Set logging level to INFO
    framework_logger.setLevel(logging.INFO)

    try:
        # Initialize ConfigReader to fetch logger path
        config_reader = ConfigReader()

        # Read relative logger directory path from config.properties
        logger_directory_relative_path = config_reader.get_config_value(
            "PATH",
            "logger_path"
        )

        # Resolve project root directory dynamically
        project_root_directory = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        # Construct absolute path for logger directory
        logger_directory_path = os.path.join(
            project_root_directory,
            logger_directory_relative_path
        )

        # Create logger directory if it does not exist
        os.makedirs(logger_directory_path, exist_ok=True)

        # Generate timestamp for log file naming
        log_file_timestamp = datetime.now().strftime(
            "%Y_%m_%d_%H_%M_%S"
        )

        # Construct full log file path
        log_file_path = os.path.join(logger_directory_path,f"log_{log_file_timestamp}.log")

        # Create file handler for logging into file
        file_handler = logging.FileHandler(log_file_path)

        # Define log message format
        log_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        # Apply formatter to file handler
        file_handler.setFormatter(log_formatter)

        # Attach handler to the framework logger
        framework_logger.addHandler(file_handler)

        return framework_logger

    except Exception as exception:
        # Raise meaningful exception if logger initialization fails
        raise Exception(
            f"Failed to initialize framework logger: {exception}"
        )