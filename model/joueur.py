class Joueur:
    def __init__(self, nom, prenom, date_naissance, sexe, elo):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.elo = elo

    def __repr__(self):
        return self.prenom

    def serialize(self) -> dict:
        serialized_player = {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_naissance': self.date_naissance,
            'sexe': self.sexe,
            'elo ': self.elo
        }
        return serialized_player

    @classmethod
    def deserialize(cls, serialized) -> "Joueur":
        return Joueur(
            nom=serialized.get("nom"),
            prenom=serialized.get("prenom"),
            date_naissance=serialized.get("date_naissance"),
            sexe=serialized.get("sexe"),
            elo=serialized.get("elo"))


if __name__ == '__main__':
    pass
