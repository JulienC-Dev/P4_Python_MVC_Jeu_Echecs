from operator import attrgetter
import time
import random

class Ronde:
    def __init__(self, nom, matchs, date_debut, date_fin=0):
        self.nom = nom
        self.matchs = matchs
        self.date_debut = date_debut
        self.date_fin = date_fin

    @classmethod
    def date_heure(cls):
        named_tuple = time.localtime()
        time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
        return time_string



class Joueur:
    def __init__(self, nom, prenom, date_naissance, sexe, elo):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.elo = elo

    def __str__(self):
        return self.prenom


class Participant:

    def __init__(self, nom, prenom, date_naissance, sexe, elo, score=0):
        joueur = Joueur(nom, prenom, date_naissance, sexe, elo)
        self.joueur = joueur
        self.score = score



    # def __str__(self):
    #     return str(self.nom) + ' ' + str(self.prenom) + ' ' + str(self.date_naissance) + ' '\
    #            + str(self.sexe) + ' ' +str(self.elo) + ' ' + str(self.score)
    def __str__(self):
        return str(self.joueur)

    def __repr__(self):
        return str(self)

    def win(self):
        self.score += 1

    def draw(self):
        self.score += 0.5

    def lose(self):
        self.score += 0


class Tournoi:

    def __init__(self, nom_tournoi, lieu, date, typejeu, description, all_participant = [],  nb_rounds=4):
        self.nom_tournoi = nom_tournoi
        self.lieu = lieu
        self.date = date
        self.nb_rounds = nb_rounds
        self.all_participant = all_participant
        self.typejeu = typejeu
        self.rondes = []
        self.description = description
        self.generer_premier_tour()

    def prochaine_ronde(self):
        return len(self.rondes) + 1

    def __str__(self):
        return str(self.nom_tournoi) + ' ' + str(self.lieu) + ' ' + str(self.date) + ' '\
               + str(self.typejeu) + ' ' + str(self.description) + ' ' + str(self.all_participant)\
               + ' ' + str(self.nb_rounds)

    def __repr__(self):
        return str(self)

    def classement_elo(self):
        result = sorted(self.all_participant, key=lambda x: x.joueur.elo, reverse=True)
        return result

    def classement_score_elo(self):
        result = sorted(self.all_participant, key=attrgetter('score', 'joueur.elo'), reverse=True)
        return result



    def modified_rang(self, new_rang, last_rang):
        new_rang -= 1
        last_rang -= 1
        result = self.classement_score_elo()
        rang_participant = self.classement_score_elo()[last_rang]
        result.remove(rang_participant)
        result.insert(new_rang, rang_participant)
        return result

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

        ronde = Ronde("Ronde " + str(self.prochaine_ronde()), set_match, print("Début de la Ronde le " + Ronde.date_heure()))
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

        ronde = Ronde("Ronde " + str(self.prochaine_ronde()), set_match, print("Début de la Ronde le " + Ronde.date_heure()))
        self.rondes.append(ronde)
        self.resultat_match()


    def resultat_match(self):
        ronde = self.rondes[-1]
        print(ronde.nom)
        for m in ronde.matchs:
            paire = list(m)

            x = random.choice([True, False])
            if x == True:
                color0 = "blanc"
                color1 = "noir"
            else:
                color0 = "noir"
                color1 = "blanc"

            print("Match oppposant " + str(paire[0]) + " couleur : " + str(color0) + " et "
                  + str(paire[1]) + " couleur : " + str(color1))
            resultat = float(input("tapez 1 si " + str(paire[0]) + " a gagné, 0 s'il a perdu, 0.5 si égalité "))
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
            terminer = input("Avez vous terminé le round ? : tapez oui pour continuer ")
            if terminer == str("oui"):
                ronde.date_fin = Ronde.date_heure()
                print("Fin de la  Ronde le ", ronde.date_fin)
                self.generer_ronde()

        else:
            ronde.date_fin = Ronde.date_heure()
            print("Fin de la  Ronde le ", ronde.date_fin)
            print("FIN DU TOURNOI, voici le classement final")
            for count, value in enumerate(self.classement_score_elo(), start=1):
                print("Rang", count, value, " - points :", value.score)
            print("voulez vous modifier le classements des joueurs")
            reponse = str(input("tapez oui pour le modifier : "))
            if reponse == str("oui"):
                joueur_modif = int(input("indiquez le rang du joueur à modifier : "))
                new_rang = int(input("indiquez le nouveau rang du joueur : "))
                print("voici le nouveau classement : ")
                print(self.modified_rang(new_rang, joueur_modif))



if __name__ == '__main__':
    pass
