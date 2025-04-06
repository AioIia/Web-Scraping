#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TV Logo Downloader
=================
Un projet pour télécharger, traiter et organiser des logos de chaînes de télévision.

Usage:
    python main.py                  # Exécute le processus complet
    python main.py download         # Exécute uniquement le téléchargement
    python main.py process          # Exécute uniquement le traitement des images
    python main.py create_excel     # Crée uniquement le fichier Excel à partir du fichier texte
    python main.py help             # Affiche l'aide
"""

import os
import sys
import logging
from download import download_all_logos, ensure_directory_exists as download_ensure_dir
from process import process_images, create_excel

# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/main.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
CONFIG = {
    'input_dir': 'data',
    'input_file': 'data/channels.xlsx',
    'output_dir': 'data/logos',
    'error_log': 'logs/errors.txt',
    'image_min_size': 320,
    'image_scale_factor': 0.85,
}

def ensure_directory_exists(path):
    """Crée le répertoire s'il n'existe pas."""
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f"Répertoire créé: {path}")

def setup_directories():
    """S'assure que les répertoires nécessaires existent."""
    for directory in ['data/logos', 'logs']:
        ensure_directory_exists(directory)

def get_txt_file():
    """Trouve le premier fichier texte dans le répertoire data."""
    txt_files = [f for f in os.listdir(CONFIG['input_dir']) if f.endswith('.txt')]
    if not txt_files:
        logger.error("Veuillez placer un fichier texte avec les chaînes dans le répertoire 'data'.")
        sys.exit(1)
    return os.path.join(CONFIG['input_dir'], txt_files[0])

def create_excel_file():
    """Crée le fichier Excel à partir du fichier texte."""
    try:
        txt_file = get_txt_file()
        logger.info(f"=== Création du fichier Excel à partir de {txt_file} ===")
        create_excel(txt_file, CONFIG['input_file'])
        logger.info("Création terminée avec succès!")
        return True
    except Exception as e:
        logger.error(f"Erreur lors de la création du fichier Excel: {e}")
        return False

def download():
    """Télécharge les logos des chaînes."""
    if not os.path.exists(CONFIG['input_file']):
        logger.info("Fichier Excel non trouvé, création en cours...")
        if not create_excel_file():
            return False
    
    logger.info("\n=== Téléchargement des logos ===")
    download_ensure_dir(CONFIG['output_dir'])  # Utiliser la fonction de download.py
    download_all_logos(CONFIG['input_file'], CONFIG['output_dir'])
    logger.info("Téléchargement terminé avec succès!")
    return True

def process():
    """Traite les images téléchargées."""
    logger.info("\n=== Traitement des images ===")
    process_images(
        CONFIG['output_dir'], 
        CONFIG['image_min_size'], 
        CONFIG['image_scale_factor'],
    )
    logger.info("Traitement des images terminé avec succès!")
    return True

def show_help():
    """Affiche l'aide pour l'utilisation du script."""
    print("""
TV Logo Downloader - Aide
========================

Usage:
    python main.py                  # Exécute le processus complet
    python main.py download         # Exécute uniquement le téléchargement
    python main.py process          # Exécute uniquement le traitement des images
    python main.py create_excel     # Crée uniquement le fichier Excel à partir du fichier texte
    python main.py clear            # Supprime les fichiers temporaires
    python main.py help             # Affiche cette aide

Description:
    Ce script permet de télécharger et traiter des logos de chaînes de télévision.
    1. Place un fichier texte avec une chaîne par ligne dans le dossier 'data'
    2. Exécutez le script pour générer un fichier Excel avec les chaînes et leur pays
    3. Les logos seront téléchargés et traités automatiquement

Configuration actuelle:
    - Répertoire d'entrée: {input_dir}
    - Fichier Excel: {input_file}
    - Répertoire de sortie des logos: {output_dir}
    - Taille minimale des images: {image_min_size}px
    - Facteur d'échelle: {image_scale_factor}
    """.format(**CONFIG))

def clear():
    logger.info("Effacement des fichiers...")
    if os.path.exists(CONFIG['input_file']):
        os.remove(CONFIG['input_file'])
    elif os.path.exists('data/logos'):
        for file in os.listdir('data/logos'):
            os.remove('data/logos/'+file)
        os.rmdir('data/logos')
    logger.info("Fichiers effacés avec succès!")
    
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
        elif command == 'create_excel':
            create_excel_file()
        elif command == 'clear':
            clear()
        elif command in ['help', '-h', '--help']:
            show_help()
        else:
            logger.error(f"Commande inconnue: {command}")
            show_help()
    else:
        # Exécuter le processus complet
        success = True
        
        
        if success:
            success = create_excel_file()
        
        if success:
            success = download()
            
        if success:
            success = process()
            
        if success:
            logger.info("\nProcessus complet terminé avec succès!")
        else:
            logger.error("\nLe processus s'est terminé avec des erreurs. Consultez les logs pour plus de détails.")


if __name__ == '__main__':
    main()