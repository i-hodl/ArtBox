import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json
import webbrowser
import os
import logging

# Set up logging
logging.basicConfig(filename='artbox.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

class ArtBoxApp(tk.Tk):
    def __init__(self, json_path, thumbnail_dir):
        super().__init__()
        self.json_path = json_path
        self.thumbnail_dir = thumbnail_dir
        self.title("ArtBox Gallery")
        self.json_data = self._load_json_data()  # Renamed the method with an underscore
        self.collections = self._get_collections()  # Renamed the method with an underscore
        self._setup_ui()  # Renamed the method with an underscore

    def _load_json_data(self):  # Renamed the method with an underscore
        try:
            with open(self.json_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            logging.error(f"Failed to load JSON data: {e}")
            return {}  # Return an empty dictionary as a fallback

    def _get_collections(self):  # Renamed the method with an underscore
        collections = {}
        try:
            for item in self.json_data['items']:
                collection_name = item['itemCollection']['name']
                if collection_name not in collections:
                    collections[collection_name] = []
                collections[collection_name].append(item)
            return collections
        except Exception as e:
            logging.error(f"Error getting collections: {e}")
            return {}

    def _setup_ui(self):  # Renamed the method with an underscore
        self.listbox_collections = tk.Listbox(self)
        self.listbox_collections.pack(side="left", fill="both", expand=True)
        self.listbox_collections.bind('<<ListboxSelect>>', self.on_collection_select)

        self.frame_thumbnails = tk.Frame(self)
        self.frame_thumbnails.pack(side="right", fill="both", expand=True)

        if self.collections is not None:
            for collection_name in self.collections.keys():
                self.listbox_collections.insert(tk.END, collection_name)

    def on_collection_select(self, event):
        logging.info("Collection selected.")
        selection_index = self.listbox_collections.curselection()
        if selection_index:
            collection_name = self.listbox_collections.get(selection_index)
            self.display_thumbnails(collection_name)

    def display_thumbnails(self, collection_name):
        logging.info(f"Displaying thumbnails for collection: {collection_name}")
        for widget in self.frame_thumbnails.winfo_children():
            widget.destroy()
        for item in self.collections.get(collection_name, []):
            thumbnail_path = os.path.join(self.thumbnail_dir, f"{item['id']}.png")
            if os.path.isfile(thumbnail_path):
                img = Image.open(thumbnail_path)
                img.thumbnail((100, 100))
                photo = ImageTk.PhotoImage(img)
                button = ttk.Button(self.frame_thumbnails, image=photo, command=lambda item=item: self.show_details(item))
                button.image = photo
                button.pack()

    def show_details(self, item):
        logging.info(f"Showing details for item: {item['tokenId']['name']}")
        detail_window = tk.Toplevel(self)
        detail_window.title(item['meta']['name'])

        img_path = os.path.join(self.thumbnail_dir, f"{item['id']}.png")
        if os.path.isfile(img_path):
            img = Image.open(img_path)
            img.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(img)
            label_image = tk.Label(detail_window, image=photo)
            label_image.photo = photo
            label_image.pack()

        label_name = tk.Label(detail_window, text=f"Name: {item['meta']['name']}")
        label_name.pack()

        label_description = tk.Label(detail_window, text=f"Description: {item['meta']['description']}")
        label_description.pack()

        link_button = ttk.Button(detail_window, text="Open in browser", command=lambda: webbrowser.open(item['meta']['externalUri']))
        link_button.pack()

if __name__ == "__main__":
    app = ArtBoxApp('trimmed_meta.json', './thumbnails')
    app.mainloop()
