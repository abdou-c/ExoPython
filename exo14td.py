#Exercice 14 : Faire un programme qui saisit une date (jour, mois et année) at qui indique si l’année est bissextile

jour = int(input("saisir le jour"))
mois= int(input("saisir le mois"))
annee= int(input("saisir l'année"))
annee_ref = 2020
if (jour < 31 or jour > 0 or mois <= 12 or mois > 0 or annee > 1 or annee <= annee_ref or mois == 2 and jour <= 29 or annee % 4 == 0 or mois == 2 or jour <= 29 or jour > 28):
    print("l'année est bissextile")
else:
    print("l'année n'est pas bissextile")