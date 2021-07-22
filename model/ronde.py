import time

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

if __name__ == '__main__':
    pass