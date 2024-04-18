# Flickr Scraper

This is a Python application for scraping images from Flickr using Selenium and BeautifulSoup.

## 💻 Installation

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

4. Install tkinter for a specific system:

   - For Ubuntu or other distros with apt:
   ```bash
   sudo apt-get install python3-tk
   ```

   - For Fedora:
   ```bash
   sudo dnf install python3-tkinter
   ```

   - For Mac:
   ```bash
   brew install python-tk
   ```

   - For Windows:
   ```bash
   pip install tk
   ```

5. Install driver for Unix system (Windows users skip):

   - Navigate to a bin folder:
   ```bash
   cd /usr/bin
   ```

   - Get the latest driver download link [Here](https://github.com/mozilla/geckodriver/releases) and then download it like that:
   ```bash
   sudo wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz
   ```

   - Unzip the package:
   ```bash
   sudo tar -xvzf geckodriver*
   ```

   - Provide all privileges:
   ```bash
   sudo chmod +x geckodriver
   ```

6. Install driver for Windows:
   - Get the latest driver for your system [Here](https://github.com/mozilla/geckodriver/releases) and then download it.
   - Unzip it in a folder and add the path of the .exe folder to the system path.

## 🚀 Usage

To use the Flickr Scraper, follow these steps:

1. Run the `main.py` file:

```bash
python main.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
