import json
import logging
import os

# Set up logging
logging.basicConfig(filename='pooper.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def load_json_data(filepath):
    """
    Load JSON data from a file.
    """
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                data = json.load(file)
            logging.info("Successfully loaded JSON data.")
            return data
        else:
            logging.error(f"File not found: {filepath}")
            return None
    except Exception as e:
        logging.error(f"Failed to load JSON data: {e}")
        return None

def save_json_data(data, filepath):
    """
    Save JSON data to a file.
    """
    try:
        with open(filepath, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info("Successfully saved JSON data.")
    except Exception as e:
        logging.error(f"Failed to save JSON data: {e}")

# Example usage
if __name__ == "__main__":
    path = './trimmed_meta.json'
    json_data = load_json_data(path)
    if json_data is not None:
        # Process your data here
        pass

        # Save data if modifications are made
        save_json_data(json_data, path)
