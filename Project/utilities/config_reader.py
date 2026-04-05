import configparser
import os


class ConfigReader:
    """
    Utility class to read values from config.properties
    Author: Sasi Kumar
    """

    def __init__(self):
        try:
            self.config = configparser.ConfigParser()

            # Resolve project root dynamically
            project_root = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )

            config_path = os.path.join(
                project_root, "config", "config.properties"
            )

            if not os.path.exists(config_path):
                raise FileNotFoundError(
                    f"Config file not found at: {config_path}"
                )

            self.config.read(config_path)

        except Exception as e:
            raise Exception(f"Failed to load config file: {e}")

    def get_data(self, section, key):
        try:
            return self.config.get(section, key)
        except configparser.NoSectionError:
            raise Exception(
                f"Section '{section}' not found in config.properties"
            )
        except configparser.NoOptionError:
            raise Exception(
                f"Key '{key}' not found in section '{section}'"
            )
        except Exception as e:
            raise Exception(f"Error reading config value: {e}")
