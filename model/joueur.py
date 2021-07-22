class Joueur:
    def __init__(self, nom, prenom, date_naissance, sexe, elo):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.elo = elo

    def __str__(self):
        return self.prenom