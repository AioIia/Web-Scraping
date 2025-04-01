#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TV Logo Downloader
=================
Un projet pour télécharger, traiter et organiser des logos de chaînes de télévision.

Usage:
    python main.py              # Exécute le processus complet
    python main.py download     # Exécute uniquement le téléchargement
    python main.py process      # Exécute uniquement le traitement des images
    python main.py normalize    # Prépare uniquement la liste normalisée
"""

import os
import sys
from download import download_all_logos, prepare_normalized_channel_list
from process import process_images

# Configuration
CONFIG = {
    'output_dir': 'data/logos',
    'channel_list_file': 'data/channels_names/channel_names_epg.best.txt',
    'excel_source': 'data/channels_names/20240318 list of tv channels.xlsx',
    'error_log': 'logs/errors.txt',
    'image_min_size': 320,
    'image_scale_factor': 0.85
}

def ensure_directory_exists(path):
    """Crée le répertoire s'il n'existe pas."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Répertoire créé: {path}")

def setup_directories():
    """S'assure que les répertoires nécessaires existent."""
    for directory in ['data/logos', 'data/channels_names', 'logs']:
        ensure_directory_exists(directory)

def normalize():
    """Prépare la liste normalisée des chaînes."""
    print("=== Préparation de la liste normalisée des chaînes ===")
    prepare_normalized_channel_list(
        CONFIG['excel_source'], 
        'data/channels_names/normalized_channels.xlsx'
    )
    print("Normalisation terminée avec succès!")

def download():
    """Télécharge les logos des chaînes."""
    print("\n=== Téléchargement des logos ===")
    download_all_logos(CONFIG['channel_list_file'], CONFIG['output_dir'])
    print("Téléchargement terminé avec succès!")

def process():
    """Traite les images téléchargées."""
    print("\n=== Traitement des images ===")
    process_images(
        CONFIG['output_dir'], 
        CONFIG['image_min_size'], 
        CONFIG['image_scale_factor']
    )
    print("Traitement des images terminé avec succès!")

def show_help():
    """Affiche l'aide pour l'utilisation du script."""
    print("""
Usage:
    python main.py              # Exécute le processus complet
    python main.py download     # Exécute uniquement le téléchargement
    python main.py process      # Exécute uniquement le traitement des images
    python main.py normalize    # Prépare uniquement la liste normalisée
    python main.py help         # Affiche cette aide
    """)

def main():
    """Fonction principale qui orchestre le workflow selon les arguments."""
    setup_directories()
    
    # Vérifier les arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'download':
            download()
        elif command == 'process':
            process()
        elif command == 'normalize':
            normalize()
        elif command in ['help', '-h', '--help']:
            show_help()
        else:
            print(f"Commande inconnue: {command}")
            show_help()
    else:
        # Exécuter le processus complet
        normalize()
        download()
        process()
        print("\nProcessus complet terminé avec succès!")


if __name__ == '__main__':
    main()