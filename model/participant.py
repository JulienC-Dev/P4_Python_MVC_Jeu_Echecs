from model.joueur import Joueur


class Participant:

    def __init__(self, nom, prenom, date_naissance, sexe, elo, score=0):
        joueur = Joueur(nom, prenom, date_naissance, sexe, elo)
        self.joueur = joueur
        self.score = score

    def __repr__(self):
        return self.joueur.prenom + ' ' + self.joueur.nom

    def win(self):
        self.score += 1

    def draw(self):
        self.score += 0.5

    def lose(self):
        self.score += 0

    def serialize(self):
        return {
            'joueur': self.joueur.serialize(),
            'score': self.score
        }

    @classmethod
    def deserialize(cls, serialized):
        return Participant(
            nom=serialized.get("joueur").get("nom"),
            prenom=serialized.get("joueur").get("prenom"),
            date_naissance=serialized.get("joueur").get("date_naissance"),
            sexe=serialized.get("joueur").get("sexe"),
            elo=serialized.get("joueur").get("elo"),
            score=serialized.get("score")
        )


if __name__ == '__main__':
    pass