from model import *

if __name__ == '__main__':
    #jeu de test nom tournoi : tournoi
    #jeu de test lieu : paris
    #jeu de test date : paris
    #date du tournoir : 2020
    #jeu de test nombre de round : 4
    #jeu de tesrt type de jeu : bullet
    #description : pas de remarque
    #jeu de test nom : cormier, dupont, kes, plazy, raton, haton, rebel, Stel
    #jeu de test prenom : julien, jessica, hervé, alice, pierre, jacques, C3PO, Vador
    #jeu de test datenaissance :  10/12/90, 21/03/76, 30/12/21, 23/01/94, 24/05/10, 20/03/13, 30/01/01, 01/01/98
    #jeu de test sexe : masculin, feminin, masculin, masculin, masculin, masculin, masculin, masculin

    nom_tournoi = "Grand prix" #input("Entrez le nom du tournoi : ")
    lieu = "Paris" #)input("Entrez le lieu du tournoi")
    date = 2020 #input("Entrer la date du tournoi")
    nb_rounds = 4 #input("Entrez le nombre de rounds : ")
    typejeu = "bullet" #input("Entrez le type de jeu: bullet, blitz ou coup rapide ")
    description = "pas de remarque"  #input("Remarque du tournoi")
    noms = ["cormier", "dupont", "kes", "plazy", "raton", "haton", "rebel", "Stel"] #input("Entrez le nom des participants séparés par un virgule : ")
    prenom = ["julien", "jessica", "hervé", "alice", "pierre", "jacques", "C3PO", "Vador"] #input("Entrez le prenom des participants séparés par un virgule : ")
    date_naissances = [90, 76, 21, 94, 10, 13, 1, 98] #input("Entrez la date de naissance des participants séparés par un virgule : ")
    sexes = ["masculin", "feminin", "masculin", "masculin", "masculin", "masculin", "masculin", "masculin"] #input("Entrez le sexe de chacun des participants séparés par un virgule : ")
    nom_premier_round = "Round 1" #input("nom du premier round : ")
    elos = [1, 42, 5, 22, 40, 10, 100, 150]


    # noms = noms.strip().split(',')
    # prenom = prenom.strip().split(',')
    # date_naissances = date_naissances.strip().split(',')
    # sexes = sexes.strip().split(',')


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

    tournoi = Tournoi(nom_tournoi, lieu, date, typejeu, description, all_participant,  int(nb_rounds))











