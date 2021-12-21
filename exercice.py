# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def exercice1(path1, path2):
    with open(path1, 'r', encoding = "utf-8") as f1:
        with open(path2, 'r', encoding = "utf-8") as f2:
            for count, ligne in enumerate(f1):
                ligne2 = f2.readline()
                if ligne != ligne2:
                    return count + 1
    return -1

def exercice2(path, path2):
    with open(path, 'r', encoding = "utf-8") as f, open(path2, 'w', encoding = "utf-8") as f2:
        f2.write(f.read().replace(' ', '   '))

def exercice3(path, path2):
    with open(path, 'r', encoding = "utf-8") as f, open(path2, 'w', encoding = "utf-8") as f2:
        for l in f:
            n = int(l)
            for i, j in PERCENTAGE_TO_LETTER.items():
                if n >= j[0] and n < j[1]:
                    s = str(n) + " " + i + "\n"
                    f2.write(s)

def exercice4():
    with open("recettes.txt", 'a', encoding = "utf-8") as f:
        bol = input("Voulez vous ajouter une recette ? (y/n) ") == "y"
        while bol:
            nom = input("Nom de la recette: ")
            f.write(nom + "\n")
            bolI = input("Voulez vous ajouter un ingrédient ? (y/n) ") == "y"
            while bolI:
                nomI = input("Ingrédient: ")
                f.write("\t-" + nomI + "\n")
                bolI = input("Voulez vous ajouter un ingrédient ? (y/n) ") == "y"
            bol = input("Voulez vous ajouter une recette ? (y/n) ") == "y"
            f.write("\n\n")

def exercice5(path):
    with open(path, 'r', encoding = "utf-8") as f:
        l = f.read().strip().split()
        L = [int(mot) for mot in l if mot.isnumeric()]
        L.sort()
        return L

def exercice6(path, path2):
    with open(path, 'r', encoding = "utf-8") as f, open(path2, 'w', encoding = "utf-8") as f2:
        for count, l in enumerate(f):
            if count % 2 == 0:
                f2.write(l)



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    exercice2("exemple.txt", "exemple3space.txt")
    exercice3("notes.txt", "notesLettres.txt")
    #exercice4()
    print(exercice5("exemple.txt"))
    exercice6("notes.txt", "notes6.txt")
    pass