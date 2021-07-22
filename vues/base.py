class Vues:
    nom_tournoi = input("Entrez le nom du tournoi : ")
    lieu = input("Entrez le lieu du tournoi")
    date = input("Entrer la date du tournoi")
    nb_rounds = input("Entrez le nombre de rounds : ")
    typejeu = input("Entrez le type de jeu: bullet, blitz ou coup rapide ")
    description = input("Remarque du tournoi")
    noms = input("Entrez le nom des participants séparés par un virgule : ")
    prenom = input("Entrez le prenom des participants séparés par un virgule : ")
    date_naissances = input("Entrez la date de naissance des participants séparés par un virgule : ")
    sexes = input("Entrez le sexe de chacun des participants séparés par un virgule : ")
    nom_premier_round = input("nom du premier round : ")
    elos = [1, 42, 5, 22, 40, 10, 100, 150]

if __name__ == '__main__':
    # jeu de test nom tournoi : tournoi
    # jeu de test lieu : paris
    # jeu de test date : paris
    # date du tournoir : 2020
    # jeu de test nombre de round : 4
    # jeu de tesrt type de jeu : bullet
    # description : pas de remarque
    # jeu de test nom : cormier, dupont, kes, plazy, raton, haton, rebel, Stel
    # jeu de test prenom : julien, jessica, hervé, alice, pierre, jacques, C3PO, Vador
    # jeu de test datenaissance :  10/12/90, 21/03/76, 30/12/21, 23/01/94, 24/05/10, 20/03/13, 30/01/01, 01/01/98
    # jeu de test sexe : masculin, feminin, masculin, masculin, masculin, masculin, masculin, masculin

    Vues()



