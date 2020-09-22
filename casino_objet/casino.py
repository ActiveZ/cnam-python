
from random import randrange
from math import ceil
from casino_objet.joueur import Joueur

class Casino_Objet:

    def launchCasino(self):
        # Déclaration des variables de départ
        continuer_partie = True # Booléen qui est vrai tant qu'on doit continuer la partie
        j1 = Joueur()

        print("Vous vous installez à la table de roulette avec", j1.argent, "$.")

        # Tant qu'on doit continuer la partie on demande à l'utilisateur de saisir le nombre sur lequel il va miser
        while continuer_partie:
            # on sélectionne la somme à miser sur le nombre
            j1.miser()

            # on sélectionne le nombre sur lequel miser
            j1.choixNombre()

            # Le nombre misé et la mise ont été sélectionnés par l'utilisateur, on fait tourner la roulette
            numero_gagnant = randrange(50)
            print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

            # On établit le gain du joueur
            if numero_gagnant == j1.nombre_mise:
                print("Félicitations ! Vous obtenez", j1.mise * 3, "$ !")
                j1.argent += j1.mise * 3
            elif numero_gagnant % 2 == j1.nombre_mise % 2: # ils sont de la même couleur
                j1.mise = ceil(j1.mise * 0.5)
                print("Vous avez misé sur la bonne couleur. Vous obtenez", j1.mise, "$")
                j1.argent += j1.mise
            else:
                print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
                j1.argent -= j1.mise

            # remet la mise à 0 et le nombre choisi = -1
            j1.resetJeu()

            # On interrompt la partie si le joueur est ruiné
            if j1.argent <= 0:
                print("Vous êtes ruiné ! C'est la fin de la partie.")
                continuer_partie = False
            else:
                # On affiche l'argent du joueur
                print("Vous avez à présent", j1.argent, "$")
                quitter = input("Souhaitez-vous quitter le casino (o/N) ? ")
                if quitter.lower() == "o":
                    print("Vous quittez le casino avec vos gains.")
                    continuer_partie = False

