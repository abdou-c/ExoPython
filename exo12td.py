#Exercice 12 : Un nombre est parfait s’il est égal à la somme de ses diviseurs stricts (différents de lui-même).
 #Ainsi par exemple, l’entier 6 est parfait car 6 = 1 + 2 + 3.
#Écrire un algorithme permettant de déterminer si un entier naturel est un nombre parfait.

nbr  = int(input("saisir le nombre"))
somme = 0
for i in range(1,nbr):
    if nbr % i == 0:
        somme = somme + i
if(somme == nbr):
    print("Ce nombre est parfait")
else:
    print("Ce nombre n'est pas parfait")
