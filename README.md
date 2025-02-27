# Snake Game en Python

Ce projet est une implémentation classique du jeu Snake en utilisant Python et la bibliothèque `turtle`. Le jeu est simple, intuitif et facile à jouer. Le serpent grandit à mesure qu'il mange de la nourriture, et le jeu se termine si le serpent entre en collision avec les murs ou avec lui-même.

## Fichiers inclus

Le projet est composé des fichiers Python suivants :

1. **`scoreboard.py`** : Gère l'affichage du score et le message de fin de jeu.
2. **`food.py`** : Gère la création et le positionnement aléatoire de la nourriture.
3. **`snake.py`** : Gère la création, le mouvement et la gestion des segments du serpent.
4. **`main.py`** : Le fichier principal qui initialise le jeu, gère les interactions et la logique du jeu.

## Fonctionnalités

- **Mouvement du serpent** : Le serpent peut se déplacer dans quatre directions (haut, bas, gauche, droite) en utilisant les touches fléchées.
- **Nourriture aléatoire** : La nourriture apparaît à des positions aléatoires sur l'écran.
- **Croissance du serpent** : Le serpent grandit d'un segment chaque fois qu'il mange de la nourriture.
- **Gestion du score** : Le score augmente à chaque fois que le serpent mange de la nourriture.
- **Fin du jeu** : Le jeu se termine si le serpent entre en collision avec les murs ou avec lui-même.

## Installation

Pour exécuter ce projet, vous devez avoir Python installé sur votre machine. Suivez les étapes suivantes pour installer et exécuter le jeu :

1. **Clonez le dépôt** :
   ```bash
   git clone git@github.com:IbrahimaLY/snake_game.git
   cd snake-game
 2.  **Installez les dépendances** :
Ce projet utilise uniquement la bibliothèque turtle, qui est incluse par défaut avec Python. Aucune installation supplémentaire n'est nécessaire.

3. **Exécutez le jeu** :

bash
Copy
python main.py
**Comment jouer**
Utilisez les touches fléchées pour diriger le serpent.

Mangez la nourriture bleue pour faire grandir le serpent et augmenter votre score.

Évitez de heurter les murs ou votre propre queue, sinon le jeu se terminera.

**Structure du code**
scoreboard.py : Contient la classe Scoreboard qui gère l'affichage du score et le message de fin de jeu.

food.py : Contient la classe Food qui gère la création et le positionnement aléatoire de la nourriture.

snake.py : Contient la classe Snake qui gère la création, le mouvement et la gestion des segments du serpent.

main.py : Le fichier principal qui initialise le jeu, gère les interactions et la logique du jeu.

**Contributions**
Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet, n'hésitez pas à ouvrir une issue ou à soumettre une pull request. Voici quelques idées d'améliorations possibles :

Ajouter des niveaux de difficulté.

Ajouter des obstacles sur le terrain de jeu.

Améliorer l'interface utilisateur avec des graphismes plus avancés.

Ajouter un système de sauvegarde des meilleurs scores.
