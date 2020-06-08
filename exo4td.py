#Exercice 4
#Ecrire un programme qui saisit un réel x et un entier n et affiche x à la puissance n.
#Version 1 : utiliser la fonction pow  du fichier d’en-tête <math.h>  ex : pow(x,n)
#Version 2 : en utilisant un boucle
#version1
x = float(input("saisir un réel"))
n = int(input("saisir un entier"))
puissance = pow(x, n)
print("X a la puissance N est :", + puissance)

#version2
for cpt in range(1, n):
    puissance = puissance * x