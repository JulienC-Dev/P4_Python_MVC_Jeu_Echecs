import random
from operator import attrgetter
from model.participant import Participant
from model.ronde import Ronde
from vues.base import Vues


class Tournoi:

    def __init__(self, nom_tournoi, lieu, date, typejeu, description, all_participant=[], rondes=[], nb_rounds=4):
        self.nom_tournoi = nom_tournoi
        self.lieu = lieu
        self.date = date
        self.nb_rounds = nb_rounds
        self.all_participant = all_participant
        self.typejeu = typejeu
        self.rondes = rondes
        self.description = description

    def __str__(self):
        return str(self.nom_tournoi) + ' ' + str(self.lieu) + ' ' + str(self.date) + ' '\
               + str(self.typejeu) + ' ' + str(self.description) + ' ' + str(self.all_participant)\
               + ' ' + str(self.nb_rounds) + ' ' + str(self.rondes)

    def __repr__(self):
        return str(self)

    def prochaine_ronde(self):
        return len(self.rondes) + 1

    def classement_elo(self) -> list:
        result = sorted(self.all_participant, key=lambda x: int(x.joueur.elo), reverse=True)
        return result

    def classement_score_elo(self):
        result = sorted(self.all_participant, key=attrgetter('score', 'joueur.elo'), reverse=True)
        return result

    def list_ronde(self):
        list_rondes = self.rondes
        return list_rondes

    # def modified_elo(self, pos_joueur, new_elo):
    #     pos_joueur -= 1
    #     player = self.classement_elo()[pos_joueur]
    #     player.joueur.elo.strip()
    #     player.joueur.elo = new_elo
    #     classement = self.classement_elo()
    #     vues = Vues()
    #     vues.affiche_classement_elo(classement)

    # def modification_classement(self):
    #     Vues.modification_classement()
    #     vues = Vues()
    #     vues.affiche_classement_elo(self.classement_elo())
    #     modification_classement = vues.classement_elo_joueur()
    #     self.modified_elo(modification_classement[0], modification_classement[1])

    def valid_pair(self, paire):
        for ronde in self.rondes:
            for match in ronde.matchs:
                if match == paire:
                    return False
        return True

    def generer_premier_tour(self):
        res = self.classement_elo()
        list_sup = res[0:4]
        list_inf = res[4:8]
        trie_first_tour = list(zip(list_inf, list_sup))
        set_match = [set(p) for p in trie_first_tour]
        vues = Vues()
        ronde = Ronde("Ronde " + str(self.prochaine_ronde()), set_match, vues.debut_round(Ronde.date_heure()))

        self.rondes.append(ronde)
        self.resultat_match()

    def trouve_match(self, joueur, joueurs_restants):
        for j in joueurs_restants:
            if self.valid_pair({joueur, j}):
                return j
        return joueurs_restants[0]

    def generer_ronde(self):
        joueurs = self.classement_score_elo()
        set_match = []
        while joueurs:
            j1 = joueurs[0]
            joueurs.remove(j1)
            j2 = self.trouve_match(j1, joueurs)
            joueurs.remove(j2)
            set_match.append({j1, j2})

        vues = Vues()
        ronde = Ronde("Ronde " + str(self.prochaine_ronde()), set_match, vues.debut_round(Ronde.date_heure()))
        self.rondes.append(ronde)
        self.resultat_match()

    def resultat_match(self):
        ronde = self.rondes[-1]
        print(ronde.nom)
        for m in ronde.matchs:
            paire = list(m)
            x = random.choice([True, False])
            if x is True:
                color0 = "blanc"
                color1 = "noir"
            else:
                color0 = "noir"
                color1 = "blanc"

            vues = Vues()
            vues.affiche_match(paire, color0, color1)
            resultat = vues.affiche_gagner(paire[0])

            if resultat == 1:
                paire[0].win()
                paire[1].lose()
            elif resultat == 0:
                paire[0].lose()
                paire[1].win()
            elif resultat == 0.5:
                paire[0].draw()
                paire[1].draw()

        if self.prochaine_ronde() <= self.nb_rounds:
            terminer_round = Vues.terminer_round()
            if terminer_round == str("oui"):
                ronde.date_fin = Ronde.date_heure()
                vues = Vues()
                vues.fin_round(ronde.date_fin)

        else:
            ronde.date_fin = Ronde.date_heure()
            vues = Vues()
            vues.fin_round(ronde.date_fin)
            Vues.fin_tournoi()
            vues.affiche_classement(self.classement_score_elo())

    def serialize_tour(self) -> dict:
        serialized_tournoi = {
            'nom_tournoi': self.nom_tournoi,
            'lieu': self.lieu,
            'date': self.date,
            'typejeu': self.typejeu,
            'description': self.description,
            'nb_round': self.nb_rounds,
            'all_participants': [p.serialize() for p in self.all_participant],
            'rondes': [r.serialize_ronde() for r in self.rondes]
        }
        return serialized_tournoi

    @classmethod
    def deserialize_tour(cls, serialized):
        return Tournoi(
            nom_tournoi=serialized.get("nom_tournoi"),
            lieu=serialized.get("lieu"),
            date=serialized.get("date"),
            typejeu=serialized.get("typejeu"),
            description=serialized.get("description"),
            nb_rounds=serialized.get("nb_round"),
            rondes=[Ronde.deserialize(ronde) for ronde in serialized.get("rondes")],
            all_participant=[Participant.deserialize(p) for p in serialized.get("all_participants")]
        )

    @classmethod
    def classement_ordre_alpha_joueur(cls, deserialize):
        result = sorted(deserialize, key=lambda x: x.joueur.prenom.lower())
        return result

    @classmethod
    def classement_rank_elo(cls, deserialize):
        result = sorted(deserialize, key=attrgetter('score', 'joueur.elo'), reverse=True)
        return result


if __name__ == '__main__':
    pass
