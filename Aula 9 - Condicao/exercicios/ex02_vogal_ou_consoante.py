# Escreva um programa que leia uma letra e mostre se é vogal ou consoante
letra = input("Digite uma letra: ")
letra_maiuscula = letra.upper()
if(letra_maiuscula == "A"
   or letra_maiuscula == "E"
   or letra_maiuscula == "I"
   or letra_maiuscula == "O"
   or letra_maiuscula == "U"):
    print("A letra {} é vogal.".format(letra))
else:
    print("A letra {} é consoante.".format(letra))
