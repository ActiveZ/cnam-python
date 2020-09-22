class Joueur:

    def __init__(self):
        self.argent = 1000
        self.mise = -1
        self.nombre_mise = -1

    def miser(self):
        while self.mise <= 0 or self.mise > self.argent:
            mise = input("Tapez le montant de votre mise : ")
            # On convertit la mise
            try:
                self.mise = int(mise)
            except ValueError:
                print("Vous n'avez pas saisi de nombre")
                self.mise = -1
                continue
            if self.mise <= 0:
                print("La mise saisie est négative ou nulle.")
            if self.mise > self.argent:
                print("Vous ne pouvez miser autant, vous n'avez que", self.argent, "$")


    def choixNombre(self):
        # on demande à l'utilisateur de saisir le nombre sur lequel il va miser
        while self.nombre_mise < 0 or self.nombre_mise > 49:
            nombre_mise = input("Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : ")
            # On convertit le nombre misé
            try:
                self.nombre_mise = int(nombre_mise)
            except ValueError:
                print("Vous n'avez pas saisi de nombre")
                self.nombre_mise = -1
                continue
            if self.nombre_mise < 0:
                print("Ce nombre est négatif")
            if self.nombre_mise > 49:
                print("Ce nombre est supérieur à 49")

    def resetJeu(self):
        self.mise = 0
        self.nombre_mise = -1
