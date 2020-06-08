#Exercice 6 :
#Faire un programme qui saisit  les coordonnées de 2 points A (x1, y1) et b(x2, y2) et qui affiche la distance entre les 2 points.
#Formule : distante = racine carrée de ((x1 – x2)2  + (y1 – y2)2)
 #Racine carrée : sqrt. Ex : sqrt(7) ; <math.h>
from math import sqrt
print("saisir les coordonnees de A")
x1 = float(input("saisir x1"))
y1 = float(input("saisir y1"))
print("saisir les coordonnees de B")
x2 = float(input("saisir x2"))
y2 = float(input("saisir y2"))
distance = sqrt(pow((x1 - x2),2) + pow((y1 - y2),2));
print("la distance est :", + distance)

