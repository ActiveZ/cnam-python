def test1():
    a = 5
    if a > 0:
        # Si a est supérieur à 0
        print("a est supérieur à 0.")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def bisex():
    try:
        annee = int(input("année:"))
        annee = annee if (annee > 0) else 2000
    except:
        annee = 2000

    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print(f"L'année {annee} saisie est bissextile.")
    else:
        print(f"L'année {annee} saisie n'est pas bissextile.")


def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb

    (max >= 0)"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

carre = lambda x: x*x