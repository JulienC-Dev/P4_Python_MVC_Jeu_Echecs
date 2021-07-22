class Participant:

    def __init__(self, nom, prenom, date_naissance, sexe, elo, score=0):
        joueur = Joueur(nom, prenom, date_naissance, sexe, elo)
        self.joueur = joueur
        self.score = score

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

