# coding=utf-8


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


def mots_de_n_lettres(dico, n):
    words = []
    for word in dico:
        if len(word) == n:
            words.append(word)
    return words


def mot_commence_par(mot, prefixe):
    return mot.startswith(prefixe)


def liste_mots_commencent_par(dico, prefixe):
    words = []
    for word in dico:
        if mot_commence_par(word, prefixe):
            words.append(word)
    return words


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


def mots_debut_fin_n(dico, prefixe, suffixe, n):
    words = liste_mots_commencent_par(dico, prefixe)
    wordsStartWith = liste_mots_terminant_par(words, suffixe)
    return mots_de_n_lettres(wordsStartWith, n)


def mot_correspond(mot, motif):
    motifLen = len(motif) - 1
    letterToCheck = []
    for count in range(motifLen):
        if motif[count] != ".":
            letterToCheck.append(count)
    check = True
    for index in letterToCheck:
        if mot[index] != motif[index]:
            check = False
    return check


def liste_mots_motif(dico, motif):
    words = []
    for word in dico:
        if mot_correspond(word, motif):
            words.append(word)
    return words


def retirer_accentuation(mot):
    accents = u"àâçéèêëîïôöùûüÿ"
    normaux = u"aaceeeeiioouuuy"
    nouveaumot = ""
    for lettre in mot:
        index = accents.find(lettre)
        if index >= 0:
            nouveaumot += normaux[index]
        else:
            nouveaumot += lettre
    return nouveaumot


def apparait(lettre, mot):
    return mot in lettre


def mot_possible(mot, lettres):
    motLen = len(mot)
    lettreDansLeMot = []

    for lettre in lettres:
        if lettre in mot:
            lettreDansLeMot.append(lettre)

    return len(lettreDansLeMot) == motLen


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


def mot_optimal_scrabble(dico, lettres):
    words = []

    for word in dico:
        if mot_possible(word, lettres):
            words.append(word)

    return words
