import requests
from bs4 import BeautifulSoup

# Define URLs and directories
urls = {
    1: "http://archive.org/download/mame251",
    2: "http://archive.org/download/sega-genesis-romset-ultra-usa"
}
dirs = {
    1: "Mame",
    2: "Genesis"
}

def get_zip_links(url, directory, file_handle):
    if not url.startswith('http'):
        return
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for row in soup.find_all('tr'):
        link = row.find('a')
        if link and link['href'].endswith(('.zip','.mgw', '.gbc', '.lnx','.gba', '.rar', '.pdf', '.hex', '.rom', '.7z', '.stx', '.ogg', 'mp3', 'st', '.json', '.png', 'D64', 'T64', 'C64', '.col', '.cas')):
            full_url = f"{url}/{link['href']}"
            file_handle.write(f"cd {directory} && wget {full_url} && cd ..\n")

def get_all():
    with open('download.bat', 'w') as f:
        for id in urls:
            f.write(f"mkdir {dirs[id]}\n")
            get_zip_links(urls[id], dirs[id], f)

if __name__ == "__main__":
    get_all()