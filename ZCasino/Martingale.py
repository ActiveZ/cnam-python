from random import randrange
from math import ceil

def Martingale():
    # Déclaration des variables de départ
    n = 0
    miseDepart = 10
    mise = miseDepart
    gain = 0
    argent = 1000 # On a 1000 $ au début du jeu
    print("Vous vous installez à la table de roulette avec", argent, "$.")

    nbPartie = int(input("Combien de parties voulez-vous jouer ?"))

    while n < nbPartie and argent >= 0:
        nombre_mise = 1 # numéro misé
        numero_gagnant = randrange(50)

        # On établit le gain du joueur
        if numero_gagnant == nombre_mise:
            argent += mise * 3
            mise = miseDepart
            print("Vous avez gagné: " + str(mise * 3))

        elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur
            gain = mise
            # gain = ceil(mise * 0.5)
            argent += gain
            mise = miseDepart
            print("Vous avez gagné: " + str(gain))

        else:
            argent -= mise
            print("Vous avez perdu: " + str(mise))
            mise = mise * 2
            if mise > argent:
                mise = argent
            print("Mise: " + str(mise))

        print("Argent: " + str(argent))
        n += 1

    print("Nombre de coups joués: " + str(n))
    # On interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        continuer_partie = False
    else:
        # On affiche l'argent du joueur
        print("Vous avez à présent", argent, "$")





