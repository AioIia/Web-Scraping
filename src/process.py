#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module de traitement pour le TV Logo Downloader
Ce module contient les fonctions de traitement des images.
"""

import os
from PIL import Image

def ensure_directory_exists(path):
    """Crée le répertoire s'il n'existe pas."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Répertoire créé: {path}")

def write_to_txt_file(file_path, content):
    """Écrit du contenu dans un fichier texte."""
    directory = os.path.dirname(file_path)
    ensure_directory_exists(directory)
    
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content)
        file.write('\n')

def process_images(directory, min_size=320, scale_factor=0.85):
    """
    Traite toutes les images dans un répertoire pour les uniformiser:
    - Redimensionne les petites images
    - Place les images sur un fond blanc carré
    
    Args:
        directory (str): Répertoire contenant les images
        min_size (int): Taille minimale des images
        scale_factor (float): Facteur d'échelle pour la taille des images
    """
    if not os.path.exists(directory):
        print(f"Le répertoire {directory} n'existe pas.")
        return
    
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    total_images = len(image_files)
    
    for index, image_filename in enumerate(image_files):
        progress = round(100 * index / total_images, 2)
        print(f"Traitement des images: {progress}% - {image_filename}")
        
        try:
            image_path = os.path.join(directory, image_filename)
            img = Image.open(image_path)
            
            # Déterminer la taille maximale
            size_taken = max(img.size)
            
            # Redimensionner si l'image est trop petite
            if size_taken < min_size:
                if size_taken == img.width:
                    new_width = int(min_size * scale_factor)
                    new_height = int(img.height * min_size / img.width * scale_factor)
                    img = img.resize((new_width, new_height))
                else:
                    new_width = int(img.width * min_size / img.height * scale_factor)
                    new_height = int(min_size * scale_factor)
                    img = img.resize((new_width, new_height))
                size_taken = min_size
            
            # Créer un canevas blanc carré
            canvas = Image.new('RGB', (size_taken, size_taken), (255, 255, 255))
            
            # Calcul de la position pour centrer l'image
            if max(img.size) == img.width:
                position = (int(img.width * 0.075), int(size_taken / 2 - img.height / 2))
            else:
                position = (int(size_taken / 2 - img.width / 2), int(img.height * 0.075))
            
            # Coller l'image sur le canevas et sauvegarder
            canvas.paste(img, position)
            canvas.save(image_path)
            
        except Exception as e:
            write_to_txt_file('logs/errors.txt', f"Erreur de traitement pour {image_filename}: {e}")
    
    print('Traitement des images terminé')