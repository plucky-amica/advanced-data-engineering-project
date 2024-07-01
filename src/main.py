from src.extraction.extract import extract_data
from src.transformation.transform import transform_data
from src.loading.load import load_data
from src.utils.logger import get_logger
from src.utils.config import DATA_PATH, DB_PATH
import sqlite3

logger = get_logger(__name__)

if __name__ == "__main__":
    logger.info("Starting data pipeline")

    data = extract_data(DATA_PATH)
    transformed_data = transform_data(data)
    
    conn = sqlite3.connect(DB_PATH)
    load_data(transformed_data, conn)
    conn.close()

    logger.info("Data pipeline completed")
