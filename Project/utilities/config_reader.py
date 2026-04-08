import configparser
import os

class ConfigReader:
    """
    Class Name    : ConfigReader
    Author        : Sasi Kumar
    Description   : Utility class responsible for reading values from the config.properties file
    Return Type   : Object
    Parameters    : None
    """

    def __init__(self):
        # Initialize ConfigParser object to read configuration files
        try:
            self.config_parser = configparser.ConfigParser()

            # Get the absolute path of the current file
            current_file_path = os.path.abspath(__file__)

            # Resolve the project root directory dynamically
            project_root_directory = os.path.dirname(
                os.path.dirname(current_file_path)
            )

            # Construct full path of config.properties file
            config_file_path = os.path.join(
                project_root_directory,
                "config",
                "config.properties"
            )

            # Validate whether config file exists
            if not os.path.exists(config_file_path):
                raise FileNotFoundError(
                    f"Config file not found at: {config_file_path}"
                )

            # Read configuration values from the file
            self.config_parser.read(config_file_path)

        except Exception as exception:
            # Raise a meaningful exception if config loading fails
            raise Exception(
                f"Failed to load config file: {exception}"
            )

    """
    Method Name   : get_config_value
    Author        : Sasi Kumar
    Description   : Fetches a value from config.properties using section name and key
    Return Type   : str
    Parameters    : section_name(str), key_name(str)
    """

    def get_config_value(self, section_name, key_name):
        try:
            # Retrieve value from the given section and key
            return self.config_parser.get(section_name, key_name)

        except configparser.NoSectionError:
            # Raised when section does not exist
            raise Exception(
                f"Section '{section_name}' not found in config.properties"
            )

        except configparser.NoOptionError:
            # Raised when key does not exist inside the section
            raise Exception(
                f"Key '{key_name}' not found in section '{section_name}'"
            )

        except Exception as exception:
            # Catch any unexpected exception
            raise Exception(
                f"Error reading config value: {exception}"
            )