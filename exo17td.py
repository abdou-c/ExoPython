#Exercice 17: Faire un programme qui calcule le PGCD de deux nombres saisis au clavier en utilisant l'astuce suivante:
#soustrait le plus petit des deux entiers du plus grand jusqu'à ce qu'ils soient égaux.

nbr1 = int(input("saisir le premier nombre"))
nbr2 = int(input("saisir le deuxieme nombre"))
while(nbr1 != nbr2):
     if(nbr1 < nbr2):
         nbr2 = nbr2 - nbr1
     else:
        nbr1 = nbr1 - nbr2
print("le Pgcd est:", nbr2)