from random import randint

class NPC:
    def __init__(self, nom, race, espece, profession):
        self.force = meilleurs_des_de_4()
        self.agilite = meilleurs_des_de_4()
        self.constitution = meilleurs_des_de_4()
        self.intelligence = meilleurs_des_de_4()
        self.sagesse = meilleurs_des_de_4()
        self.charisme = meilleurs_des_de_4()
        self.classe_armure = de12()
        self.nom = nom
        self.race = race
        self.espece = espece
        self.points_vie = de20()
        self.profession = profession

    def afficher_caracteristiques(self):
        print(f"""Nom: {self.nom}
Race: {self.race}
Espèce: {self.espece}
Force: {self.force}
Agilité: {self.agilite}
Constitution: {self.constitution}
Intelligence: {self.intelligence}
Sagesse: {self.sagesse}
Charisme: {self.charisme}
Classe armure: {self.classe_armure}
Points vie: {self.points_vie}
Profession: {self.profession}
""")

class Kobold(NPC):
    def __init__(self):
        super().__init__("Kobold", "Kobold", "Kobold", "Kobold")
    def attaquer(self, cible):
        faire_attaque(self, cible)

class Hero(NPC):
    def __init__(self):
        super().__init__("Héros", "Héros", "Héros", "Héros")
    def attaquer(self, cible):
        faire_attaque(self, cible)







def de():
    reponse = randint(1, 6)
    return reponse

def de12():
    reponse = randint(1, 12)
    return reponse

def de20():
    reponse = randint(1, 20)
    return reponse

def de8():
    return randint(1, 8)

def faire_attaque(attaquant, cible):
    de_attaquant = de20()
    if de_attaquant == 20:
        # attaque critique
        cible.points_vie -= de8()
        return 3
    elif de_attaquant == 1:
        # attaque ratée
        return 0
    else:
        if de_attaquant >= cible.classe_armure:
            cible.points_vie -= de()
        else:
            # armure protège
            return 1

# cette fonction va rouler 4 dés, choisir les 3 plus élevés et retourner leur somme
def meilleurs_des_de_4():
    reponses = [de(), de(), de(), de()]
    plus_basse_reponse = min(reponses)
    basse_reponse_index = reponses.index(plus_basse_reponse)
    del reponses[basse_reponse_index]
    return sum(reponses)