import os
from PIL import Image

def resize_image(input_path, output_path, max_width=200):
    """Resize an image to a maximum width while maintaining aspect ratio."""
    with Image.open(input_path) as img:
        original_width, original_height = img.size
        if original_width <= max_width:
            img.save(output_path)
            print(f"No resizing needed for {input_path}.")
            return

        scaling_factor = max_width / original_width
        new_height = int(original_height * scaling_factor)
        resized_img = img.resize((max_width, new_height), Image.ANTIALIAS)

        resized_img.save(output_path)
        print(f"Image saved to {output_path} with width {max_width}px and height {new_height}px.")

def process_directory(input_directory, output_directory):
    """Process each image in a directory and save resized images to another directory."""
    os.makedirs(output_directory, exist_ok=True)  # Ensure the output directory exists
    for filename in os.listdir(input_directory):
        file_path = os.path.join(input_directory, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'webp')):
            output_filename = f"thumbnail_{filename}"
            output_path = os.path.join(output_directory, output_filename)
            resize_image(file_path, output_path)

# Main execution
if __name__ == '__main__':
    downloaded_media_dir = './media'
    thumbnails_dir = './thumbnails'
    process_directory(downloaded_media_dir, thumbnails_dir)
