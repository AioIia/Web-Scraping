# 🌐 TV Logo Downloader

## 🚀 Description
Ce projet permet de télécharger et traiter automatiquement des logos de chaînes de télévision à partir d'Internet. Il recherche les logos sur Google Images, les télécharge, puis les normalise pour obtenir une collection uniforme.

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
│   ├── xxxx.txt             # Fichier texte utiliser
│── logs/                    # Contient les fichiers de logs et d'erreurs
│   ├── download.log         # Enregistrement des logs rencontrées dans download.py
│   ├── errors.txt           # Enregistrement des erreurs rencontrées
│   ├── main.log             # Enregistrement des logs rencontrées dans main.py
│   ├── process.log          # Enregistrement des logs rencontrées dans process.py
│── README.md                # Documentation principale
│── requirements.txt         # Liste des dépendances du projet
│── .gitignore               # Fichiers et dossiers à exclure du contrôle de version
```

---

## ⚡ Utilisation

### 🛠 Préparation
1. Placez un fichier texte contenant les noms des chaînes (un par ligne) dans le dossier `data/`
2. Assurez-vous que les dossiers nécessaires existent (créés automatiquement au démarrage)

### ▶️ Exécuter le script principal

Usage :
```bash
python main.py                  # Exécute le processus complet
python main.py download         # Exécute uniquement le téléchargement (besoin du fichier Excel)
python main.py process          # Exécute uniquement le traitement des images
python main.py create_excel     # Crée uniquement le fichier Excel à partir du fichier texte
python main.py clear            # Supprime les fichiers temporaires
python main.py help             # Affiche l'aide détaillée
```

### 🔄 Processus de fonctionnement
1. **Création du fichier Excel** : Le script recherche le pays associé à chaque chaîne
2. **Téléchargement des logos** : Récupération des logos depuis Google Images
3. **Traitement des images** : Normalisation des logos (taille, fond, format)

### 🎛 Personnalisation
Les paramètres peuvent être ajustés dans la section `CONFIG` du script `main.py` :
- Taille minimale des images
- Facteur d'échelle
- Sauvegarde des images originales
- Répertoires d'entrée/sortie

### 🛑 Gestion des erreurs
Les erreurs et exceptions sont enregistrées dans `logs/errors.txt` et dans les fichiers de logs spécifiques. En cas de problème, consultez ces fichiers pour diagnostiquer et corriger les erreurs éventuelles.

---

## 📋 Fonctionnalités principales

- **Détection automatique du pays** : Identifie le pays d'origine de la chaîne
- **Téléchargement intelligent** : Utilise différents User-Agents pour éviter les blocages
- **Normalisation des images** : Crée des logos uniformes avec fond blanc
- **Gestion des erreurs** : Sauvegarde les erreurs et fait plusieurs tentatives en cas d'échec
- **Suivi du progrès** : Affichage de l'avancement des opérations

---

## 👤 Auteur
**Aiolia**

---
