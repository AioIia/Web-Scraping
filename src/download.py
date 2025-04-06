#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module de téléchargement pour le TV Logo Downloader
Ce module contient les fonctions de téléchargement et de gestion des noms de chaînes.
"""

import os
import time
import logging
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from tqdm import tqdm

# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/download.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Liste d'agents utilisateurs pour éviter les blocages
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
]

# Dictionnaire pour la conversion des caractères spéciaux
SPECIAL_CHAR_MAPPING = {
    "+": "Plus", "&": "And", "'": "", "_": "", 
    "(": "", "/": "", ")": "", "-": "", 
    ".": "", ";": "", " ": "", "*": "", 
    "!": "", "´": "", ":": "", "?": "",
    ",": "", "@": "", "=": "", "#": "",
    "$": "", "%": "", "^": "", "[": "",
    "]": "", "{": "", "}": "", "|": "",
    "\\": "", "<": "", ">": "", "\"": ""
}

# Utilitaires de fichiers
def ensure_directory_exists(path):
    """Crée le répertoire s'il n'existe pas."""
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f"Répertoire créé: {path}")

def write_to_txt_file(file_path, content):
    """Écrit du contenu dans un fichier texte."""
    directory = os.path.dirname(file_path)
    ensure_directory_exists(directory)
    
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content)
        file.write('\n')

# Traitement des noms de chaînes
def normalize_channel_name(channel_name):
    """
    Normalise un nom de chaîne en remplaçant les caractères spéciaux.
    
    Args:
        channel_name (str): Nom de chaîne original
    
    Returns:
        str: Nom de chaîne normalisé
    """
    normalized_name = ""
    
    for char in channel_name:
        if not (char.isalpha() or char.isnumeric()):
            normalized_name += SPECIAL_CHAR_MAPPING.get(char, "")
        else:
            normalized_name += char
    
    return normalized_name

# Téléchargement des logos
def download_logo(channel_name, epg_best, output_dir="data/logos"):
    """
    Télécharge le logo d'une chaîne de télévision depuis Google Images.
    
    Args:
        channel_name (str): Nom de la chaîne
        output_dir (str): Répertoire de sortie où sauvegarder l'image
    
    Returns:
        bool: True si le téléchargement a réussi, False sinon
    """
    # Prépare la requête de recherche Google
    if len(channel_name) > 2 and channel_name[-3] == '.':
        search_term = f"{channel_name[:-3]}+logo"
    else:
        search_term = f"{channel_name}+logo"
    
    search_term = search_term.replace(' ', '+')
    google_search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={search_term}"
    
    try:
        # Récupération de la page de résultats
        response = requests.get(google_search_url)
        response.raise_for_status()  # Vérifie si la requête a réussi
        
        # Analyse de la page HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.findAll('img')
        
        # Sélection de l'image
        current_image_url = None
        for image in images:
            if 'src' in image.attrs:
                # Préfère les images de Wikipedia pour leur qualité
                if 'wikipedia' in image['src']:
                    current_image_url = image['src']
                    break
        
        # Si aucune image Wikipedia n'a été trouvée, prend la première image (en ignorant le logo Google)
        if not current_image_url and len(images) > 1:
            current_image_url = images[1]['src']
        
        if not current_image_url:
            print(f"Aucune image trouvée pour {channel_name}")
            return False
        
        # Téléchargement de l'image
        image_response = requests.get(current_image_url)
        image_response.raise_for_status()
        
        # Enregistrement de l'image
        output_path = f'{output_dir}/{normalize_channel_name(channel_name)}.{epg_best}.png'
        with open(output_path, 'wb') as file:
            file.write(image_response.content)
        
        return True
    
    except requests.RequestException as e:
        print(f"Erreur lors de la requête pour {channel_name}: {e}")
        return False
    except Exception as e:
        print(f"Erreur inattendue pour {channel_name}: {e}")
        return False

def download_all_logos(excel_path, output_dir="data/logos"):
    """
    Télécharge les logos pour toutes les chaînes listées dans un fichier.
    
    Args:
        excel_path (str): Chemin vers le fichier contenant la liste des chaînes
        output_dir (str): Répertoire où sauvegarder les logos
    """
    ensure_directory_exists(output_dir)
    
    try:
        df = pd.read_excel(excel_path)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier Excel: {e}")
        return
    
    # Récupération des noms de chaînes (supposé en première colonne)
    channels = df.iloc[:, 0].dropna().astype(str).tolist()
    epg_best = df.iloc[:, 1].dropna().astype(str).tolist()
    total_channels = len(channels)
    
    # Barre de progression tqdm
    for index, channel in enumerate(tqdm(channels, desc="Téléchargement des logos", unit="logo")):
        try:
            success = download_logo(channel, epg_best[index])
            
            if not success:
                logger.warning(f"Échec du téléchargement pour {channel}")
                write_to_txt_file('logs/errors.txt', f"Échec du téléchargement pour {channel}")
        
        except Exception as e:
            write_to_txt_file('logs/errors.txt', f"Erreur lors du téléchargement du logo pour {channel}: {e}")
