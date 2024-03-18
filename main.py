import requests
from bs4 import BeautifulSoup
import os
from download import download_logo, write_to_file

if not os.path.exists('Logos'):
    os.makedirs('Logos')

#ouvre le fichier contenant le nom des chaines
file_path = f"{os.getcwd()}/channel_names.txt"
with open(file_path, 'r', encoding='latin-1') as file:
    channels = file.readlines()

# Enlever les sauts de ligne
channels = [channel.strip() for channel in channels]
channels.sort()

def main():
    n = len(channels)
    i = 0
    logo_folder = f"{os.getcwd()}/Logos"
    # Télécharger les logos pour chaque chaîne
    for channel in channels:
        try:
            download_logo(channel, logo_folder)
            print(f"Logo téléchargé pour {channel}, {round((i/n)*100, 2)}%")

        except Exception as e:
            write_to_file("errors.txt", f"Erreur lors du téléchargement du logo pour {channel}: {e}")
        i += 1

if __name__ == '__main__':
    main();