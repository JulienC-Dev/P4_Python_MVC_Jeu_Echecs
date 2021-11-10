from model.joueur import Joueur
from model.ronde import Ronde
from model.tournoi import Tournoi
from model.participant import Participant
from vues.base import Vues
from tinydb import TinyDB
import pandas as pd


class Controller:

    @classmethod
    def run(cls):
        menu_tournoi = Vues.menu_principal()
        if menu_tournoi == 1:
            nom_tournoi = "test"
            lieu = "paris"
            date = "2020"
            typejeu = "bullet"
            description = "pas de remarque"
            nb_rounds = "4"
            noms = "cormier,pernia,stell,valgu,mitel,al,mars,mechant".split(",")
            prenom = "julien,jessica,hervé,alice,pierre,jacques,c3PO,vador".split(",")
            date_naissances = "2020,1009,2002,1990,2020,2020,2023,2101".split(",")
            sexes = "masculin,feminin,masculin,masculin,masculin,masculin,masculin,masculin".split(",")
            elos = "1,42,5,22,40,10,100,150".split(",")

            participants1 = Participant(noms[0], prenom[0], date_naissances[0], sexes[0], elos[0])
            participants2 = Participant(noms[1], prenom[1], date_naissances[1], sexes[1], elos[1])
            participants3 = Participant(noms[2], prenom[2], date_naissances[2], sexes[3], elos[2])
            participants4 = Participant(noms[3], prenom[3], date_naissances[3], sexes[3], elos[3])
            participants5 = Participant(noms[4], prenom[4], date_naissances[4], sexes[4], elos[4])
            participants6 = Participant(noms[5], prenom[5], date_naissances[5], sexes[5], elos[5])
            participants7 = Participant(noms[6], prenom[6], date_naissances[6], sexes[6], elos[6])
            participants8 = Participant(noms[7], prenom[7], date_naissances[7], sexes[7], elos[7])

            all_participant = [participants1, participants2, participants3, participants4, participants5,
                               participants6, participants7, participants8]

            serialized_players = [p.serialize() for p in all_participant]
            db = TinyDB('db.json')
            players_table = db.table("players")
            players_table.insert_multiple(serialized_players)
            rondes = []
            tournoi = Tournoi(nom_tournoi, lieu, date, typejeu, description, all_participant, rondes, int(nb_rounds))
            cls.tournoi = tournoi
            tournoi.generer_premier_tour()
            Controller.next_round()
            Controller.next_round()
            Controller.next_round()
            tournoi_table = db.table("tournoi")
            serialized_tournoi = tournoi.serialize_tour()
            tournoi_table.insert(serialized_tournoi)
            Controller.menu_rapports()
            Controller.run()

        if menu_tournoi == 2:
            Controller.menu_rapports()
            Controller.run()

        if menu_tournoi == 3:
            Controller.modification_elo_joueur()

    @classmethod
    def modification_elo_joueur(cls):
        Controller.list_elo_joueur()
        Vues.classement_elo_joueur()

    @classmethod
    def list_elo_joueur(cls):
        db = TinyDB('db.json')
        player = db.table("players").all()
        df = pd.DataFrame(player)
        list_player = []
        players = df["joueur"]
        for deserializ in players:
            deserialize_players = Joueur.deserialize(deserializ)
            list_player.append(deserialize_players)
        result = sorted(list_player, key=lambda x: int(x.elo), reverse=True)
        Vues.affiche_console(Vues.list_joueurs_elo(result))


    @classmethod
    def next_round(cls):
        result_menu = Vues.retour_menu()
        if result_menu == 1:
            Controller.menu_rapports()
            Controller.next_round()
        if result_menu == 2:
            tournoi = cls.tournoi
            tournoi.generer_ronde()

    @classmethod
    def affiche_list_joueurs(cls):
        db = TinyDB('db.json')
        player = db.table("players").all()
        df = pd.DataFrame(player).drop("score", axis=1)
        list_player = []
        players = df["joueur"]
        for deserializ in players:
            deserialize_players = Joueur.deserialize(deserializ)
            list_player.append(deserialize_players)
        Vues.affiche_console(Vues.rapport_list_joueurs(list_player))

    @classmethod
    def affiche_classement_aphab_joueurs(cls):
        db = TinyDB('db.json')
        tournois = db.table("tournoi").all()
        df = pd.DataFrame(tournois).drop(["all_participants", "rondes"], axis=1)
        Vues.affiche_console(df)
        selection_tournoi = Vues.choix_tournoi()
        data_frame = pd.DataFrame(tournois)
        players = data_frame["all_participants"][selection_tournoi]
        list_player = []
        for deserializ in players:
            deserialize_players = Participant.deserialize(deserializ)
            list_player.append(deserialize_players)
        Vues.affiche_console(Vues.rapport_ord_joueur(Tournoi.classement_ordre_alpha_joueur(list_player)))

    @classmethod
    def affiche_classement_joueurs(cls):
        db = TinyDB('db.json')
        tournois = db.table("tournoi").all()
        df = pd.DataFrame(tournois).drop(["all_participants", "rondes"], axis=1)
        Vues.affiche_console(df)
        selection_tournoi = Vues.choix_tournoi()
        data_frame = pd.DataFrame(tournois)
        players = data_frame["all_participants"][selection_tournoi]
        list_player = []
        for deserializ in players:
            deserialize_players = Participant.deserialize(deserializ)
            list_player.append(deserialize_players)
        Vues.affiche_console(Vues.rapport_ord_joueur(Tournoi.classement_rank_elo(list_player)))

    @classmethod
    def affiche_rondes(cls):
        db = TinyDB('db.json')
        tournois = db.table("tournoi").all()
        df = pd.DataFrame(tournois).drop(["all_participants", "rondes"], axis=1)
        Vues.affiche_console(df)
        selection_tournoi = Vues.choix_tournoi()
        data_frame = pd.DataFrame(tournois)
        rondes = data_frame["rondes"][selection_tournoi]
        for ronde in rondes:
            deserializ = Ronde.deserialize(ronde)
            Vues.affiche_console(deserializ.nom)
            for i in deserializ.matchs:
                Vues.affiche_rond(list(i)[0], list(i)[1])

    @classmethod
    def affiche_tournoi(cls):
        db = TinyDB('db.json')
        tournois = db.table("tournoi").all()
        df = pd.DataFrame(tournois).drop(["all_participants", "rondes"], axis=1)
        Vues.affiche_console(df)

    @classmethod
    def menu_rapports(cls):
        resultat = Vues.rapport_menu()
        if resultat == 1:
            try:
                cls.affiche_tournoi()
            except KeyError as e:
                Vues.affiche_console(Vues.erreur_rapport())
        elif resultat == 2:
            try:
                cls.affiche_rondes()
            except KeyError as e:
                Vues.affiche_console(Vues.erreur_rapport())
        elif resultat == 3:
            try:
                Controller.affiche_list_joueurs()
            except KeyError as e:
                Vues.affiche_console(Vues.erreur_rapport())
        elif resultat == 4:
            try:
                cls.affiche_classement_aphab_joueurs()
            except KeyError as e:
                Vues.affiche_console(Vues.erreur_rapport())
        elif resultat == 5:
            try:
                cls.affiche_classement_joueurs()
            except KeyError as e:
                Vues.affiche_console(Vues.erreur_rapport())


if __name__ == '__main__':
    pass
