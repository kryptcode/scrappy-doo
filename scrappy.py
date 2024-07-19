import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def download_image(url, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        image_name = os.path.join(folder_path, url.split("/")[-1])
        with open(image_name, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {image_name}")
    else:
        print(f"Failed to retrieve  {url}")

def scrape_images(url, folder_path="images"):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    for img in img_tags:
        img_url = img.get('src')
        img_url = urljoin(url, img_url)
        try:
            download_image(img_url, folder_path)
        except Exception as e:
            print(f"Could not download {img_url}: {e}")

if __name__ == "__main__":
    website_url = "https://example.vercel.app/" 
    scrape_images(website_url)
