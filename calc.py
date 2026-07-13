import numpy as np

class FinancialData:
    """Handles the ingestion and parsing of user input data."""
    def __init__(self):
        raw_input = input("Enter financial metrics separated by commas (e.g., 100, 250, 400): ")
        # Split by comma, strip whitespace, and convert to float safely
        self.clean_data = [float(x.strip()) for x in raw_input.split(",") if x.strip()]


class StatisticsCalculator:
    """A high-performance calculator for analyzing numerical datasets using NumPy."""
    def __init__(self, data_list):
        # We accept the raw list and store it internally as a highly optimized NumPy array
        self.data = np.array(data_list)

    def display_all_stats(self):
        """Executes and prints a full dashboard overview of the data."""
        print("\n || --- FINTRAA STATISTICAL ANALYSIS REPORT --- || ")
        print(f"Target Data Stream: {self.data}\n" + "-"*45)
        
        # We call our internal methods directly
        self.get_maximum()
        self.get_minimum()
        self.get_range()
        self.get_sum()
        self.get_average()
        self.get_median()
        self.get_variance()
        self.get_standard_deviation()
        self.get_percentile(75) # Checks upper quartile by default

    def get_maximum(self):
        print(f'Maximum Value      : ({np.max(self.data)})')

    def get_minimum(self):
        print(f'Minimum Value      : ({np.min(self.data)})')

    def get_range(self):
        stat_range = np.max(self.data) - np.min(self.data)
        print(f'Statistical Range  : ({stat_range})')

    def get_sum(self):
        print(f'Sum Total          : ({np.sum(self.data)})')

    def get_average(self):
        print(f'Arithmetic Average : ({np.average(self.data)})')

    def get_median(self):
        print(f'Median (50th %)    : ({np.median(self.data)})')

    def get_variance(self):
        print(f'Data Variance      : ({np.var(self.data):.4f})')

    def get_standard_deviation(self):
        print(f'Standard Deviation : ({np.std(self.data):.4f})')

    def get_percentile(self, q=50):  
        val = np.percentile(self.data, q)
        print(f'{q}th Percentile     : ({val})')


# ==========================================
# FUTURE EXPANSION SPACE
# ==========================================
class Arthmetic:
    """ Basic Airhtmetic logic : """ 
    pass

class TaxCalculator:
    """Placeholder: You can build your GST/Income Tax logic here later!"""
    pass

class InterestCalculator:
    """Placeholder: You can build Compound/Simple interest logic here later!"""
    pass


# --- RUNNING THE PIPELINE ---
if __name__ == "__main__":
    # 1. Fetch and clean the data
    session_data = FinancialData()
    
    # 2. Pass that data directly into the calculator instance
    fintraa_calc = StatisticsCalculator(session_data.clean_data)
    
    # 3. Fire up the dashboard!
    fintraa_calc.display_all_stats()