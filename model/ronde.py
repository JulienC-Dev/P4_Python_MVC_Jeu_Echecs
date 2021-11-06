import time
from model.participant import Participant


class Ronde:

    def __init__(self, nom, matchs, date_debut, date_fin=0):
        self.nom = nom
        self.matchs = matchs
        self.date_debut = date_debut
        self.date_fin = date_fin

    def __str__(self):
        return self.nom + ' ' + self.matchs

    def __repr__(self):
        return self.nom + ' ' + self.matchs

    @classmethod
    def date_heure(cls):
        named_tuple = time.localtime()
        time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
        return time_string

    def serialize_ronde(self):
        serialize_round = {
            'nom': self.nom,
            'matchs': [[list(m)[0].serialize(), list(m)[1].serialize()] for m in self.matchs],
            'date_debut': self.date_debut,
            'date_fin': self.date_fin
        }
        return serialize_round

    @classmethod
    def deserialize(cls, serialized):
        return Ronde(
            nom=serialized.get("nom"),
            matchs=[{Participant.deserialize(m[0]), Participant.deserialize(m[1])} for m in serialized.get("matchs")],
            date_debut=serialized.get("date_debut"),
            date_fin=serialized.get("date_fin"))


if __name__ == '__main__':
    pass
