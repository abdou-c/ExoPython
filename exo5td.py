#Exercice 5 :
#Ecrire un programme qui saisit 5 variables de type entier au clavier et qui affiche leur somme.\
    #Utiliser une boucle (for ou while ou do..while).
somme = 0
for i in range(5):
    val = int(input("saisir valeur"))
    somme = somme + val
print("la somme est :", + somme)
