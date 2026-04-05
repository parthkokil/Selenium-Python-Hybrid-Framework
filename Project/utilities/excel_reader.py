import os
from openpyxl import load_workbook
from utilities.config_reader import ConfigReader


class ExcelReader:
    """
    Utility class to read data from Excel files using openpyxl.
    Author : Saptarshi
    """

    def __init__(self):
        try:
            config = ConfigReader()
            relative_path = config.get_data("PATH", "excel_path")

            if not relative_path:
                raise ValueError("Excel path not found in config file")

            project_root = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )

            excel_path = os.path.join(project_root, relative_path)

            if not os.path.exists(excel_path):
                raise FileNotFoundError(
                    f"Excel file not found at {excel_path}"
                )

            self.workbook = load_workbook(excel_path)

        except Exception as e:
            raise Exception(f"Failed to load Excel workbook: {e}")

    def get_data(self, sheet_name, row, col):
        try:
            if sheet_name not in self.workbook.sheetnames:
                raise ValueError(
                    f"Sheet '{sheet_name}' does not exist in Excel file"
                )

            sheet = self.workbook[sheet_name]
            return sheet.cell(row=row, column=col).value

        except Exception as e:
            raise Exception(
                f"Failed to read data from sheet '{sheet_name}', "
                f"row {row}, column {col}: {e}"
            )