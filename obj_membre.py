from obj_couleur import Couleur
from obj_livre import Livre
from obj_auteur import Auteur

class Membre(Couleur):
    nombre_total_membres = 0

    def __init__(self, nom, prenom, date_naissance):
        Membre.nombre_total_membres += 1
        self.id = Membre.nombre_total_membres
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.livres_empruntes = []  # Liste des livres empruntés

    def __str__(self):
        return f"{Membre.BLEU}{self.id}.\t: {Membre.NO_COLOR}{self.prenom} {self.nom} {Membre.MAGENTA}(né(e) le {self.date_naissance}){Membre.NO_COLOR}"

    def emprunter_livre(self, livre):
        """Le membre emprunte un livre s'il est disponible."""
        if livre.disponible:
            livre.disponible = False
            self.livres_empruntes.append(livre)
            print(f"\t{Membre.ROUGE}----> {Membre.VERT}{self.prenom} {self.nom}{Membre.NO_COLOR} a emprunté '{Membre.MAGENTA}{livre.titre}{Membre.NO_COLOR}'.")
        else:
            print(f"\t{Membre.ROUGE}----> {Membre.NO_COLOR}Le livre '{Membre.MAGENTA}{livre.titre}{Membre.NO_COLOR}' est {Membre.ROUGE}déjà emprunté{Membre.NO_COLOR}.")

    def lister_emprunts(self):
        if len(self.livres_empruntes) == 0:
            print(f"\t{Membre.ROUGE}///{Membre.VERT}{self.prenom}{self.nom}{Membre.NO_COLOR}n'a aucun livre emprunté.")
        else:
            for index, livre in enumerate(self.livres_empruntes, start=1):
                print(f"{Membre.ROUGE}->{Membre.VERT}{self.prenom}{self.nom}{Membre.NO_COLOR}a emprunté les livres suivants : \t {index} {livre.titre} de {livre.auteur.prenom} {livre.auteur.nom} \t")

    def restituer_livre(self, livre):
        livre.disponible=True
        self.livres_empruntes.remove(livre)
        print(f"\t{Membre.ROUGE}-----> {Membre.VERT}{self.prenom}{self.nom}{Membre.NO_COLOR} a restitué '{Membre.MAGENTA}{livre.titre}{Membre.NO_COLOR}'.")
if __name__ == "__main__":
    print("Création de 2 instances de Membre et affichage...")
    albert = Membre("EINSTEIN", "Albert", "14/03/1879")
    marie = Membre("CURIE", "Marie", "07/11/1867")
    print(albert)
    print(marie)

    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    livre_1 = Livre("Les Piliers de la Terre", follett, "9782130428114", "1989")
    livre_2 = Livre("Une Colonne de Feu", follett, "9782221157695", "2017")

    print("\n*** 1er affichage des livres empruntés...")
    albert.lister_emprunts()
    marie.lister_emprunts()

    print("\nEmprunts de livres...")
    albert.emprunter_livre(livre_1)
    albert.emprunter_livre(livre_2)
    marie.emprunter_livre(livre_2)

    print("\n*** 2ème affichage des livres empruntés...")
    albert.lister_emprunts()
    marie.lister_emprunts()

    print("\nRestitution d'un livre...")
    albert.restituer_livre(livre_1)

    print("\n*** 3ème affichage des livres empruntés...")
    albert.lister_emprunts()
    marie.lister_emprunts()



