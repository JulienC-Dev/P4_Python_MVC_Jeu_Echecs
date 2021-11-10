PROJET 4

Programme jeu d'échecs :

l'application permet à l'utilisateur de créer et d'éditer des tournois d'échecs.
Le programme automatise la gestion des matchs en fonction de différents critères comme l'élo.

1 - Pré-requis pour lancer l'application:

- Installer la dernière version de Python sur le site : https://www.python.org
- Ouvrir l'interpréteur des commandes de Python (terminal sur Mac)
- Créer un nouveau repertoire via la commande "mkir" exemple : tapez - mkdir projets dans la console
- Tapez dans la console : git init
- Tapez dans la console : git clone https://github.com/JulienC-Dev/JulienC-Dev.git:projets
(le "projets" peut être remplacé par le nom de votre choix)
- Créer un environnement virtuel - Tapez dans la console : python -m venv
- installer les packets nécessaires via la commande - pip install -r /projets/requirements.txt


1.1 - Gestion des rapports flake8

Permet un code propre et maintenable

Générer un nouveau rapport flake8 :

- tapez dans la commande : pip install flake8 et pip install flake8-html pour permettre l'enregistrement des rapports
- créer un dossier nommé  "flake8_rapport" avec la commande : Mkdir flake8_rapport
- l'option de longueur de ligne maximum pour le projet est de 119. l'option est : --max-line-length=119
- tapez dans la console les lignes suivantes pour générer les rapports :
 - flake8 --output-file flake8_rapport/main.html --max-line-length=119 --htmldir=Desktop/OpenclassRooms/
 Projet\ 4(Emplacement du dossier)/ model/main.py
 - flake8 --output-file flake8_rapport/tournoi.html --max-line-length=119 --htmldir=Desktop/OpenclassRooms/
 Projet\ 4(Emplacement du dossier)/model/tournoi.py
 - flake8 --output-file flake8_rapport/ronde.html --max-line-length=119 --htmldir=Desktop/OpenclassRooms/
 Projet\ 4(Emplacement du dossier)/model/ronde.py
 - flake8 --output-file flake8_rapport/joueur.html --max-line-length=119 --htmldir=Desktop/OpenclassRooms/
 Projet\ 4(Emplacement du dossier)/model/joueur.py
 - flake8 --output-file flake8_rapport/participant.html --max-line-length=119 --htmldir=Desktop/OpenclassRooms/
 Projet\ 4(Emplacement du dossier)/ model/participant.py
 - flake8 --output-file flake8_rapport/main.html --max-line-length=119 --htmldir=Desktop/OpenclassRooms/
 Projet\ 4/ main.py


1.2 - Démarage de l'application
lancer l'application via la commande : python main.py
L'utilisateur peut créer un tournoi et naviguer dans les rapports d'un tournoi

1.3 - Jeu de données
nom_tournoi = test
lieu = paris
date = 2020
typejeu = bullet
description = pas de remarque
nb_rounds = 4
noms = cormier,pernia,michet,valo,mitel,hal,mars,smith
prenom = julien,jessica,hervé,alice,pierre,jacques,paul,albert
date_naissances = 10/02/1990,11/01/1950,07/05/1987,10/06/1956,04/09/1995,08/11/2020,10/01/2020,29/12/1956
sexes = masculin,feminin,masculin,masculin,masculin,masculin,masculin,masculin
elos = 1, 42, 5, 22, 40, 10, 100, 150

Version
0.1

Auteur
JulienC-Dev - github : https://github.com/JulienC-Dev/P4_echecs


