import requests
from bs4 import BeautifulSoup
import os.path

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
    31: "https://archive.org/download/GameboyClassicRomCollectionByGhostware",
    32: "https://archive.org/download/GameboyAdvanceRomCollectionByGhostware",
    33: "https://archive.org/download/GameBoyColor",
    34: "https://archive.org/download/GameWatchRomCollectionByGhostware",
    35: "https://archive.org/download/playtime_amstradGX4000",
    36: "https://archive.org/download/mattel-intellivision",
    37: "https://archive.org/download/atari-jaguar-no-intro_unzipped",
    38: "https://archive.org/download/lowresnx",
    39: "https://archive.org/download/lutro_202401",
    40: "https://archive.org/download/AtariLynxRomCollectionByGhostware",
    41: "macintosh",
    42: "https://archive.org/download/mame-0.260-roms-fullset-no-clones",
    43: "mame-advmame",
    44: "mame-libretro",
    45: "mame-mame4all",
    46: "https://archive.org/download/nointro.ms-mkiii",
    47: "megadrive",
    48: "https://archive.org/download/analogue-pocket-mega-duck-full-rom-set-2024-7-3",
    49: "moonlight",
    50: "msx",
    51: "msx1",
    52: "https://archive.org/download/microsoft-msx_msx2_romset",
    53: "msxturbor",
    54: "multivision",
    55: "https://archive.org/download/nintendo-64-romset-usa",
    56: "naomi",
    57: "naomigd",
    58: "https://archive.org/download/Neo-geoRomCollectionByGhostware",
    59: "neogeocd",
    60: "https://archive.org/download/nes-roms",
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
    75: "pico8",
    76: "https://archive.org/download/PokemonMiniRomCollectionByGhostware",
    77: "ports",
    78: "https://archive.org/download/def-jam-vendetta-u",
    79: "psx",
    80: "roms",
    81: "https://archive.org/download/Sam_Coupe_TOSEC_2012_04_23",
    82: "https://archive.org/download/nintendo-satellaview",
    83: "https://archive.org/download/ef_Sega_Saturn_Collection/Sega%20Saturn/",
    84: "https://archive.org/download/The_Complete_ScummVM_Collection_v2",
    85: "https://archive.org/download/Epoch_Super_Cassette_Vision_TOSEC_2012_04_23",
    86: "https://archive.org/download/nointro.32xx",
    87: "https://archive.org/download/rr-sega-mega-cd/bin/usa/",
    88: "https://archive.org/download/SegaSG-1000RomCollectionByGhostware",
    89: "https://archive.org/download/snes-romset-ultra-us",
    90: "https://archive.org/download/solarus-v1.6.2-src",
    91: "https://archive.org/download/Spectravideo_SVI-318_SVI-328_TOSEC_2012_04_23",
    92: "https://archive.org/download/NoIntroSufamiTurbo",
    93: "https://archive.org/download/necsupergrafxcomplete/ROMs/",
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
    108: "x1",
    109: "x68000",
    110: "zmachine",
    111: "zx81",
    112: "zxspectrum"
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


def clean_url(base_url, href):
    base_url = base_url.rstrip('/')
    href = href.lstrip('/')
    return f"{base_url}/{href}"

def get_zip_links(url, directory, file_handle):
    if not url.startswith('http'):
        return
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        file_handle.write(f"if not exist \"{directory}\" mkdir \"{directory}\"\n")
        file_handle.write(f"pushd \"{directory}\"\n")
        
        for link in soup.find_all('a'):
            if link and 'href' in link.attrs:
                href = link['href']
                if href.endswith(('.wsc', '.tic', '.sg', '.zip','.mgw', '.gbc', '.lnx','.gba', '.rar', 
                                '.pdf', '.hex', '.rom', '.7z', '.stx', '.ogg', 'mp3', 'st', '.json', 
                                '.png', 'D64', 'T64', 'C64', '.col', '.cas')):
                    full_url = clean_url(url, href)
                    file_handle.write(f"wget --no-check-certificate \"{full_url}\"\n")
        
        file_handle.write("popd\n")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

def get_all():
    with open('download.cmd', 'w', encoding='utf-8') as f:
        f.write("@echo off\n")
        f.write("setlocal enabledelayedexpansion\n")
        for id in urls:
            get_zip_links(urls[id], dirs[id], f)

if __name__ == "__main__":
    get_all()