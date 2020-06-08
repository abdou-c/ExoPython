#Exercice 3 :
#Version 1 :
#Faire un programme qui saisit 3 résistances : R1, R2 et R3.
#Calculer et afficher la résistance en série : R1 + R2 +R3
#Calculer et afficher la résistance en parallèle : (R1 * R2 * R3) / (R1*R2 + R2*R3 + R1*R3)
#Version 2 :
#Demander à l’utilisateur d’indiquer son choix.
#S’il entre la valeur 1, calculer et afficher la fréquence en série.
#S’il entre la valeur 2, calculer et afficher la fréquence en parallèle.

R1 = float(input("saisir la première résistance"))
R2 = float(input("saisir la deuxième résistance"))
R3 = float(input("saisir la troisième résistance"))

res_serie = R1 + R2 + R3
print("la résistance en série est : ", + res_serie)
#resistance en parallele
res_paral = (R1 * R2 * R3) / (R1*R2 + R2*R3 + R1*R3)
print("la résistance en parallèle est : ", res_paral)

#version2
choix = int(input("faites votre choix"))
freq_serie = (R1/res_serie + R2/res_serie + R3/res_serie)/ res_serie
freq_paral = (R1/res_paral + R2/res_paral + R3/res_paral)/res_paral
if (choix == 1):
    print(freq_serie)

elif(choix == 2):
    print(freq_paral)

else:
    print("votre choix n'est pas valide")

