import json
import logging
import urllib.request
from pathlib import Path
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class FlickrScraper:
    def __init__(self, scraper_url: str, max_images: int | None = None) -> None:
        self.scraper_url = scraper_url
        self.__set_limit(max_images)
        self.logger = logging.getLogger("FlickrScraper")
        self.logger.setLevel(logging.INFO)
        
        # Create a folder to save the images
        self.folder_path = Path("scraped_images")
        self.folder_path.mkdir(parents=True, exist_ok=True)
        
        # create subfolder for the current run a subfolder with the current timestamp
        self.folder_path = self.folder_path / str(int(time.time()))
        self.folder_path.mkdir(parents=True, exist_ok=True)

        # Create a formatter with timestamp
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Add a StreamHandler to output log messages to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Add a FileHandler to output log messages to a file
        LOG_FILE_PATH = f"{self.folder_path}/flickr_scraper{self.folder_path.stem}.log"
        file_handler = logging.FileHandler(LOG_FILE_PATH)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler) 
        
        # Call the method to download ChromeDriver if needed
        self.download_chromedriver()  

    def __set_limit(self, max_images):
        if max_images is None:
            self.max_images = 200   # Default to 200 images if max_images is not provided
            self.default_limited = True
        else:
            self.max_images = max_images  
            self.default_limited = False 
            
    def download_chromedriver(self):
        try:
            # Try to create a Chrome driver to check if ChromeDriver is already available
            webdriver.Chrome(ChromeDriverManager().install())
        except:
            # If creating Chrome driver fails, download ChromeDriver
            self.logger.info("ChromeDriver not found. Downloading ChromeDriver...")
            ChromeDriverManager().install()

    def scrape(self) -> list[str]:

        images = set()  # Use a set to store unique image URLs
        driver = webdriver.Chrome()
        driver.get(self.scraper_url)
        try:
            # Scroll down to load more images
            last_height = driver.execute_script("return document.body.scrollHeight")
            
            while len(images) < self.max_images:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)  # Adjust the sleep time as needed
                new_height = driver.execute_script("return document.body.scrollHeight")
                
                if new_height == last_height:
                    break
                last_height = new_height

                # Parse the HTML content after scrolling
                soup = BeautifulSoup(driver.page_source, "html.parser")
                # Extract image URLs using BeautifulSoup
                image_tags = soup.select(".photo-list-photo-container img")

                for img in image_tags:
                    src = img.get("src")
                    if src:
                        images.add(src)  # Add the image URL to the set

                if len(images) >= self.max_images:
                    break

            # Close the browser
            driver.quit()

        except Exception as e:
            self.logger.error(f"Error occurred during scraping: {e}")

        # track the images that were scraped
        TRACK_FILE_PATH = f"{self.folder_path}/track_{self.folder_path.stem}.json"
        with open(TRACK_FILE_PATH, "w") as f:
            if self.default_limited:
                json.dump(list(images), f)
            else:
                json.dump(
                    list(images)[: self.max_images], f
                )  # limited to max number of images

        
        if self.default_limited: # Return all images if max_images is not set
            return list(images)
        
        return list(images)[
            : self.max_images
        ]  # Convert set to list and return only max_images

    def download_images(self) -> None:
        
        # log the start of the download process
        self.logger.info("Starting to scrape images")
        images = self.scrape()
        self.logger.info(f"Found {len(images)} images to download")
        
        base_url = "https:" if "https:" in self.scraper_url else "http:"

        # log the folder path
        self.logger.info(f"Saving images to {self.folder_path}")
        
        for i, image in enumerate(images):
            try:
                # Construct the complete image URL by prepending the protocol
                image_url = base_url + image
                response = urllib.request.urlopen(image_url)
                image_data = response.read()
                file_type = Path(image_url).suffix
                if file_type:
                    self.save_image(i, image_data, file_type)
                else:
                    self.logger.error("Could not detect file type")
            except Exception as e:
                self.logger.error(
                    f"Failed to download image {image_url} with error {e}"
                )

    def save_image(self, index, image_data, file_type):
        file_name = f"{self.folder_path}/image_{index}{file_type}"
        with open(file_name, "wb") as f:
            f.write(image_data)

    def run(self) -> None:
        self.download_images()
        self.logger.info("Finished downloading images")