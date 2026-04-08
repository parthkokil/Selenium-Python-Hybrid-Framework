import configparser
import os


class ConfigReader:
    """
    Class Name    : ConfigReader
    Description   : Reads configuration values from config.properties file
    """

    def __init__(self):
        """
        Method Name   : __init__
        Author        : Sasi Kumar
        Description   : Initializes ConfigParser and loads config file
        Return Type   : None
        Parameters    : None
        """
        try:
            self.config = configparser.ConfigParser()

            config_path = os.path.join(
                os.getcwd(), "config", "config.properties"
            )

            if not os.path.exists(config_path):
                raise FileNotFoundError(
                    f"Config file not found at path: {config_path}"
                )

            self.config.read(config_path)

        except Exception as exception:
            print(f"Error loading config file: {exception}")

    def get_config_value(self, section, key):
        """
        Method Name   : get_config_value
        Author        : Sasi Kumar
        Description   : Fetches value from config file based on section and key
        Return Type   : String
        Parameters    : section, key
        """
        try:
            return self.config.get(section, key)

        except Exception as exception:
            raise Exception(
                f"Failed to get config value for [{section}] {key}: {exception}"
            )