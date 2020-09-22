
from pendu_objet.donnees import *
from random import choice

class Pendu:

    def LaunchPendu(self):

        # Notre variable pour savoir quand arrêter la partie
        continuer_partie = 'o'
        # Nombre de coups par partie
        nb_coups = 8

        while continuer_partie != 'n':
            mot_a_trouver = choice(liste_mots)
            lettres_trouvees = []
            mot_trouve = self._recup_mot_masque(mot_a_trouver, lettres_trouvees)
            nb_chances = nb_coups
            while mot_a_trouver!=mot_trouve and nb_chances>0:
                print("Mot à trouver {0} (encore {1} chances)".format(mot_trouve, nb_chances))
                lettre = self._recup_lettre()
                if lettre in lettres_trouvees: # La lettre a déjà été choisie
                    print("Vous avez déjà choisi cette lettre.")
                elif lettre in mot_a_trouver: # La lettre est dans le mot à trouver
                    lettres_trouvees.append(lettre)
                    print("Bien joué.")
                else:
                    nb_chances -= 1
                    print("... non, cette lettre ne se trouve pas dans le mot...")
                mot_trouve = self._recup_mot_masque(mot_a_trouver, lettres_trouvees)

            # A-t-on trouvé le mot ou nos chances sont-elles épuisées ?
            if mot_a_trouver==mot_trouve:
                print("Félicitations ! Vous avez trouvé le mot {0}.".format(mot_a_trouver))
            else:
                print("PENDU !!! Vous avez perdu.")

            continuer_partie = input("Souhaitez-vous continuer la partie (O/n) ?")
            continuer_partie = continuer_partie.lower()

    def _recup_lettre(self):
        """Cette fonction récupère une lettre saisie par
            l'utilisateur. Si la chaîne récupérée n'est pas une lettre,
            on appelle récursivement la fonction jusqu'à obtenir une lettre"""

        lettre = input("Tapez une lettre: ")
        lettre = lettre.lower()
        if len(lettre) > 1 or not lettre.isalpha():
            print("Vous n'avez pas saisi une lettre valide.")
            return self._recup_lettre()
        else:
            return lettre


    def _recup_mot_masque(self, mot_complet, lettres_trouvees):
        """Cette fonction renvoie un mot masqué tout ou en partie, en fonction :
        - du mot d'origine (type str)
        - des lettres déjà trouvées (type list)

        On renvoie le mot d'origine avec des * remplaçant les lettres que l'on
        n'a pas encore trouvées."""

        mot_masque = ""
        for lettre in mot_complet:
            if lettre in lettres_trouvees:
                mot_masque += lettre
            else:
                mot_masque += "*"
        return mot_masque