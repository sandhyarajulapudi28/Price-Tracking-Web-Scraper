import requests
from bs4 import BeautifulSoup
import csv

# Read product URLs from urls.txt
with open("urls.txt", "r") as f:
    urls = [line.strip() for line in f.readlines() if line.strip()]

# Open CSV file to save results
with open("prices.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Product Name", "Price", "URL"])

    # Loop through each product URL
    for url in urls:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")

            # Flipkart specific scraping
            name = soup.find("span", {"class": "VU-ZEz"}).get_text(strip=True)
            price = soup.find("div", {"class": "Nx9bqj CxhGGd"}).get_text(strip=True)

            writer.writerow([name, price, url])
            print(f"✅ {name} - {price}")

        except Exception as e:
            print(f"❌ Failed to scrape {url}: {e}")
