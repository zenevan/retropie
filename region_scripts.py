import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

urls = {
    1: "https://archive.org/download/panasonic_3do_interactive_multiplayer",
    2: "https://archive.org/download/N64DDROMS",
    3: "https://archive.org/download/commodore-amiga-romset-us",
    4: "https://archive.org/download/all-amiga-roms_202404",
    5: "https://archive.org/download/commodore_amiga_cd32",
    6: "https://archive.org/download/commodore_amiga_cdtv",
    7: "https://archive.org/download/amstrad-cpc_202203",
    8: "https://archive.org/download/apple-ii-games-nib",
    9: "https://archive.org/download/apple_collection_v1.02",
    10: "https://archive.org/download/Arduboy-Arquivista",
    11: "https://archive.org/download/nointro.atari-2600",
    12: "https://archive.org/download/nointro.atari-5200",
    13: "https://archive.org/download/nointro.atari-7800",
    14: "https://archive.org/download/Atari800RomCollectionByGhostware",
    15: "https://archive.org/download/AtariSTRomsetByGhostware2018",
    16: "https://archive.org/download/atomiswave_202307",
    17: "https://archive.org/download/AcornBBCMicroRomCollectionByGhostware",
    18: "https://archive.org/download/Elektronika_BK-0010-0011M_TOSEC_2012_04_23",
    19: "https://archive.org/download/C64RomCollectionByGhostware",
    20: "https://archive.org/download/philips_cd-i",
    21: "https://archive.org/download/FairchildChannelF",
    22: "https://archive.org/download/colecovision-roms-usa",
    23: "https://archive.org/download/space-ace",
    24: "https://archive.org/download/trivialcrosswords1986fowlerh.",
    25: "dragon",
    26: "https://archive.org/download/DreamcastCollectionByGhostwareMulti-region",
    27: "https://archive.org/download/EasyRPG_Games",
    28: "https://archive.org/download/fbnarcade-fullnonmerged/arcade/",
    29: "https://archive.org/download/gamelist.backup_202012",
    30: "https://archive.org/download/sega-game-gear-romset-ultra-us",
    31: "https://archive.org/download/Cyles_Gameboy_roms",
    32: "https://archive.org/download/GameboyAdvanceRomCollectionByGhostware",
    33: "https://archive.org/download/GameBoyColor",
    34: "https://archive.org/download/GameWatchRomCollectionByGhostware",
    35: "https://archive.org/download/Amstrad_GX4000_TOSEC_2012_04_23",
    36: "https://archive.org/download/mattel-intellivision",
    37: "https://archive.org/download/atari-jaguar-no-intro_unzipped",
    38: "https://archive.org/download/lowresnx",
    39: "https://archive.org/download/lutro_202401",
    40: "https://archive.org/download/AtariLynxRomCollectionByGhostware",
    41: "https://archive.org/download/Macintosh_ROMs_Collection_1990s",
    42: "https://archive.org/download/mame-0.260-roms-fullset-no-clones",
    43: "mame-advmame",
    44: "mame-libretro",
    45: "mame-mame4all",
    46: "https://archive.org/download/nointro.ms-mkiii",
    47: "https://archive.org/download/sega-genesis-romset-ultra-usa",
    48: "https://archive.org/download/analogue-pocket-mega-duck-full-rom-set-2024-7-3",
    49: "https://archive.org/download/moonlight-p7lkbm",
    50: "msx",
    51: "msx1",
    52: "https://archive.org/download/microsoft-msx_msx2_romset",
    53: "msxturbor",
    54: "https://archive.org/download/multivision_202110",
    55: "https://archive.org/download/nintendo-64-romset-usa",
    56: "https://archive.org/download/sega-naomi/world/",
    57: "naomigd",
    58: "https://archive.org/download/Neo-geoRomCollectionByGhostware",
    59: "neogeocd",
    60: "https://archive.org/download/nintendo-entertainment-system-all-nes-roms-goodnes",
    61: "ngp",
    62: "https://archive.org/download/cylums-neo-geo-pocket-color-rom-collection",
    63: "https://archive.org/download/Magnavox_Odyssey_2_TOSEC_2012_04_23",
    64: "https://archive.org/download/OpenBOR-Packs",
    65: "https://archive.org/download/Tangerine_Oric_1_and_Atmos_TOSEC_2012_04_23",
    66: "https://archive.org/download/palmkiwadump",
    67: "pc",
    68: "pc88",
    69: "pc98",
    70: "pcengine",
    71: "pcenginecd",
    72: "pcfx",
    73: "pcv2",
    74: "https://archive.org/download/sega-pico_202008",
    75: "https://archive.org/download/pico-8-all-versions-collection",
    76: "https://archive.org/download/PokemonMiniRomCollectionByGhostware",
    77: "ports",
    78: "https://archive.org/download/def-jam-vendetta-u",
    79: "https://archive.org/download/psx-roms-archive",
    80: "roms",
    81: "https://archive.org/download/Sam_Coupe_TOSEC_2012_04_23",
    82: "https://archive.org/download/nintendo-satellaview",
    83: "https://archive.org/download/ef_Sega_Saturn_Collection/Sega%20Saturn/",
    84: "https://archive.org/download/The_Complete_ScummVM_Collection_v2",
    85: "https://archive.org/download/Epoch_Super_Cassette_Vision_TOSEC_2012_04_23",
    86: "https://archive.org/download/Sega-32x-Romset-us",
    87: "https://archive.org/download/rr-sega-mega-cd/bin/usa/",
    88: "https://archive.org/download/SegaSG1000",
    89: "https://archive.org/download/snes-usa-romset-complete-collection.-7z",
    90: "https://archive.org/download/solarus-v1.6.2-src",
    91: "https://archive.org/download/Spectravideo_SVI-318_SVI-328_TOSEC_2012_04_23",
    92: "https://archive.org/download/NintendoSufamiTurbo",
    93: "https://archive.org/download/NECSuperGrafx",
    94: "https://archive.org/download/Watara-SupervisionNo-Intro/Watara%20-%20Supervision%20%5BNo-Intro%5D/",
    95: "https://archive.org/download/unrenamed-files-thomson/UnRenamed%20Files%20-%20Thomson/",
    96: "https://archive.org/download/Texas_Instruments_TI-99_4a_TOSEC_2012_04_23",
    97: "https://archive.org/download/tic80games_202303",
    98: "https://archive.org/download/Tandy_TRS80_Color_Computer_TOSEC_2012_04_23",
    99: "https://archive.org/download/uzebox-collection",
    100: "https://archive.org/download/VectrexROMS",
    101: "https://archive.org/download/Philips_VG-5000_TOSEC_2012_04_23",
    102: "https://archive.org/download/commodore-vic-20",
    103: "https://archive.org/download/Philips_Videopac_Plus_TOSEC_2012_04_23",
    104: "https://archive.org/download/vbromcollectionmm1000",
    105: "https://archive.org/download/wasm4_202211",
    106: "https://archive.org/download/WonderswanColorRomCollectionByGhostware",
    107: "wswanc",
    108: "https://archive.org/download/Sharp_X1_TOSEC_2012_04_23",
    109: "https://archive.org/download/Sharp_X68000_Collection",
    110: "https://archive.org/download/Infocom_Z-Machine_TOSEC_2012_04_23",
    111: "https://archive.org/download/Sinclair_ZX81_TOSEC_2012_04_23",
    112: "https://archive.org/download/zx-spectrum-tosec-set-v-2020-02-18-lady-eklipse"
}

dirs = {
    1: "3do",
    2: "64dd",
    3: "amiga1200",
    4: "amiga600",
    5: "amigacd32",
    6: "amigacdtv",
    7: "amstradcpc",
    8: "apple2",
    9: "apple2gs",
    10: "arduboy",
    11: "atari2600",
    12: "atari5200",
    13: "atari7800",
    14: "atari800",
    15: "atarist",
    16: "atomiswave",
    17: "bbcmicro",
    18: "bk",
    19: "c64",
    20: "cdi",
    21: "channelf",
    22: "colecovision",
    23: "daphne",
    24: "dos",
    25: "dragon",
    26: "dreamcast",
    27: "easyrpg",
    28: "fbneo",
    29: "fds",
    30: "gamegear",
    31: "gb",
    32: "gba",
    33: "gbc",
    34: "gw",
    35: "gx4000",
    36: "intellivision",
    37: "jaguar",
    38: "lowresnx",
    39: "lutro",
    40: "lynx",
    41: "macintosh",
    42: "mame",
    43: "mame-advmame",
    44: "mame-libretro",
    45: "mame-mame4all",
    46: "mastersystem",
    47: "megadrive",
    48: "megaduck",
    49: "moonlight",
    50: "msx",
    51: "msx1",
    52: "msx2",
    53: "msxturbor",
    54: "multivision",
    55: "n64",
    56: "naomi",
    57: "naomigd",
    58: "neogeo",
    59: "neogeocd",
    60: "nes",
    61: "ngp",
    62: "ngpc",
    63: "o2em",
    64: "openbor",
    65: "oricatmos",
    66: "palm",
    67: "pc",
    68: "pc88",
    69: "pc98",
    70: "pcengine",
    71: "pcenginecd",
    72: "pcfx",
    73: "pcv2",
    74: "pico",
    75: "pico8",
    76: "pokemini",
    77: "ports",
    78: "psp",
    79: "psx",
    80: "roms",
    81: "samcoupe",
    82: "satellaview",
    83: "saturn",
    84: "scummvm",
    85: "scv",
    86: "sega32x",
    87: "segacd",
    88: "sg1000",
    89: "snes",
    90: "solarus",
    91: "spectravideo",
    92: "sufami",
    93: "supergrafx",
    94: "supervision",
    95: "thomson",
    96: "ti994a",
    97: "tic80",
    98: "trs80coco",
    99: "uzebox",
    100: "vectrex",
    101: "vg5000",
    102: "vic20",
    103: "videopacplus",
    104: "virtualboy",
    105: "wasm4",
    106: "wswan",
    107: "wswanc",
    108: "x1",
    109: "x68000",
    110: "zmachine",
    111: "zx81",
    112: "zxspectrum"
}

def check_region(filename):
    filename = filename.upper()
    has_usa = "USA" in filename
    has_europe = "EUROPE" in filename or "EUR" in filename
    has_japan = "JAPAN" in filename or "JPN" in filename
    
    if has_usa:  # If it has USA, we want it
        return True
    elif not has_usa and (has_europe or has_japan):  # If no USA but other regions, skip
        return False
    return True  # If no region specified, include it

def check_size(size_text):
    try:
        size = float(size_text.split()[0])
        unit = size_text.split()[1].upper()
        if unit == 'GB' and size > 1:  # More than 1GB
            ttotal += size*1000
            return True
        if unit == 'MB' and size > 800:  # More than 800MB
            ttotal += size
            return True
    except:
        return False
    return False

def normalize_filename(filename):
    filename = urllib.parse.unquote(filename)
    filename = filename.replace('%20', ' ')
    filename = filename.replace('%28', '(')
    filename = filename.replace('%29', ')')
    filename = filename.replace('0(', '(')
    filename = filename.replace('0)', ')')
    filename = filename.replace('0-', '-')
    filename = filename.replace('0.', '.')
    filename = ' '.join(filename.split())
    return filename

def create_download_script(url, directory):
    if not url.startswith('http'):
        return
        
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    script_content = """import requests
import os
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def download_file(url, filename):
    if os.path.exists(filename):
        print(f"Skipping {filename} - already exists")
        return
    try:
        response = requests.get(url, verify=False, stream=True)
        response.raise_for_status()
        print(f"Downloading: {filename}")
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

"""
    
    auto_downloads = []
    large_downloads = []
    
    try:
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for row in soup.find_all('tr'):
            link = row.find('a')
            if link and 'href' in link.attrs:
                href = link['href']
                if href.endswith(('.wsc', '.tic', '.sg', '.zip','.mgw', '.gbc', '.lnx','.gba', '.rar', 
                                '.pdf', '.hex', '.rom', '.7z', '.stx', '.ogg', 'mp3', 'st', '.json', 
                                '.png', 'D64', 'T64', 'C64', '.col', '.cas','.afpk','.mp3','.flac')):
                    filename = normalize_filename(href)
                    full_url = f"{url}/{href}"
                    
                    # Get file size if available
                    size_cell = row.find_all('td')[-1].text.strip() if len(row.find_all('td')) > 2 else "0 KB"
                    
                    if check_region(filename):
                        if check_size(size_cell):
                            large_downloads.append((full_url, filename))
                        else:
                            auto_downloads.append((full_url, filename))
    
        # Add automatic downloads
        script_content += "\ndef download_normal_files():\n"
        for url, filename in auto_downloads:
            script_content += f'    download_file("{url}", "{filename}")\n'
        
        if len(large_downloads):
            # Add large downloads with choice
            script_content += "\ndef download_large_files():\n"
            for i, (url, filename) in enumerate(large_downloads, 1):
                script_content += f'    print("{i}. {filename}")\n'
        
        if len(large_downloads):
            script_content += "    choices = input('Enter numbers of files to download (comma-separated) or press Enter to skip: ')\n"
            script_content += "    if choices.strip():\n"
            script_content += "        for choice in choices.split(','):\n"
            script_content += "            try:\n"
            script_content += "                idx = int(choice.strip()) - 1\n"
            script_content += f"                if 0 <= idx < {len(large_downloads)}:\n"
            script_content += "                    url, filename = large_downloads[idx]\n"
            script_content += "                    download_file(url, filename)\n"
            script_content += "            except ValueError:\n"
            script_content += "                continue\n"
        
        # Add the large_downloads list to the script
        if len(large_downloads):
            script_content += "\nlarge_downloads = [\n"
            for url, filename in large_downloads:
                script_content += f'    ("{url}", "{filename}"),\n'
            
            script_content += "]\n"
    
        # Add main execution
        script_content += "\nif __name__ == '__main__':\n"
        script_content += "    print('Downloading normal sized files...')\n"
        script_content += "    download_normal_files()\n"
        if len(large_downloads):
            script_content += "    print('\\nLarge files available:')\n"
            script_content += "    download_large_files()\n"
        
        # Write the script
        script_path = os.path.join(directory, 'download_files.py')
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        print(f"Created download script in {directory}")
        print(f"Normal files to download: {len(auto_downloads)}")
        print(f"Large files available: {len(large_downloads)}")
        
    except Exception as e:
        print(f"Error creating script for {url}: {e}")

def create_all_scripts():
    for id in urls:
        print(f"\nProcessing {dirs[id]} from {urls[id]}")
        create_download_script(urls[id], dirs[id])

if __name__ == "__main__":
    create_all_scripts()