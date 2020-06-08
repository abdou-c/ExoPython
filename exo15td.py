#Exercice 15 : Ecrire un algorithme qui demande un nombre de départ, et qui calcule
# la somme des entiers jusqu'à ce nombre.
 #Par exemple si l'on tape 4 , l’algorithme doit calculer: 1 + 2 + 3+ 4 = 10
# Réécrire l'algorithme qui calcule cette fois la moyenne !

val = int(input("saisir une valeur"))
somme = 0
for i in range(1,val+1):
    somme = somme + i
print("le resultat est :",somme )
val1 = float(input("saisir une valeur"))
moyenne = float(val1)/2
print("la moyenne est :",moyenne)