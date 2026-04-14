from obj_couleur import Couleur

class Auteur(Couleur) :

    nombre_total_auteurs = 0

    def __init__(self, nom, prenom, pays=None, date_naissance=None):
        Auteur.nombre_total_auteurs += 1

        self.id = Auteur.nombre_total_auteurs

        self.nom = nom.upper()

        self.prenom = prenom.capitalize()

        if pays is None:
            self.pays = "inconnu"
        else:
            self.pays = pays

        if date_naissance is None:
            self.date_naissance = "inconnue"
        else:
            self.date_naissance = date_naissance

    def __str__(self):
        return (f" {self.id} : {Couleur.MAGENTA}{self.prenom} {self.nom},"
                f"(né(e) le {self.date_naissance}"
                f" en {self.pays}){Auteur.NO_COLOR}")

if __name__ == "__main__":
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    verne = Auteur("VERNE","Jules","France", "08/02/1828")
    bridou = Auteur("BRIDOU", "Justin", None, None)
    print(follett)
    print(verne)
    print(bridou)
    print(bridou.pays)
    print(bridou.date_naissance)

