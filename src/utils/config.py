import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'sample_data.csv')
DB_PATH = os.path.join(BASE_DIR, 'data', 'database.db')
