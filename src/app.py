import json
import os
from dotenv import load_dotenv
from utils.process.data_processor import DataProcessor
import logging
import traceback

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Define a list of geographic levels to process
    geo_levels = ["Zip", "State", "US"]

    for geo_level in geo_levels:
        try:
            logger.info(f"Processing data for geographic level: {geo_level}")
            data_processor = DataProcessor(geo_level)
            data_processor.process()
        except Exception as e:
            logger.error(f"Error processing data for {geo_level}: {e}")
            traceback.print_exc()
