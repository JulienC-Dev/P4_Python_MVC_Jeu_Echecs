from model.joueur import Joueur
from model.joueur import Tournoi

from vues import *

class Controller:

    def __init__(self):
        

    def get_participant(self):
        participants1 = Participant(noms[0], prenom[0], date_naissances[0], sexes[0], elos[0])
        participants2 = Participant(noms[1], prenom[1], date_naissances[1], sexes[1], elos[1])
        participants3 = Participant(noms[2], prenom[2], date_naissances[2], sexes[3], elos[2])
        participants4 = Participant(noms[3], prenom[3], date_naissances[3], sexes[3], elos[3])
        participants5 = Participant(noms[4], prenom[4], date_naissances[4], sexes[4], elos[4])
        participants6 = Participant(noms[5], prenom[5], date_naissances[5], sexes[5], elos[5])
        participants7 = Participant(noms[6], prenom[6], date_naissances[6], sexes[6], elos[6])
        participants8 = Participant(noms[7], prenom[7], date_naissances[7], sexes[7], elos[7])

    all_participant = [participants1, participants2, participants3, participants4, participants5, participants6,
                       participants7, participants8]

    tournoi = Tournoi(nom_tournoi, lieu, date, typejeu, description, all_participant, int(nb_rounds))

if __name__ == '__main__':
    # noms = noms.strip().split(',')
    # prenom = prenom.strip().split(',')
    # date_naissances = date_naissances.strip().split(',')
    # sexes = sexes.strip().split(',')
    Controller()

