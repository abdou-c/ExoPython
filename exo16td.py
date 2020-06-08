#Exercice 16 : Faire un programme qui calcule et affiche la division de a par b par soustractions successives

val1 = int(input("saisir le dividant"))
val2 = int(input("saisir le diviseur"))
i = 0
while(val1 >= val2):
    val1 = val1 - val2
    i = i + 1
print(val2)