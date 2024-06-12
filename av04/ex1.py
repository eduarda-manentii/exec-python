# 1. Escreva um programa que leia uma frase qualquer e chame uma função para contar
# e mostrar o número de vogais e espaços da frase.

vogais = ["a", "e", "i", "o", "u"]

def conta_caracteres(frase):
    qtde_vogais = 0
    espacos = frase.count(" ")

    for letra in frase.lower():
        for vogal in vogais:
            if vogal == letra:
                qtde_vogais += 1

    return qtde_vogais, espacos

frase = input("Digite uma frase: ")
vogais, espacos = conta_caracteres(frase)
print("Quantidade de vogais: ", vogais)
print("Quantidade de espaços em branco: ", espacos)

#OUTRA FORMA
# for letra in frase.lower():
#        if letra in vogais:
#            qtde_vogais += 1
