from utils.process.data_processor import DataProcessor
import logging
import traceback

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    geo_levels = ["Zip", "State", "US"]
    for geo_level in geo_levels:
        try:
            logger.info(f"Processing data for geographic level: {geo_level}")
            data_processor = DataProcessor(geo_level)
            data_processor.process()
        except Exception as e:
            logger.error(f"Error processing data for {geo_level}: {e}")
            traceback.print_exc()
