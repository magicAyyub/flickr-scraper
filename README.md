# Flickr Scraper

This is a Python application for scraping images from Flickr using Selenium and BeautifulSoup.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/magicAyyub/flickr-scraper.git
```

2. Navigate to the project directory:

```bash
cd flickr-scraper
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

4. Install tkinter 

- For Ubuntu or other distros with apt :

```bash
sudo apt-get install python3-tk
```

- For Fedora:
```bash
sudo dnf install python3-tkinter
```

- For Mac :

```bash
brew install python-tk
```

- For Windows:

```bash
pip install tk
```

## Usage

To use the Flickr Scraper, follow these steps:

1. Run the `main.py` file:

```bash
python main.py
```

2. Enter the URL of the Flickr page you want to scrape images from.

3. Optionally, specify the maximum number of images to scrape. If not provided, it will default to 200.

4. Click the "Scrape" button to start the scraping process.

5. Wait for the process to finish. Once completed, the images will be saved in the `scraped_images` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.