#Exercice 2
#Ecrire un programme qui demande à l’utilisateur de donner le rayon d’un cercle et
#lui retourne sa surface et son périmètre.

rayon = float(input("saisir le rayon"))
pi = 3.14
surface = float(rayon * rayon * pi)
perimetre = float(2 * rayon * pi)
print("la surface est : ", + surface)
print("le perimetre est :", + perimetre)


