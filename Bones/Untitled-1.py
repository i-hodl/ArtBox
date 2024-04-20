# %%
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json
import webbrowser
import os

class ArtBoxApp(tk.Tk):
    def __init__(self, json_path, thumbnail_dir):
        super().__init__()
        self.json_path = json_path
        self.thumbnail_dir = thumbnail_dir
        self.title("ArtBox Gallery")
        self.json_data = self.load_json_data()
        self.collections = self.get_collections()
        self.setup_ui()

    def load_json_data(self):
        with open(self.json_path, 'r') as file:
            return json.load(file)

    def get_collections(self):
        # Group items by 'itemCollection/name'
        collections = {}
        for item in self.json_data['items']:
            collection_name = item['itemCollection']['name']
            if collection_name not in collections:
                collections[collection_name] = []
            collections[collection_name].append(item)
        return collections

    def setup_ui(self):
        self.listbox_collections = tk.Listbox(self)
        self.listbox_collections.pack(side="left", fill="both", expand=True)
        self.listbox_collections.bind('<<ListboxSelect>>', self.on_collection_select)
        
        self.frame_thumbnails = tk.Frame(self)
        self.frame_thumbnails.pack(side="right", fill="both", expand=True)

        # Populate the listbox with collection names
        for collection_name in self.collections.keys():
            self.listbox_collections.insert(tk.END, collection_name)

    def on_collection_select(self, event):
        selection_index = self.listbox_collections.curselection()
        if selection_index:
            collection_name = self.listbox_collections.get(selection_index)
            self.display_thumbnails(collection_name)

    def display_thumbnails(self, collection_name):
        # Clear the frame first
        for widget in self.frame_thumbnails.winfo_children():
            widget.destroy()

        # Load and display thumbnails
        for item in self.collections[collection_name]:
            thumbnail_path = os.path.join(self.thumbnail_dir, f"{item['id']}.png")
            if os.path.isfile(thumbnail_path):
                img = Image.open(thumbnail_path)
                img.thumbnail((100, 100))  # Assuming thumbnails are 100x100
                photo = ImageTk.PhotoImage(img)
                button = ttk.Button(self.frame_thumbnails, image=photo, command=lambda item=item: self.show_details(item))
                button.image = photo
                button.pack()

    def show_details(self, item):
        detail_window = tk.Toplevel(self)
        detail_window.title(item['meta']['name'])
        
        img_path = os.path.join(self.thumbnail_dir, f"{item['id']}.png")
        if os.path.isfile(img_path):
            img = Image.open(img_path)
            img.thumbnail((300, 300))  # For larger display
            photo = ImageTk.PhotoImage(img)
            label_image = tk.Label(detail_window, image=photo)
            label_image.photo = photo  # Keep a reference
            label_image.pack()
        
        label_name = tk.Label(detail_window, text=f"Name: {item['meta']['name']}")
        label_name.pack()
        
        label_description = tk.Label(detail_window, text=f"Description: {item['meta']['description']}")
        label_description.pack()
        
        # External link (assume we want to open the 'externalUri')
        link_button = ttk.Button(detail_window, text="Open in browser", command=lambda: webbrowser.open(item['meta']['externalUri']))
        link_button.pack()

if __name__ == "__main__":
    app = ArtBoxApp('collections.json', './thumbnails')
    app.mainloop()

