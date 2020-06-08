#Exercice 8 : Ecrire un algorithme permettant de résoudre une équation du second degré.
#Ax2 + bx + c = 0
from math import sqrt
a = int(input("saisir les valeurs de A"))
b = int(input("saisir les valeurs de B"))
c = int(input("saisir les valeurs de C"))
delta = pow(b, 2) - 4 * a * c
x1 = -b + sqrt(delta) / 2 * a
x2 = -b - sqrt(delta) / 2 * a
x0 = -b / 2 * a
if (delta > 0):
    print("l'equation admet une solution double")
    x1 = -b + (sqrt(delta)) / 2 * a
    x2 = -b - (sqrt(delta)) / 2 * a
elif (delta == 0):
    print("l'equation admet une racine double")
    x0 = -b / 2 * a
else:
    print("l'equation n'admet pas de solution")