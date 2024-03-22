
<h2 align="center">Test-web-scraping</h3>
<h3 align="center">AIMT-058-23-000050-C Generation de la base de donnée d'icones de chaines tv 3/18/2024</h3>


## Context

Pour l’application airmont player, il est nécéssaire de générer la liste des icones des chaine de TV mondiales.
Cette liste peut présenter plusieurs millier de fichiers, qui vont aussi évoluer dans le temps.
Nous souhaitons générer automatiquement un répertoire contenant les logo des chaines de TV.

## Requirements


La convention de nommage des fichier est celui de epg.best : <nom de la chaine sans espaces>.<code du pays à 2 lettres>.
La procédure est la suivante :

* Extraire la liste des nom de chaines au format epg.best dans un fichier texte (ou csv). Cf fichier `20240318 list of tv
channels.xlsx`
* Pour chacun des nom de chaine au format epg, lancer une recherche google image « nom de chaine au format
epg.best » « logo », télécharger la première image et l’enregistrer sous son nom epg.best, dans 1 répertoire unique.
Pour déterminer le nom epg.best
* Zipper le repertoire et l’uploader sur <a href = "cloud.airmont.com/tbd"> cloud.airmont.com/tbd</a>
* Formater les images sous forme de carré avec un liseré blanc puis les sauvegarder dans un autre répertoire, respectant les consignes suivantes:
  
  <li>
      coté du carré 100%
  </li>
  <li>
      largeur du liseré 7,50%
  </li>
  <li>
      longueur de l'icone d'origine 85,00%
  </li>
  <li>
       L’icone REQUIREMENTSdoit être centrée dans le carré sur la largeur.
  </li>
   <li>
      La résolution minimale doit être de 320p
   </li>
