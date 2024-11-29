import os
import boto3
import datetime
import pandas as pd
import json
from io import BytesIO
import logging
from dotenv import load_dotenv
from urllib.request import urlopen

load_dotenv()

class DataProcessor:
    def __init__(self, geo_level):
        self.geo_level = geo_level
        self.session = boto3.Session()
        self.s3_client = self.session.client('s3')
        self.bucket_name = os.getenv("BUCKET_NAME")
        self.api_key = os.getenv("CENSUS_API_KEY")
        self.year = os.getenv('YEAR')
        self.logger = logging.getLogger(__name__)
        self.base_url = "https://api.census.gov/data/"

    def get_variables_for_geo(self):
        """Fetches variables relevant to the given geographical level from the appropriate CSV file."""

        # Determine the correct CSV file based on geo_level
        if self.geo_level == "Zip":
            filename = "acs5_variables_zip.csv"
        elif self.geo_level in ["US", "State"]:
            filename = "acs1_variables_us_state.csv"
        else:
            raise ValueError("Unsupported geographical level")

        # Construct the full file path        
        file_path = filename

        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Extract unique values from the 'Variable' column
        variables = df['Variable'].unique().tolist()

        return variables 

    def fetch_and_process_data(self, variables_chunk):
        """Fetches data from the Census API and processes it."""

        variables_str = ",".join(variables_chunk) + ",NAME"

        # Determine the correct endpoint and geo identifier based on your geo_level logic
        if self.geo_level == "State":
            base_url = f"{self.base_url}{self.year}/acs/acs1/profile"
            geo_suffix = "state"
        elif self.geo_level == "US":
            base_url = f"{self.base_url}{self.year}/acs/acs1/profile"
            geo_suffix = "us"
        elif self.geo_level == "Zip":
            base_url = f"{self.base_url}{self.year}/acs/acs5"
            geo_suffix = "zip%20code%20tabulation%20area"
        else:
            raise ValueError("Unsupported geographical level")

        url = f"{base_url}?get={variables_str}&for={geo_suffix}:*&key={self.api_key}"
        
        try:
            with urlopen(url) as response:
                data = json.loads(response.read().decode())
        except Exception as e:
            self.logger.error(f"API request failed for {url}: {e}")
            return None
        
        return pd.DataFrame(data[1:], columns=data[0])

    def process(self):
        """Orchestrates data fetching, processing, and saving to S3."""
        all_variables = self.get_variables_for_geo()

        # Process data in chunks as needed
        chunk_size = 100
        for i in range(0, len(all_variables), chunk_size):
            variables_chunk = all_variables[i : i + chunk_size]
            df = self.fetch_and_process_data(variables_chunk)
            if df is not None:
                self.save_to_s3(df)

    def save_to_s3(self, df):
        """Saves the processed DataFrame to S3."""

        # Save to s3
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        s3_path = f"CENSUS_YEAR={self.year}/{self.geo_level}/{timestamp}/{self.geo_level}_data.json"
        json_data = df.to_json(orient="records")
        self.s3_client.put_object(Bucket=self.bucket_name, Key=s3_path, Body=json_data)
        self.logger.info(f"Saved {len(df)} rows to S3: {s3_path}")