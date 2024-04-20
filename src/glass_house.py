import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox, Label, Button, Toplevel
from PIL import Image, ImageTk
import json
import urllib.parse
import os
import logging

logging.basicConfig(filename='glass_house.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


# Configuration paths
json_path = 'trimmed_meta.json'
thumbnail_dir = './thumbnails'  # Directory where thumbnails are stored

def load_json_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

class GlassHouseApp(tk.Tk):
    def __init__(self, json_path, thumbnail_dir):
        super().__init__()
        self.json_path = json_path
        self.thumbnail_dir = thumbnail_dir
        self.data = load_json_data(self.json_path)
        self.title("Glass House Gallery")
        self.setup_ui()l

    def setup_ui(self):
        self.frame_collections = ttk.Frame(self)
        self.frame_collections.pack(side="left", fill="both", expand=True)

        self.listbox_collections = tk.Listbox(self.frame_collections)
        self.listbox_collections.pack(side="left", fill="both", expand=True)
        self.populate_collections_listbox()

        self.frame_thumbnails = ttk.Frame(self)
        self.frame_thumbnails.pack(side="right", fill="both", expand=True)

        self.listbox_collections.bind('<<ListboxSelect>>', self.display_thumbnails)

 
def populate_collections_listbox(self):
    if 'items' not in self.data:
        print("No 'items' key in JSON data.")
        return

    for item in self.data['items']:
        if 'meta' in item and 'name' in item['meta']:
            self.listbox_collections.insert(tk.END, item['meta']['name'])
        else:
            print("Missing 'meta' or 'name' key in some items.")


    def display_thumbnails(self, event):
        self.frame_thumbnails.destroy()
        self.frame_thumbnails = ttk.Frame(self)
        self.frame_thumbnails.pack(side="right", fill="both", expand=True)
        

        selected_collection = self.listbox_collections.get(self.listbox_collections.curselection())
        items = [item for item in self.data if item['itemCollection']['name'] == selected_collection]

        for item in items:
            thumbnail_path = os.path.join(self.thumbnail_dir, f"{item['id']}.png")
            if os.path.exists(thumbnail_path):
                img = Image.open(thumbnail_path)
                photo = ImageTk.PhotoImage(img)
                btn = ttk.Button(self.frame_thumbnails, image=photo, command=lambda item=item.copy(): self.show_item_detail(item))
                btn.image = photo
                btn.pack()
                

    def show_item_detail(self, item):
        details_window = Toplevel(self)
        details_window.title(item['meta']['name'])

        img = Image.open(os.path.join(self.thumbnail_dir, f"{item['id']}.png"))
        photo = ImageTk.PhotoImage(img)
        label_image = Label(details_window, image=photo)
        label_image.image = photo
        label_image.pack()

        label_name = Label(details_window, text=f"Name: {item['meta']['name']}")
        label_name.pack()

        label_desc = Label(details_window, text=f"Description: {item['meta']['description']}")
        label_desc.pack()

        url = f"https://dweb.link/ipfs/QmViHGre4k9XzvS76y25s3Bf5fKJWNaTj3ZHJRqMCSydzS?contract_address={item['contract']}&token_id={item['tokenId']}&image_url={urllib.parse.quote(item['meta']['content'][0]['url'])}"
        share_button = Button(details_window, text="View on Website", command=lambda url=url: self.open_url(url))
        share_button.pack()

import tkinter as tk
from tkinter import ttk, Label, Button, Toplevel
from PIL import Image, ImageTk
import json
import urllib.parse
import os
import logging

logging.basicConfig(filename='glass_house.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Configuration paths
json_path = 'trimmed_meta.json'
thumbnail_dir = './thumbnails'

def load_json_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

class GlassHouseApp(tk.Tk):
    def __init__(self, json_path, thumbnail_dir):
        super().__init__()
        self.json_path = json_path
        self.thumbnail_dir = thumbnail_dir
        self.data = load_json_data(self.json_path)
        self.title("Glass House Gallery")
        self.setup_ui()

    def setup_ui(self):
        self.frame_collections = ttk.Frame(self)
        self.frame_collections.pack(side="left", fill="both", expand=True)

        self.listbox_collections = tk.Listbox(self.frame_collections)
        self.listbox_collections.pack(side="left", fill="both", expand=True)
        self.populate_collections_listbox()

        self.frame_thumbnails = ttk.Frame(self)
        self.frame_thumbnails.pack(side="right", fill="both", expand=True)

        self.listbox_collections.bind('<<ListboxSelect>>', self.display_thumbnails)

    def populate_collections_listbox(self):
        if 'items' not in self.data:
            print("No 'items' key in JSON data.")
            return
        
        for item in self.data['items']:
            if 'meta' in item and 'name' in item['meta']:
                self.listbox_collections.insert(tk.END, item['meta']['name'])
            else:
                print("Missing 'meta' or 'name' key in some items.")

    def display_thumbnails(self, event):
        self.frame_thumbnails.destroy()
        self.frame_thumbnails = ttk.Frame(self)
        self.frame_thumbnails.pack(side="right", fill="both", expand=True)

        selected_collection = self.listbox_collections.get(self.listbox_collections.curselection())
        items = [item for item in self.data['items'] if item['itemCollection']['name'] == selected_collection]

        for item in items:
            thumbnail_path = os.path.join(self.thumbnail_dir, f"{item['id']}.png")
            if os.path.exists(thumbnail_path):
                img = Image.open(thumbnail_path)
                photo = ImageTk.PhotoImage(img)
                btn = ttk.Button(self.frame_thumbnails, image=photo, command=lambda item=item.copy(): self.show_item_detail(item))
                btn.image = photo
                btn.pack()

    def show_item_detail(self, item):
        details_window = Toplevel(self)
        details_window.title(item['meta']['name'])

        img = Image.open(os.path.join(self.thumbnail_dir, f"{item['id']}.png"))
        photo = ImageTk.PhotoImage(img)
        label_image = Label(details_window, image=photo)
        label_image.image = photo
        label_image.pack()

        label_name = Label(details_window, text=f"Name: {item['meta']['name']}")
        label_name.pack()

        label_desc = Label(details_window, text=f"Description: {item['meta']['description']}")
        label_desc.pack()

        url = f"https://dweb.link/ipfs/QmViHGre4k9XzvS76y25s3Bf5fKJWNaTj3ZHJRqMCSydzS?contract_address={item.get('contract', '')}&token_id={item.get('tokenId', '')}&image_url={urllib.parse.quote(item['meta']['content'][0]['url'])}"
        share_button = Button(details_window, text="View on Website", command=lambda url=url: self.open_url(url))
        share_button.pack()

    def open_url(self, url):
        import webbrowser
        webbrowser.open(url)

if __name__ == "__main__":
    app = GlassHouseApp(json_path, thumbnail_dir)
    app.mainloop()


if __name__ == "__main__":
    app = GlassHouseApp(json_path, thumbnail_dir)
    app.mainloop()
