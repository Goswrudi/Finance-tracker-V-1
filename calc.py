import numpy as np

class FinancialData:
    """Handles the ingestion and parsing of user input data."""
    def __init__(self):
        raw_input = input("Enter financial metrics separated by commas (e.g., 100, 250, 400): ")
        # Split by comma, strip whitespace, and convert to float safely
        self.clean_data = [float(x.strip()) for x in raw_input.split(",") if x.strip()]
