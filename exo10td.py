#Exercice 10 : Ecrire un algorithme qui lit trois valeurs entières ( A, B et C)
# et qui permet de les trier par échanges successifs
#  Et enfin les afficher dans l'ordre.


A = int(input("saisir la valeur de A"))
B = int(input("saisir la valeur de B"))
C = int(input("saisir la valeur de B"))
if(A<B and B<C):
    print("l'ordre des valeurs est : ", A, B, C)
elif(A<C and C<B):
    print("l'ordre des valeurs est : ", A, C, B)
elif(B<A and A<C):
    print("l'ordre des valeurs est : ", B, A, C)
elif(B<C and C<A):
    print("l'ordre des valeurs est : ", B, C, A)
elif(C<A and A<B):
    print("l'ordre des valeurs est : ", C, A, B)
elif(C<B and B<A):
    print("l'ordre des valeurs est : ", C, B, A)
else:
    print("veuillez saisir des valeurs qui ne sont pas égales")





