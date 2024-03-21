import os
from download import download_logo, write_to_file

def main(path_to_write, path_to_channel_names):

    with open(path_to_channel_names, 'r', encoding='latin-1') as file:
        channels = file.readlines()

    # Enlever les sauts de ligne
    channels = [channel.strip() for channel in channels]
    channels.sort()

    n = len(channels)
    i = 0
    # Télécharger les logos pour chaque chaîne
    for channel in channels:
        try:
            download_logo(channel, path_to_write)
            print(f"Logo téléchargé pour {channel}, {round((i/n)*100, 2)}%")

        except Exception as e:
            write_to_file("errors.txt", f"Erreur lors du téléchargement du logo pour {channel}: {e}")
        i += 1

if __name__ == '__main__':
    main("Logos/Logos_epg.best", "channels_names/channel_names_epg.best.txt");