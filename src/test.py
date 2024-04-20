import json

# Replace 'json_file_path' with the actual path to your JSON file
json_file_path = 'split_meta.json'

# Load the JSON file content
with open(json_file_path, 'r') as file:
    content = json.load(file)

# Print out a small part of the content to understand its structure
print(content[:500])  # or print(content) if it's not too large
