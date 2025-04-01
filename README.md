# Web-Scraping

## Description
Ce projet permet d'extraire et de manipuler des données provenant de différentes sources en ligne. Il inclut des scripts pour télécharger des fichiers, traiter des images et extraire des données Excel. Ce projet est particulièrement utile pour automatiser la collecte et le traitement de données issues de plusieurs plateformes.

## Installation
### Prérequis
- Python 3.x
- pip

### Installation des dépendances
Exécutez la commande suivante pour installer les dépendances nécessaires :
```bash
pip install -r requirements.txt
```

## Structure du projet
Le projet est organisé de manière modulaire pour faciliter la maintenance et l'extensibilité.
```
Web-Scraping/
│── src/                     # Contient les scripts principaux
│   ├── main.py              # Script principal qui orchestre les différentes tâches
│   ├── download.py          # Téléchargement et gestion des fichiers
│   ├── edit_image.py        # Édition et manipulation d'images
│   ├── extract_xlsx.py      # Extraction et traitement des fichiers Excel
│   ├── generate_epg.py      # Génération d’un guide électronique des programmes (EPG)
│── data/                    # Contient les fichiers de données récupérées
│   ├── channels_names/      # Liste des chaînes et leurs métadonnées
│── logs/                    # Contient les fichiers de logs et d'erreurs
│   ├── errors.txt           # Enregistrement des erreurs rencontrées
│── config/                  # Fichiers de configuration du projet
│   ├── settings.json        # Paramètres ajustables pour le scraping et le traitement
│── README.md                # Documentation principale
│── requirements.txt         # Liste des dépendances du projet
│── .gitignore               # Fichiers et dossiers à exclure du contrôle de version
```

## Utilisation
### Exécuter le script principal
Pour lancer le projet, exécutez la commande suivante :
```bash
python src/main.py
```

### Personnalisation
Vous pouvez modifier les paramètres dans le fichier `config/settings.json` pour ajuster le comportement du scraping et du traitement des données. Voici quelques paramètres que vous pouvez configurer :
- **URLs des sources de données**
- **Format de sortie des fichiers extraits**
- **Options de filtrage et de nettoyage des données**

### Gestion des erreurs
Les erreurs et exceptions sont enregistrées dans `logs/errors.txt`. En cas de problème, consultez ce fichier pour diagnostiquer et corriger les erreurs éventuelles.

## Auteur
Aiolia

