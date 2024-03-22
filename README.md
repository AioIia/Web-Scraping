
<h2 align="center">Test-web-scraping</h3>
<h3 align="center">AIMT-058-23-000050-C Generation de la base de donnée d'icones de chaines tv 3/18/2024</h3>

## Table of contents
* [Context](#Context)
* [Requirements](#Requirements)
* [Specifications](#Specifications)
  * [`main.py`](#`main.py`)
  * [`download.py`](#`download.py`)
  * [`edit_image.py`](#`edit_image.py`)
  * [`extract_xls_files.py`](#`extract_xls_files.py`)
*[Using](#Using)
### Context

Pour l’application airmont player, il est nécéssaire de générer la liste des icones des chaine de TV mondiales.
Cette liste peut présenter plusieurs millier de fichiers, qui vont aussi évoluer dans le temps.
Nous souhaitons générer automatiquement un répertoire contenant les logo des chaines de TV.

### Requirements


La convention de nommage des fichier est celui de epg.best : *nom de la chaine sans espace*.*code du pays à 2 lettres*.
La procédure est la suivante :

* Extraire la liste des nom de chaines au format epg.best dans un fichier texte (ou csv). Cf fichier `20240318 list of tv channels.xlsx`
* Pour chacun des nom de chaine au format epg, lancer une recherche google image « nom de chaine au format epg.best » « logo », télécharger la première image et l’enregistrer sous son nom epg.best, dans 1 répertoire unique.
Pour déterminer le nom epg.best
* Zipper le repertoire et l’uploader sur [cloud.airmont.com/tbd](https://cloud.airmont.com/tbd)
* Formater les images sous forme de carré avec un liseré blanc puis les sauvegarder dans un autre répertoire, respectant les consignes suivantes:
  * Coté du carré 100%
  * Largeur du liseré 7,50%
  * Longueur de l'icone d'origine 85,00%
  * L’icone doit être centrée dans le carré sur la largeur.
  * La résolution minimale doit être de 320p.

### Specifications
* #### main.py
  * `main(path_to_write, path_to_channel_names)`
    * path_to_write est le repertoir ou les chaines seront stockées, path_to_channel_names est le fichier texte où le nom de les chaines sont sstocke ouù une ligne correspond au nom d'une chaine.
* #### download.py
  * `download_logo(channel_name, path)`
    * channel_name est la liste des chaines, path est le repertoir ou les chaines seront stockées.
  * `write_to_file(file, content)`
    * file est le fichier txt ou le content sera ecrit suivi dun retour a la ligne.
* #### edit_image.py
  * `modify_image(path)`
    * path est le repertoire ou les images sont stocke puis applique a chacune d'elles les [Requirements](#Requirements)
* #### extract_xls_files.py
  * `extract_xls_files(path)`
    * path est le fichier .xls contenant la liste du nom des chaines sous le format epg.best.
    
### Using
Le projet utilise:
* openpyxl
* os
* bs4
* requests
* PIL
