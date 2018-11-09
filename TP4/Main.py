def dictionnaire(fichier):
    # Combien y a-t'il de mots dans le dictionnaire littre.zip ?
    # -> 73192
    # Combien y en a-t'il dans le dictionnaire dico.zip ?
    # -> 336531
    # Quelles sont les expressions Python à évaluer pour obtenir ces valeurs ?
    # -> On utilise la fonction len() et dictionnaire()

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