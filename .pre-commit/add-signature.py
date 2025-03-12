import os
import datetime
import sys

# Signature à ajouter
# shellcheck disable=SC2283
SIGNATURE = """
# Auteur : Ibrahima Oumar LY
# Github name: IbrahimaLY
# Date de création : {date}
# Description : Ce fichier contient les fonctions pour le jeu Snake.
"""

# Récupérer les fichiers .py modifiés

# shellcheck disable=SC2283
# shellcheck disable=SC1036
files = os.popen('git diff --cached --name-only --diff-filter=ACM').read().splitlines()
files = [f for f in files if f.endswith('.py')]

# Ajouter la signature aux fichiers
for file in files:
    with open(file, 'r+') as f:
        content = f.read()
        if SIGNATURE not in content:
            print(f"Ajout de la signature à {file}")
            f.write(f"\n{SIGNATURE}\n")
            os.system(f"git add {file}")

# Auteur : Ibrahima Oumar LY
# Github name: IbrahimaLY
# Date de cr�ation : {date}
# Description : Ce fichier contient les fonctions pour le jeu Snake.

