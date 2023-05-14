# Python Web Scraper

This is a simple Python web scraper that can be used to extract the text content from a given web page, and also recursively scrapes the sidebar links. This program uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for parsing HTML and [requests](https://docs.python-requests.org/en/latest/) for sending HTTP requests.

## Prerequisites

Make sure you have installed the following Python packages:

1. BeautifulSoup
2. requests

You can install these packages using pip:

```bash
pip install beautifulsoup4 requests
```

## Usage

To use this script, just replace the URL in the `__main__` function with the URL you want to scrape. The script will save the scraped content as text files in the same directory as the script.

```python
if __name__ == "__main__":
    # Replace this URL with your target URL
    url = "https://modal.com/docs/reference"
    scrape_docs(url, url)
```

Each file is named based on the last segment of the URL (after the last '/'). Special characters are removed from the filename and spaces are replaced with underscores. The text content of the page is saved in the file.

## Functions

Here is a brief overview of what each function in the script does:

- `extract_sidebar_links(soup, base_url)`: Extracts links from the sidebar of the webpage.
- `extract_text_from_url(url)`: Fetches a webpage and extracts the text content.
- `save_text_to_file(text, filename)`: Saves given text to a file with the given filename.
- `get_filename_from_url(url)`: Generates a filename based on the last part of the URL.
- `scrape_docs(url, base_url, visited=set())`: Recursively scrapes a webpage and its sidebar links.
