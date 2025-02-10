import requests
from bs4 import BeautifulSoup
import os.path

def clean_url(base_url, href):
    # Remove trailing slash from base_url
    base_url = base_url.rstrip('/')
    # Remove leading slash from href
    href = href.lstrip('/')
    return f"{base_url}/{href}"

def get_zip_links(url, directory, file_handle):
    if not url.startswith('http'):
        return
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        #file_handle.write(f"mkdir {directory} 2>nul\n")
        file_handle.write(f"cd {directory}\n")
        
        for link in soup.find_all('a'):
            if link and 'href' in link.attrs:
                href = link['href']
                if href.endswith(('.wsc', '.tic', '.sg', '.zip','.mgw', '.gbc', '.lnx','.gba', '.rar', 
                                '.pdf', '.hex', '.rom', '.7z', '.stx', '.ogg', 'mp3', 'st', '.json', 
                                '.png', 'D64', 'T64', 'C64', '.col', '.cas')):
                    full_url = clean_url(url, href)
                    file_handle.write(f"wget --no-check-certificate {full_url}\n")
        
        file_handle.write("cd ..\n")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

def get_all():
    with open('download.bat', 'w') as f:
        f.write("@echo off\n")  # Make batch file less verbose
        for id in urls:
            get_zip_links(urls[id], dirs[id], f)

if __name__ == "__main__":
    get_all()