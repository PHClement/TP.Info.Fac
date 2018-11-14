# coding=utf-8
###
### INFO101 - TP6 - Polynomes
###

from tkinter import *
from datetime import datetime


# Question 1
# >>> t1 = [2, 4, 6, 8]
# >>> len(t1)
# 4
# >>> t2 = t1 + [8, 10]
# >>> len(t2)
# 6
# >>> t2[0]
# 2
# >>> t2
# [2, 4, 6, 8, 8, 10]
# >>> t2[4] = 12
# >>> t2
# [2, 4, 6, 8, 12, 10]
# >>> t2 * 2
# [2, 4, 6, 8, 12, 10, 2, 4, 6, 8, 12, 10]

# Question 2
# [0,1,2,3] -> 3X^3+2X^2+X
# [1,2,3] -> 3x^2+2x+1
# [3,2,1] -> x^2+2x+3
# [3,2,1,0] -> x^2+2x+3

def degre(polynome):
    degre = -1
    for index, terme in enumerate(polynome):
        if terme == 0 and index == (len(polynome) - 1):
            break
        degre += 1
    return degre


# >>> degre([0,1,2,3])
# 3
# >>> degre([4,3,2,1,0])
# 3

def calcule_polynome(P, x):
    result = 0
    for index, terme in enumerate(P):
        result += terme * (x ** index)
    return result


# calcule_polynome([1,3,1], 0)
# 1
# calcule_polynome([1,3,1], 1)
# 5
# calcule_polynome([1,3,1], -1)
# -1
# calcule_polynome([1,3,1], 2)
# 11

def affiche_age(nom, annee_naissance):
    annee = datetime.now().year
    print("Bonjour", nom, "!")
    print("Tu as", annee - annee_naissance, "ans.")


# affiche_age("Albert Einstein", 1879)
# ('Bonjour', 'Albert Einstein', '!')
# ('Tu as', 139, 'ans.')

# Question 7
# Etant donné que la fonction est une procédure nous ne pouvons pas stocké le résultat de la fonction dans
# une variable, la variable retournera donc un NoneType

def multiplication_scalaire(P, nb):
    nouveauPolynome = []
    for terme in P:
        nouveauPolynome.append(terme * nb)
    return nouveauPolynome


def oppose(P):
    nouveauPolynome = []
    for terme in P:
        nouveauPolynome.append(-(terme))
    return nouveauPolynome


def symetrique(P):
    nouveauPolynome = []
    for index, terme in enumerate(P):
        nouveauPolynome.append(-(terme) if index % 2 != 0 else terme)
    return nouveauPolynome


def somme_poly(P1, P2):
    nouveauPolynome = []
    if len(P1) > len(P2):
        for index, termeP1 in enumerate(P1):
            if P2[index] is not None:
                nouveauPolynome.append(termeP1 + P2[index])
            else:
                nouveauPolynome.append(termeP1)
    else:
        for index, termeP2 in enumerate(P2):
            if P1[index] is not None:
                nouveauPolynome.append(termeP2 + P1[index])
            else:
                nouveauPolynome.append(termeP2)
    return nouveauPolynome


# Question 12
# Deux arguments P1, P2, qui sont deux tableaux des termes des polynomes.

# somme_poly([1, 2], [2, 3])
# [3, 5]

def derive_poly(P):
    nouveauPolynome = []
    for index, terme in enumerate(P):
        if index == 0:
            continue
        nouveauPolynome.append(terme * index)
    return nouveauPolynome


# derive_poly([18, 3, -25, -5, 7, 2])
# [3, -50, -15, 28, 10]

def chaine_polynome(P):
    polynomeString = ""
    for index, terme in enumerate(P):
        if terme == 0:
            continue
        if index == 0:
            polynomeString += str(terme)
        elif terme < 0:
            if index == 1:
                polynomeString += str(terme) + "X"
            else:
                polynomeString += str(terme) + "X^" + str(index)
        elif index == 1:
            polynomeString += "+" + str(terme) + "X"
        else:
            polynomeString += "+" + str(terme) + "X^" + str(index)
    return polynomeString


# chaine_polynome([1,1,2,-3,4,5])
# '1X^0+1X^1+2X^2+-3X^3+4X^4+5X^5'

# Question 15
# chaine_polynome([3,6,0,-3,-4,0])
# '3+6X-3X^3-4X^4'

def mult_poly(P1, P2):
    nouveauPolynome = [0] * (len(P1) + len(P2) - 1)
    for indexP1, termeP1 in enumerate(P1):
        for indexP2, termeP2 in enumerate(P2):
            nouveauPolynome[indexP1 + indexP2] += termeP1 * termeP2
    return nouveauPolynome

# mult_poly([-2, 4, -3], [1, -1, 0, 1])
# [-2, 6, -7, 1, 4, -3]

# def comp_poly(P1, P2):
    # TODO

########################################################################
### affichage graphique d'un polynôme

def graphe_polynome(x_min, x_max, *polynomes):
    """affiche le graphe de polynômes passés en argument,
entre x_min et x_max"""
    hauteur = 400
    largeur = 600

    if "calcule_polynome" not in globals():
        print("*** La fonction 'calcule_polynome(P, x)' n'est pas définie !")
        print("*** abandon")
        return

    if len(polynomes) == 0:
        print("Il faut donner au moins un polynôme à tracer !")
        print("*** abandon")
        return

    xs = [x_min + (x * (x_max - x_min)) / (largeur - 1) for x in range(largeur)]

    tmp = [[calcule_polynome(p, x) for x in xs] for p in polynomes]

    y_min = min(map(min, tmp))
    y_max = max(map(max, tmp))
    if y_min == y_max:
        y_min -= 1
        y_max += 1

    lines = []
    for ys in tmp:
        line = []
        for i in range(largeur):
            y = ys[i]
            y_pixel = int(((hauteur - 1) * (y - y_min)) / (y_max - y_min))
            line.extend((i, hauteur - 1 - y_pixel))
        lines.append(line)

    root = Tk()
    root.title("graphes de polynômes")
    root.resizable(width=False, height=False)
    root.bind("q", lambda _: root.destroy())
    graphe = Canvas(root, width=largeur, height=hauteur)
    graphe.pack()

    print("affichage des polynomes entre x={} et x={}".format(x_min, x_max))
    print("les valeurs varient  entre y={} et y={}".format(y_min, y_max))
    # les axes
    if x_min * x_max < 0:
        x0 = int(((largeur - 1) * (-x_min)) / (x_max - x_min))
        graphe.create_line(x0, 0, x0, hauteur - 1)
    if y_min * y_max < 0:
        y0 = hauteur - 1 - int(((hauteur - 1) * (-y_min)) / (y_max - y_min))
        graphe.create_line(0, y0, largeur - 1, y0)

    # les polynômes
    couleurs = [("red", "rouge"), ("green", "vert"), ("blue", "bleu"),
                ("magenta", "magenta"), ("cyan", "cyan"), ("grey", "gris"),
                ("orange", "orange"), ("dark violet", "violet"),
                ("brown", "marron"), ("black", "noir")]
    for i in range(len(polynomes)):
        line = lines[i]
        p = polynomes[i]
        c = couleurs[0]
        graphe.create_line(*line, fill=c[0], width=2, smooth=True)
        if "chaine_polynome" in globals():
            print("   {:<7} : {}".format(c[1], chaine_polynome(p), ":", c[1]))
        couleurs = couleurs[1:] + couleurs[0:1]

    print("Appuyez sur la touche 'q' pour quitter la fenêtre graphique.")
    root.mainloop()
