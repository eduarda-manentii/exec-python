# Escreva um programa que leia uma frase e mostre:
# Quantas vezes aparece a letra ‘a’
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input("Escreva uma frase: ")
texto = frase.lower()
print("Quantas vezes aparece a letra a: {} ".format(texto.count("a")))
print("Em que posição ela aparece a primeira vez: {} ".format(texto.find("a")))
print("Em que posição ela aparece a última vez: {} ".format(texto.rfind("a")))
