#Exercice 9 : Ecrire un algorithme qui donne la durée de vol en heure minute connaissant l'heure de départ et l'heure d'arrivée.
#a. On considère que le départ et l'arrivé ont lieu le même jour
#b. On suppose que la durée de vol est inférieure à 24 heures mais peut avoir lieu le lendemain

hd = int(input("saisir l'heure de depart"))
md = int(input("saisir les minutes de depart"))
ha = int(input("saisir l'heure d'arrivée"))
ma = int(input("saisir les minutes d'arrivée"))

#conversion de l'heure en minute
md = md + hd * 60
ma = ma + ha * 60

#calcul de la durée de vol
dv = ma - md
dh = dv / 60
dm = dv % 60
print("la durée de vol en heure est :", + dh)
print("la durée de vol en minute est :", + dm)

