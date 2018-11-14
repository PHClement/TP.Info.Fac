# coding=utf-8
###
### INFO101 - TP6 - Polynomes
###

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
    print("Tu as", annee-annee_naissance, "ans.")

# affiche_age("Albert Einstein", 1879)
# ('Bonjour', 'Albert Einstein', '!')
# ('Tu as', 139, 'ans.')

# Question 7
# Etant donné que la fonction est une procédure nous ne pouvons pas stocké le résultat de la fonction dans
# une variable, la variable retournera donc un NoneType


