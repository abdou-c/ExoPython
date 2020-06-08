#Exercice11: Ecrire un algorithme calculatrice permettant la
#saisie du premier entier(a) de l'opération (+ ou – ou * ou /: sont des caractères) \'
# et du deuxième entier(b) et qui affiche le résultat.

nbr1 = int(input("saisr le premier nombre"))
opr = str(input("saisir l'operateur"))
nbr2 = int(input("saisir leu deuxieme nombre"))
if(opr == "+"):
    resultat = nbr1 + nbr2
    print("le resulta est :", + resultat)

elif(opr == "-"):
    resultat = nbr1 - nbr2
    print("le resulta est :", + resultat)

elif(opr == "*"):
    resultat = nbr1 * nbr2
    print("le resulta est :", + resultat)

elif(opr == "/"):
    resultat = float(nbr1 / nbr2)
    print("le resulta est :", + resultat)
