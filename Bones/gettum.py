import requests
import json

def fetch_creator_items(creator_address, api_key, output_file):
    url = f"https://api.rarible.org/v0.1/items/byCreator?creator=ETHEREUM%3A{creator_address}&size=1500"

    headers = {
        "accept": "application/json",
        "X-API-KEY": api_key
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Parse the response to JSON and save it to a file
        with open(output_file, 'w') as f:
            json.dump(response.json(), f, indent=4)
        print(f"Data saved to {output_file}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}, Response: {response.text}")

# Example usage
creator_address = '0x49E5C693dC0cC586B6e29E2404B17dc0565Ac12B'
api_key = '41494f4b-11a8-4d29-a4a5-7307b34c1af9'
output_file = 'collections.json'

fetch_creator_items(creator_address, api_key, output_file)
