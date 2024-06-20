import pandas as pd

def open_parquet_file(file_path):
    """Opens a Parquet file and returns a Pandas DataFrame.

    Args:
        file_path (str): The path to the Parquet file.

    Returns:
        pandas.DataFrame: The DataFrame containing the Parquet file's data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If an invalid file path is provided.
        pd.errors.ParserError: If there's an issue parsing the Parquet file.
    """

    try:
        df = pd.read_parquet(file_path)  # Read the Parquet file into a DataFrame
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except ValueError as e:
        raise ValueError(f"Invalid file path or format: {file_path}. Error: {e}")
    except pd.errors.ParserError as e:
        raise pd.errors.ParserError(f"Error parsing Parquet file: {file_path}. Error: {e}")

# Get the file path from the user
# file_path = input("Enter the path to your Parquet file: ")
file_path = '/Users/rmcrae/Downloads/State_data.parquet'

# Open and process the Parquet file
try:
    df = open_parquet_file(file_path)

    # Now you can work with the DataFrame (df)
    print("\nFirst 5 rows of the DataFrame:")
    print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

    print("\nColumns and their types:")
    print(df.info())

except Exception as e:
    print(f"An error occurred: {e}")
