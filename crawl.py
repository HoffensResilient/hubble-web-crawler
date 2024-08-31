import os
import requests
from bs4 import BeautifulSoup
import csv
import sys
from urllib.parse import urljoin

def get_all_urls(base_url):
    try:
        response = requests.get(base_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')

    # Join relative URLs with the base URL
    urls_titles = [(urljoin(base_url, link.get('href')), link.get_text().strip()) for link in links if link.get('href')]

    return urls_titles

def crawl_website(website_url):
    urls_titles = get_all_urls(website_url)
    if urls_titles:
        data_folder = 'datas'
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        csv_filepath = os.path.join(data_folder, 'webpages.csv')
        try:
            with open(csv_filepath, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['URL', 'Title'])
                writer.writerows(urls_titles)

            print(f"Data saved to '{csv_filepath}' inside the 'datas' folder.")
            return csv_filepath
        except PermissionError:
            print(f"Permission denied: '{csv_filepath}'. Ensure the file is not open elsewhere and you have write permissions.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    else:
        print("No webpages found on the website.")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python crawl.py <website_url>")
        sys.exit(1)

    website_url = sys.argv[1]
    crawl_website(website_url)
