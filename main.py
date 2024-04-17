import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from flickrscraper import FlickrScraper
import threading


class FlickrScraperApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Flickr Scraper")
        self.root.geometry("400x200")

        self.url_label = ttk.Label(self.root, text="URL de la page Flickr à scrapper", font=("Helvetica", 12))
        self.url_label.pack(pady=(10, 5))

        self.url_entry = ttk.Entry(self.root, width=50, font=("Helvetica", 10))
        self.url_entry.pack(pady=5)

        self.max_images_label = ttk.Label(self.root, text="Nombre limite d'image (facultatif)", font=("Helvetica", 12))
        self.max_images_label.pack(pady=(10, 5))

        self.max_images_entry = ttk.Entry(self.root, width=10, font=("Helvetica", 10))
        self.max_images_entry.pack(pady=5)

        self.scrape_button = ttk.Button(self.root, text="Scrapper", command=self.scrape_images)
        self.scrape_button.pack(pady=10)

        self.status_label = ttk.Label(self.root, text="")
        self.status_label.pack()

    def scrape_images(self):
        url = self.url_entry.get()
        max_images = self.max_images_entry.get()

        # Validate input values
        if not url:
            messagebox.showerror("Error", "Veuillez saisir une URL.")
            return
        if not url.startswith("https://www.flickr.com/"):
            messagebox.showerror("Error", "Veuillez saisir une URL Flickr valide.")
            return
        if not max_images:
            max_images = None
        elif int(max_images) < 1:
            messagebox.showerror("Error", "Le nombre d'images doit être supérieur à 0.")
            return
        else:
            max_images = int(max_images)

        # Perform scraping in a separate thread
        self.status_label.config(text="Traitement en cours...")
        threading.Thread(target=self.start_scraping, args=(url, max_images), daemon=True).start()

    def start_scraping(self, url, max_images):
        scraper = FlickrScraper(url, max_images)
        scraper.run()

        # Update status label
        self.status_label.config(text="Traitement terminé.")
        messagebox.showinfo("Success", "Images scrappées avec succès.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = FlickrScraperApp()
    app.run()