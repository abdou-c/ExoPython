#Exercice 7 :  Décomposition d’un montant en euros Écrire un algorithme permettant
#de décomposer un montant entré au clavier en billets de 20, 10, 5 euros et pièces
#de 2, 1 euros, de façon à minimiser le nombre de billets et de pièces.

montant = int(input("saisir un montant"))
billet_20 = montant / 20
montant = montant % 20
print("la decomposition en billet de 20 euros est: ", + billet_20)
billet10 = montant / 10
montant = montant % 10
print("la decomposition en billet de 10 euros est : ", + billet10)
billet5 = montant / 5
montant = montant % 5
print("la decomposition en billet de 5 euros est : ", + billet5)
piece2 = montant / 2
montant = montant % 2
print("la decomposition en piece de 2 euros est: ", + piece2)
piece1 = montant / 1
montant = montant % 1
print("la decomposition en piece de d'1 euros est: ", + piece1)