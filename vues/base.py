class Vues:

    def affiche_gagner(self, paire):
        return float(input(f'"tapez 1 {paire} si a gagné, 0 s il a perdu, 0.5 si égalité " '))

    def affiche_match(self, paire, color0, color1):
        return print("Match oppposant " + str(paire[0]) + " couleur : " + str(color0) + " et "
                     + str(paire[1]) + " couleur : " + str(color1))

    def debut_round(self, date):
        return print(f'"Début de la Ronde le {date}"')

    def modification_classement_joueur(self):
        joueur_modif = int(input("indiquez le rang du joueur à modifier : "))
        new_rang = int(input("indiquez le nouveau rang du joueur : "))
        print("voici le nouveau classement : ")
        return joueur_modif, new_rang

    @classmethod
    def nom_tournoi(cls):
        return input("Entrez le nom du tournoi : ").strip()

    @classmethod
    def lieu(cls):
        return input("Entrez le lieu du tournoi ").strip()

    @classmethod
    def date(cls):
        return input("Entrer la date du tournoi ").strip()

    @classmethod
    def nb_rounds(cls):
        return input("Entrez le nombre de rounds : ")

    @classmethod
    def typejeu(cls):
        return input("Entrez le type de jeu: bullet, blitz ou coup rapide ")

    @classmethod
    def description(cls):
        return input("Remarque du tournoi ")

    @classmethod
    def noms(cls):
        return input("Entrez le nom des participants séparés par un virgule : ").strip().split(',')

    @classmethod
    def prenom(cls):
        return input("Entrez le prenom des participants séparés par un virgule : ").strip().split(',')

    @classmethod
    def date_naissances(cls):
        return input("Entrez la date de naissance des participants séparés par un virgule : ").strip().split(',')

    @classmethod
    def sexes(cls):
        return input("Entrez le sexe de chacun des participants séparés par un virgule : ").strip().split(',')

    @classmethod
    def elos(cls):
        return input("Entrez l'elo de chacun des participants séparés par un virgule : ").strip().split(',')

    @classmethod
    def nom_premier_round(cls):
        return input("nom du premier round : ")

    @classmethod
    def terminer_round(cls):
        return input("Avez vous terminé le round ? : tapez oui pour le sauvergarder ")

    @classmethod
    def fin_tournoi(cls):
        return print("FIN DU TOURNOI, voici le classement final ")

    @classmethod
    def fin_round(cls, date):
        return print(f'"Fin de la  Ronde le  {date}"')

    @classmethod
    def affiche_classement(cls, classement_score_elo):
        for count, value in enumerate(classement_score_elo, start=1):
            print("Rang", count, value, " - points :", value.score)

    @classmethod
    def modification_classement(cls):
        print("Voulez vous modifier le classements des joueurs")
        return str(input("tapez oui pour le modifier : "))

    @classmethod
    def rapport_ord_joueur(cls, classement_alphabetique):
        print("Rapport : Classement des joueurs par odre aphabétique ")
        for count, value in enumerate(classement_alphabetique, start=1):
            print("Rang", count, value, " - points :", value.score)

    @classmethod
    def rapport_tournoi_all(cls):
        print("Rapport : Liste de tous les tournois ")

    @classmethod
    def rapport_tournoi_ronde(cls, list_ronde):
        print("Rapport : Liste des rondes d'un tournoi ")
        for count, value in enumerate(list_ronde, start=1):
            print("Ronde", count, value)

    @classmethod
    def menu_principal(cls):
        return float(input("Bienvenue\ntapez 1 si souhaitez-vous créer un tournoi \n"
                           "tapez 2 si vous souhaitez consulter les rapports : "))

    @classmethod
    def retour_menu(cls):
        return float(input("Tapez 1, si vous souhaitez revenir à la liste des rapports \n"
                           "Tapez 2, pour reprendre la partie : "
                           ))

    @classmethod
    def rapport_menu(cls):
        return float(input("Quel rapport souhaitez-vous ? \n"
                           "Tapez 1 pour afficher la liste de tous les tournois \n"
                           "Tapez 2 pour afficher la liste de tous les tours d'un tournoi \n"
                           "Tapez 3 pour afficher la liste de joueurs triés par ordre aphabétique \n"
                           "Tapez 4 pour afficher le classement des joueurs d'un tournoi: "))

    @classmethod
    def sauvergarder_match(cls):
        return str(input("souhaitez vous sauvergarder le match ? : "))

    @classmethod
    def choix_tournoi(cls):
        return int(input("Veuillez choisir le numéro du tournoi : "))


if __name__ == '__main__':
    pass