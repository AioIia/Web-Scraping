# 🌐 Web-Scraping

## 🚀 Description
Ce projet permet d'extraire et de manipuler des données provenant de différentes sources en ligne. Il inclut des scripts pour télécharger des fichiers et traiter les données, facilitant ainsi l'automatisation de la collecte et du traitement des données issues de plusieurs plateformes.

---

## 📥 Installation

### 📌 Prérequis
- Python 3.x
- pip

### 🛠 Installation des dépendances
1. (Optionnel) Créez un environnement virtuel pour isoler les dépendances du projet :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Linux/macOS
   venv\Scripts\activate  # Sous Windows
   ```
2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

---

## 📂 Structure du projet
Le projet est organisé de manière modulaire pour faciliter la maintenance et l'extensibilité.

```
Web-Scraping/
│── src/                     # Contient les scripts principaux
│   ├── main.py              # Script principal qui orchestre les différentes tâches
│   ├── download.py          # Téléchargement et gestion des fichiers
│   ├── process.py           # Traitement et normalisation des données
│── data/                    # Contient les fichiers de données récupérées
│   ├── channels_names/      # Liste des chaînes et leurs métadonnées
│── logs/                    # Contient les fichiers de logs et d'erreurs
│   ├── errors.txt           # Enregistrement des erreurs rencontrées
│── README.md                # Documentation principale
│── requirements.txt         # Liste des dépendances du projet
│── .gitignore               # Fichiers et dossiers à exclure du contrôle de version
```

---

## ⚡ Utilisation

### ▶️ Exécuter le script principal

Usage :
```bash
python main.py              # Exécute le processus complet
python main.py download     # Exécute uniquement le téléchargement
python main.py process      # Exécute uniquement le traitement des images
python main.py normalize    # Prépare uniquement la liste normalisée
```

### 🎛 Personnalisation
Certains paramètres peuvent être ajustés directement dans les scripts si nécessaire. Assurez-vous que les fichiers de données sont bien placés dans le dossier `data/channels_names/`.

### 🛑 Gestion des erreurs
Les erreurs et exceptions sont enregistrées dans `logs/errors.txt`. En cas de problème, consultez ce fichier pour diagnostiquer et corriger les erreurs éventuelles.

---

## 👤 Auteur
**Aiolia** ✨

---
