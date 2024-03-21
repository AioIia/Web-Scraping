# Test-web-scraping
AIMT-058-23-000050-C Generation de la base de donnée d'icones de chaines tv 3/18/2024

CONTEXT

Pour l’application airmont player, il est nécéssaire de générer la liste des icones des chaine de TV mondiales.
Cette liste peut présenter plusieurs millier de fichiers, qui vont aussi évoluer dans le temps.
Nous souhaitons générer automatiquement un répertoire contenant les logo des chaines de TV.

REQUIREMENTS DESCRIPTION

La convention de nommage des fichier est celui de epg.best : <nom de la chaine sans espaces>.<code du pays à 2 lettres>.
La procédure est la suivante :
1-Extraire la liste des nom de chaines au format epg.best dans un fichier texte (ou csv). Cf fichier «20240318 list of tv
channels.xlsx »
2-Pour chacun des nom de chaine au format epg, lancer une recherche google image « nom de chaine au format
epg.best » « logo », télécharger la première image et l’enregistrer sous son nom epg.best, dans 1 répertoire unique.
Pour déterminer le nom epg .best
3-zipper le repertoire et l’uploader sur cloud.airmont.com/tbd
4-fomater les images sous forme de carré avec un liseré blanc puis les sauvegarder dans un autre répertoire, respectant les consignes suivantes:
coté du carré 100%
largeur du liseré 7,50%
longueur de l'icone d'origine 85,00%
L’icone doit être centrée dans le carré sur la largeur.
La résolution minimale doit être de 320p
