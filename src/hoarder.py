import json
import os
import requests
import subprocess

media_dir = './downloaded_media'
thumbnail_dir = './thumbnails'
os.makedirs(os.path.abspath(media_dir), exist_ok=True)
os.makedirs(os.path.abspath(thumbnail_dir), exist_ok=True)

def download_and_save_image(url, save_path):
    """Function to download an image from a URL and save it."""
    try:
        if url.startswith('https://ipfs.raribleuserdata.com/ipfs/'):
            ipfs_hash = url.split('/')[-1]
            save_path_with_extension = os.path.abspath(save_path)
            subprocess.run(['ipfs', 'get', ipfs_hash, '-o', save_path_with_extension])
            print(f"IPFS file fetched and saved to {save_path}")
        else:
            response = requests.get(url)
            response.raise_for_status()
            with open(os.path.abspath(save_path), 'wb') as f:
                f.write(response.content)
            print(f"Image saved to {save_path}")
        return True
    except (requests.RequestException, subprocess.CalledProcessError) as e:
        print(f"Failed to download image: {e}")
        return False

def process_items(data):
    """Function to process each item in the provided JSON data."""
    for item in data:
        meta = item.get('meta', {})
        content = meta.get('content', [])
        
        for media in content:
            if media.get('available', False) and media.get('@type', '') == 'IMAGE' and media.get('representation', '') == 'PREVIEW':
                url = media.get('url', '')
                mime_type = media.get('mimeType', '').split('/')[-1].lower()
                filename = f"{item.get('id', '').replace(':', '_')}.{mime_type}"
                image_path = os.path.join(media_dir, filename)
                
                if download_and_save_image(url, image_path):
                    print("Original image downloaded successfully.")

if __name__ == '__main__':
    with open('collections.json', 'r') as file:
        data = json.load(file)
        process_items(data.get('items', []))
