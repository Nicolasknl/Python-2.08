class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Je me nomme {self.nom}, j’ai {self.age} ans")

if __name__ == "__main__":
    animaux = [
    #Animal("Simba", 5),
    #Animal("Beethoven", 3),
    #Animal("César", 26),
    #Animal("Dumbo", 1)
        ]


    for animal in animaux:
        animal.se_presenter()


class Mammifere(Animal):
    def __init__(self, nom, age, race, type_pelage, couleur):
            super().__init__(nom, age)
            self.race = race
            self.type_pelage = type_pelage
            self.couleur = couleur

    def se_presenter(self):
        super().se_presenter()
        print(f"Je suis un(e) {self.race} revêtu de {self.type_pelage} de couleur : {self.couleur}")


#animaux = [Mammifere("Simba", 5, "lion", "poils courts", "fauve clair"),
#Mammifere("Beethoven", 3, "chien", "poils longs", "blanche & fauve"),
#Mammifere("César", 26, "singe", "poils courts", "marron"),
#Mammifere("Dumbo", 1, "éléphanteau", "peau nue", "grise")]
for animal in animaux:
    animal.se_presenter()

class Oiseau(Animal):
    def __init__(self, nom, age, ordre, envergure):
        super().__init__(nom, age)
        self.ordre = ordre
        self.envergure = envergure

    def se_presenter(self):
        super().se_presenter()
        print(f"Je suis un oiseau de type {self.ordre} et mon envergure est de {self.envergure} cm.")

animaux = [ Mammifere("Simba", 5, "lion", "poils courts", "fauve clair"),
Mammifere("Beethoven", 3, "chien", "poils longs", "blanche & fauve"),
Mammifere("César", 26, "singe", "poils courts", "marron"),
Mammifere("Dumbo", 1, "éléphanteau", "peau nue", "grise"),
Oiseau("Hedwige", 7, "rapace", 90),
Oiseau("Blu", 5, "perroquet", 100),
Oiseau("Lago", 12, "perroquet", 60),
Oiseau("Zazu", 40, "passereau", 40)]
for animal in animaux:
    animal.se_presenter()