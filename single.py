import requests
from bs4 import BeautifulSoup

# Define URLs and directories
urls = {
    1: "http://archive.org/download/rr-3do/usa",
    2: "xyz"
}

dirs = {
    1: "3do",
    2: "64dd"
}


def get_zip_links(url, directory, file_handle):
    if not url.startswith('http'):
        return
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for link in soup.find_all('a'):
        if link and link['href'].endswith(('.wsc', '.tic', '.sg', '.zip','.mgw', '.gbc', '.lnx','.gba', '.rar', '.pdf', '.hex', '.rom', '.7z', '.stx', '.ogg', 'mp3', 'st', '.json', '.png', 'D64', 'T64', 'C64', '.col', '.cas')):
            full_url = f"{url}/{link['href']}"
            file_handle.write(f"cd {directory} && wget --no-check-certificate {full_url} && cd ..\n")



def get_all():
    with open('download.bat', 'w') as f:
        for id in urls:
            #f.write(f"mkdir {dirs[id]}\n")
            f.write(f"cd {dirs[id]}\n")            
            get_zip_links(urls[id], dirs[id], f)
            f.write(f"cd ..\n")

if __name__ == "__main__":
    get_all()