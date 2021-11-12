class Vues:

    def affiche_gagner(self, paire):
        return float(input(f'"tapez 1 {paire} si a gagné, 0 s il a perdu, 0.5 si égalité " '))

    def affiche_match(self, paire, color0, color1):
        return print("Match oppposant " + str(paire[0]) + " couleur : " + str(color0) + " et "
                     + str(paire[1]) + " couleur : " + str(color1))

    def debut_round(self, date):
        return print(f'"Début de la Ronde le {date}"')

    @classmethod
    def classement_elo_joueur(cls):
        joueur_modif = int(input("indiquez le rang du joueur à modifier : "))
        new_elo = int(input("indiquez l'elo du nouveau joueur : "))
        print("Voici le nouveau classement par l'élo: ")
        return joueur_modif, new_elo

    @classmethod
    def affiche_rond(cls, match0, match1):
        return print("Match - ", match0, "VS", match1)

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
        return input("Entrez le nom des participants séparés par un virgule sans espace : ").strip().split(',')

    @classmethod
    def prenom(cls):
        return input("Entrez le prenom des participants séparés par un virgule sans espace : ").strip().split(',')

    @classmethod
    def date_naissances(cls):
        return input("Entrez la date de naissance des participants séparés par un virgule  "
                     "sans espace: ").strip().split(',')

    @classmethod
    def sexes(cls):
        return input("Entrez le sexe de chacun des participants séparés par un virgule "
                     "sans espace : ").strip().split(',')

    @classmethod
    def elos(cls):
        return input("Entrez l'elo de chacun des participants séparés par un virgule"
                     " sans espace : ").strip().split(',')

    @classmethod
    def nom_premier_round(cls):
        return input("nom du premier round : ")

    @classmethod
    def terminer_round(cls):
        return input("Souhaitez-vous passer au round suivant ? : ")

    @classmethod
    def fin_tournoi(cls):
        return print("FIN DU TOURNOI, voici le classement final ")

    @classmethod
    def fin_round(cls, date):
        return print(f'"Fin du tour le  {date}"')

    @classmethod
    def affiche_classement(cls, classement_score_elo):
        for count, value in enumerate(classement_score_elo, start=1):
            print("Rang", count, value, " - points :", value.score)

    @classmethod
    def affiche_classement_elo(cls, classement_elo):
        for count, value in enumerate(classement_elo, start=1):
            print("Rang", count, value, " - élo :", value.joueur.elo)


    @classmethod
    def rapport_ord_joueur(cls, classement_alphabetique):
        print("Rapport : Classement des joueurs par odre aphabétique ")
        for count, value in enumerate(classement_alphabetique, start=1):
            print("Rang", count, value, " - points :", value.score)

    @classmethod
    def rapport_list_joueurs(cls, list_players):
        print("Liste des joueurs : ")
        for count, value in enumerate(list_players, start=1):
            print("Joueur", count, "-", value.prenom, value.nom)

    @classmethod
    def list_joueurs_elo(cls, list_players):
        print("Voici le classements des joueurs par l'élo : ")
        for count, value in enumerate(list_players, start=1):
            print("Joueur", count, "-", value.prenom, value.nom, " - élo :", value.elo)

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
                           "tapez 2 si vous souhaitez consulter les rapports \n"
                           "tapez 3 si vous souhaitez modifier l'élo d'un joueur : "))

    @classmethod
    def retour_menu(cls):
        return float(input("Tapez 1, si vous souhaitez revenir à la liste des rapports \n"
                           "Tapez 2, pour reprendre la partie : "))

    @classmethod
    def rapport_menu(cls):
        return float(input("Quel rapport souhaitez-vous ? \n"
                           "Tapez 1 pour afficher la liste de tous les tournois \n"
                           "Tapez 2 pour afficher la liste de tous les tours d'un tournoi \n"
                           "Tapez 3 pour afficher la liste des joueurs \n"
                           "Tapez 4 pour afficher la liste de joueurs triés par ordre aphabétique \n"
                           "Tapez 5 pour afficher le classement des joueurs d'un tournoi: "))

    @classmethod
    def sauvergarder_match(cls):
        return str(input("souhaitez vous sauvergarder le match ? : "))

    @classmethod
    def choix_tournoi(cls):
        return int(input("Quel tournoi voulez vous voir : "))

    @classmethod
    def affiche_console(cls, affiche):
        return print(affiche)

    @classmethod
    def erreur_rapport(cls):
        return print("Opps, pas de classement encore disponible \n"
                     "retour au Menu Principal")


if __name__ == '__main__':
    pass
