# Blackjack

Ce projet est une implémentation du célèbre jeu Blackjack, réalisé dans le cadre d'un projet demandé par l'école. 

## Règles du jeu

Le but est de marquer le plus de points possible sans dépasser 21. Chaque carte a une valeur :`enter code here`

- de 2 à 10 : ces cartes ont pour valeur leur valeur nominale
- une figure vaut 10 points
- un As vaut 1 ou 11 points au choix

Le jeu commence avec les joueurs qui reçoivent chacun 2 cartes. Ensuite, le joueur peut choisir de "prendre" (recevoir) une ou plusieurs cartes supplémentaires pour tenter d'améliorer sa main, ou de "passer" et laisser le tour au croupier. Le croupier prend des cartes jusqu'à ce qu'il ait au moins 17 points, puis s'arrête. Si la main du joueur dépasse 21, il perd immédiatement. Si le total de la main du joueur est supérieur à celui du croupier, le joueur gagne. Sinon, c'est le croupier qui gagne.

## Classes

Le projet utilise deux classes : `Carte` et `Jeu`.

### Carte

La classe `Carte` représente une carte de jeu. Elle possède deux attributs :

- `valeur` : la valeur de la carte
- `couleur` : la couleur de la carte

### Jeu

La classe `Jeu` gère l'ensemble du jeu. Elle contient les méthodes nécessaires pour jouer une partie.

#### Initialisation

La méthode `__init__()` initialise un nouveau jeu de cartes en créant une liste de 52 cartes. Les cartes sont stockées dans l'attribut `paquet`.

#### Distribution des cartes

La méthode `distribuer_cartes()` distribue deux cartes à chaque joueur.

#### Affichage de la main du joueur

La méthode `afficher_main_joueur()` affiche la main du joueur.

#### Affichage de la première carte du croupier

La méthode `afficher_premiere_carte_croupier()` affiche la première carte du croupier.

#### Demande d'une carte supplémentaire

La méthode `demander_carte()` demande au joueur s'il souhaite prendre une carte supplémentaire. Si oui, lui donne une carte et réaffiche sa main. Si non, passe la main au croupier.

#### Jouer pour le croupier

La méthode `jouer_croupier()` permet au croupier de prendre des cartes jusqu'à ce qu'il ait au moins 17 points, puis s'arrête.

#### Détermination du gagnant

La méthode `determiner_gagnant()` détermine le gagnant en fonction des règles énoncées précédemment.

## Exécution du programme

Le programme peut être exécuté en créant une instance de la classe `Jeu` et en appelant les méthodes nécessaires pour jouer une partie.
