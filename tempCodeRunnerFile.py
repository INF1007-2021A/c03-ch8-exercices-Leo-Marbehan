#!/usr/bin/env python
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

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    exercice2("exemple.txt", "exemple3space.txt")
    pass