import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def extract_sidebar_links(soup, base_url):
    sidebar_links = []

    # Adjust the selector to partially match the class attribute for the sidebar links
    sidebar_links_elements = soup.find_all("a", class_=lambda value: value and "svelte-b61eto" in value)

    for link in sidebar_links_elements:
        href = link.get("href")
        if href:
            full_url = urljoin(base_url, href)
            sidebar_links.append(full_url)

    return sidebar_links


def extract_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # Remove script and style elements
        for element in soup(["script", "style"]):
            element.decompose()
        
        # Extract text
        text = " ".join(t.strip() for t in soup.stripped_strings)
        return text, soup
    else:
        return f"Error fetching URL: {response.status_code}", None

def save_text_to_file(text, filename):
    with open(filename, "w") as file:
        file.write(text + "\n")

def get_filename_from_url(url):
    # Get the last part of the URL (after the last '/')
    name = url.split("/")[-1]
    # Remove any special characters and replace spaces with underscores
    name = re.sub(r'\W+', '_', name)
    # Add a .txt extension
    return f"{name}.txt"

def scrape_docs(url, base_url, visited=set()):
    if url in visited:
        return
    visited.add(url)

    text, soup = extract_text_from_url(url)
    
    if "Error fetching URL" not in text:
        filename = get_filename_from_url(url)
        save_text_to_file(text, filename)

        if soup:
            sidebar_links = extract_sidebar_links(soup, base_url)
            for link in sidebar_links:
                scrape_docs(link, base_url, visited)
    else:
        print(f"Skipping URL: {url} - {text}")


if __name__ == "__main__":
    #url = "https://modal.com/docs/guide"
    #url for Reference. Replace url with:
    url = "https://modal.com/docs/reference"
    scrape_docs(url, url)