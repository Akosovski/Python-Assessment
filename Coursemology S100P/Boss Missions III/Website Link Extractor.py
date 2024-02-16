import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_links(url, depth):
    if depth == 0:
        return []

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        links = []
        for anchor in soup.find_all('a', href=True):
            href = anchor['href']
            full_url = urljoin(url, href)
            links.append(full_url)

        unique_links = set(links)

        print(f"Links at depth {depth} for {url}:")
        for link in unique_links:
            print(link)

        for link in unique_links:
            if is_same_domain(url, link):
                get_links(link, depth - 1)
    except Exception as e:
        print(f"Error while processing {url}: {e}")

def is_same_domain(base_url, target_url):
    base_domain = urlparse(base_url).netloc
    target_domain = urlparse(target_url).netloc
    return base_domain == target_domain

link = input("Input Website URL: ")
depth = int(input("Input Depth (max 3): "))

if depth > 3:
    print("Depth cannot exceed 3. Max depth of 3 applied.")
    depth = 3

get_links(link, depth)