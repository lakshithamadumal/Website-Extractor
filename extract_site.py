import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Target Website URL
url = "Target-Website-URL"

# Create folder for saving files
os.makedirs("website_assets", exist_ok=True)

# Function to download a file
def download_file(file_url, folder):
    parsed_url = urlparse(file_url)
    filename = os.path.basename(parsed_url.path)
    save_path = os.path.join(folder, filename)

    try:
        response = requests.get(file_url)
        response.raise_for_status()  # Check if request was successful
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {file_url}: {e}")

# Step 1: Get HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Save HTML
html_file = os.path.join("website_assets", "index.html")
with open(html_file, "w", encoding="utf-8") as file:
    file.write(soup.prettify())
print("HTML Saved!")

# Step 2: Find and download CSS files
css_folder = os.path.join("website_assets", "css")
os.makedirs(css_folder, exist_ok=True)

for css_link in soup.find_all("link", rel="stylesheet"):
    css_url = urljoin(url, css_link.get("href"))
    download_file(css_url, css_folder)

# Step 3: Find and download JavaScript files
js_folder = os.path.join("website_assets", "js")
os.makedirs(js_folder, exist_ok=True)

for script in soup.find_all("script", src=True):
    js_url = urljoin(url, script.get("src"))
    download_file(js_url, js_folder)

print("✅ Extraction Complete! HTML, CSS, and JS saved in 'website_assets' folder.")

igh jfdiohoi98hth