import json

def load_json_data(filepath):
    """ Load JSON data from a file. """
    with open(filepath, 'r') as file:
        return json.load(file)

def display_available_keys(data):
    """ Display available keys from the JSON data. """
    if isinstance(data, list):
        data = data[0]  # Assuming all items have a similar structure
    keys = data.keys()
    print("Available keys:", ', '.join(keys))
    return keys

def get_user_selection(keys):
    """ Get user's selection of keys to display. """
    selections = input("Enter the keys you want to extract, separated by commas (e.g., id,meta): ")
    selected_keys = selections.split(',')
    selected_keys = [key.strip() for key in selected_keys if key.strip() in keys]
    return selected_keys

def extract_and_display_data(data, selected_keys, save_path):
    """ Extract and display data based on selected keys and save to file. """
    output = []
    if not isinstance(data, list):
        data = [data]  # Make sure data is iterable
    
    for index, item in enumerate(data):
        item_data = {}
        print(f"\nItem {index + 1}:")
        for key in selected_keys:
            if key in item:
                print(f"  {key}: {item[key]}")
                item_data[key] = item[key]
            else:
                print(f"  {key}: Key not found in item.")
        output.append(item_data)
    
    # Save the output data to the specified file
    with open(save_path, 'w') as f:
        json.dump(output, f, indent=4)
    print(f"\nData saved to {save_path}")

def main():
    filepath = input("Enter the path to your JSON file: ")
    json_data = load_json_data(filepath)
    
    # Assuming data is under 'items' key, adjust if needed
    if 'items' in json_data:
        json_data = json_data['items']
    
    available_keys = display_available_keys(json_data)
    selected_keys = get_user_selection(available_keys)
    
    save_path = input("Enter the path to save the extracted data (e.g., output.json): ")
    extract_and_display_data(json_data, selected_keys, save_path)

if __name__ == "__main__":
    main()
