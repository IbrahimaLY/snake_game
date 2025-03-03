
# Auteur : Ibrahima Oumar LY
# Date de création : 2025-03-03
# Description : Ce fichier contient les fonctions pour le jeu Snake.

import os
import datetime

# Signature à ajouter
SIGNATURE = """
# Auteur : Ibrahima Oumar LY
# Date de création : {date}
# Description : Ce fichier contient les fonctions pour le jeu Snake.
"""

# Répertoire contenant les fichiers Python
DIRECTORY = "../"


# Fonction pour ajouter la signature
def add_signature_to_file(file_path):
    with open(file_path, "r+", encoding="utf-8") as file:
        content = file.read()
        file.seek(0, 0)  # Déplacer le curseur au début du fichier
        file.write(SIGNATURE.format(date=datetime.datetime.now().strftime("%Y-%m-%d")) + "\n" + content)


# Parcourir tous les fichiers Python dans le répertoire
for root, _, files in os.walk(DIRECTORY):
    for file_name in files:
        if file_name.endswith(".py"):  # Vérifier si le fichier est un fichier Python
            file_path = os.path.join(root, file_name)
            print(f"Ajout de la signature à : {file_path}")
            add_signature_to_file(file_path)

print("Signature ajoutée à tous les fichiers Python.")
