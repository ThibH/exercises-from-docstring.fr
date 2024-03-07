"""
TRiEUR DE FICHIERS
-> Exercise from the course "Les bases de Python" on Docstring website (www.docstring.fr)
Date: 2024-03-06
Author: Simon Salvaing

Sort the files contained in the data folder according to the following associations. :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
others : Divers
"""

from pathlib import Path

# Folders paths
DATA = Path.cwd() / "data"
MUSIQUE = DATA / "Musique"
VIDEOS = DATA / "Vidéos"
IMAGES = DATA / "Images"
DOCUMENTS = DATA / "Documents"
AUTRES = DATA / "Autres"

STORAGE_FOLDERS = [MUSIQUE, VIDEOS, IMAGES, DOCUMENTS, AUTRES]
EXTENSIONS = {
    (".mp3", ".flac", ".wav"): MUSIQUE,
    (".avi", ".mp4", ".gif"): VIDEOS,
    (".bmp", ".jpg", ".png"): IMAGES,
    (".txt", ".pptx", ".csv", ".xls", ".odt", ".pages"): DOCUMENTS,
}

# Creation of an iterator on DATA folder content
fichiers = DATA.iterdir()

# Creation of the storage folders in DATA folder
for dossier in STORAGE_FOLDERS:
    dossier.mkdir(exist_ok=True)

# Moving into the appropriate folders file by file.
for fichier in fichiers:
    if fichier.is_file():
        for extensions, dossier in EXTENSIONS.items():
            if fichier.suffix in extensions:
                fichier.rename(dossier / fichier.name)
                break
        else:
            fichier.rename(AUTRES / fichier.name)
