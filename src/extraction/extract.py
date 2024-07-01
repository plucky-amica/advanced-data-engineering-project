import pandas as pd

def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
