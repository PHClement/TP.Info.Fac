# coding=utf-8
import unicodedata

def dictionnaire(fichier):
    import zipfile
    import sys

    f = zipfile.ZipFile(fichier, 'r')
    file_list = f.namelist()
    if len(file_list) != 1:
        print("*** L'archive devrait contenir exactement 1 fichier mais en contient {}".format(len(file_list)))
        sys.exit(1)
    r = f.read(file_list[0]).decode(encoding="UTF-8", errors="strict").split("\n")
    return [m for m in r if len(m) != 0]


littre = dictionnaire("ressources/littre.zip")
dico = dictionnaire("ressources/dico.zip")

# Combien y a-t'il de mots dans le dictionnaire littre.zip ?
# -> 73192
# Combien y en a-t'il dans le dictionnaire dico.zip ?
# -> 336531
# Quelles sont les expressions Python à évaluer pour obtenir ces valeurs ?
# -> On utilise la fonction len() et dictionnaire()

def mots_de_n_lettres(dico, n):
    words = []
    for word in dico:
        if len(word) == n:
            words.append(word)
    return words

## mots_de_n_lettres(littre, 22)
## -> [u'cristallographiquement', u'disproportionnellement']
## len(mots_de_n_lettres(dico, 10))
## -> 51402

def mot_commence_par(mot, prefixe):
    return mot.startswith(prefixe)

## >>> mot_commence_par("temoignage", "te")
## True
## >>> mot_commence_par("chouette", "choux")
## False
## >>> mot_commence_par("chou", "chouette")
## False
## >>> mot_commence_par("chouette", "clou")
## False

def liste_mots_commencent_par(dico, prefixe):
    words = []
    for word in dico:
        if mot_commence_par(word, prefixe):
            words.append(word)
    return words

## >>> len(liste_mots_commencent_par(littre, "chou"))
## 17

def mot_terminant_par(mot, suffixe):
    suffixeLen = len(suffixe) - 1
    motLen = len(mot) - 1

    checkLetter = True
    for count in range(0, suffixeLen + 1):
        if not checkLetter:
            break
        if mot[motLen - count] != suffixe[suffixeLen - count]:
            checkLetter = False

    return checkLetter


def liste_mots_terminant_par(dico, suffixe):
    words = []
    for word in dico:
        if mot_terminant_par(word, suffixe):
            words.append(word)
    return words

## Quels sont les mots du dictionnaire « le Littré » se terminant par "chou" ?
## >>> liste_mots_terminant_par(littre, "chou")
## [u'bachou', u'cachou', u'chabichou', u'chou']

def mots_debut_fin_n(dico, prefixe, suffixe, n):
    words = liste_mots_commencent_par(dico, prefixe)
    wordsStartWith = liste_mots_terminant_par(words, suffixe)
    return mots_de_n_lettres(wordsStartWith, n)

# Combien y a-t-il de mots commençant par "cas", se terminant par "ns" et comportant 12 lettres dans le
# dictionnaire avec conjugaisons ?
#
# >>> len(mots_debut_fin_n(dico, "cas", "ns", 12))
# 7

def mot_correspond(mot, motif):
    lettreAVerifier = []
    noAccentMot = retirer_accentuation(mot)
    noAccentMotif = retirer_accentuation(motif)

    if len(mot) != len(motif):
        return False

    for index, lettre in enumerate(noAccentMotif):
        if lettre != ".":
            lettreAVerifier.append(index)

    check = True

    for lettre in lettreAVerifier:
        if noAccentMot[lettre] != noAccentMotif[lettre]:
            check = False

    return check

# >>> mot_correspond("tarte", "t..t.")
# True
# >>> mot_correspond("cheval", "c..v..l")
# False
# >>> mot_correspond("cheval", "c..v.l")
# True
# >>> mot_correspond("salut", ".al..")
# True

def liste_mots_motif(dico, motif):
    words = []
    for word in dico:
        if mot_correspond(word, motif):
            words.append(word)
    return words

# Compter le nombre de mots correspondant au motif "p..h.s" dans le dictionnaire avec conjugaisons.
# >>> len(liste_mots_motif(dico, "p..h.s"))
# 12

def retirer_accentuation(mot):
    try:
        mot = unicode(mot, 'utf-8')
    except (TypeError, NameError):
        pass
    text = unicodedata.normalize('NFD', mot)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)


def apparait(lettre, mot):
    return mot in lettre


def mot_possible(mot, lettres):
    motLen = len(mot)
    lettreDansLeMot = []

    for lettre in lettres:
        if lettre in mot:
            lettreDansLeMot.append(lettre)

    return len(lettreDansLeMot) == motLen

# >>> mot_possible("lapin", "abilnpq")
# True
# >>> mot_possible("cheval", "abilnpq")
# False
# >>> mot_possible("chapeau", "abcehpuv")
# True
# >>> mot_possible("salut", "taslu")
# True

def mot_optimal(dico, lettres):
    words = []

    for word in dico:
        if mot_possible(word, lettres):
            words.append(word)

    return words


def mot_possible_scrabble(mot, lettres):
    motLen = len(mot)
    lettreDansLeMot = []

    for lettre in lettres:
        if lettre in mot:
            lettreDansLeMot.append(lettre)

    return len(lettreDansLeMot) == motLen

# >>> mot_possible_scrabble("chapeau", "abcehpuv")
# False
# >>> mot_possible_scrabble("chapeau", "abcehpuva")
# True

def mot_optimal_scrabble(dico, lettres):
    words = []

    for word in dico:
        if mot_possible(word, lettres):
            words.append(word)

    return words
