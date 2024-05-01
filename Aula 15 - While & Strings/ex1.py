# Escreva um programa para ler uma frase e mostre a quantidade de espaços em
# branco e quantas vezes aparecem as vogais.

frase = input("Digite uma frase: ")
brancos = frase.count(" ")
print(brancos)

vogais = ["a", "e", "i", "o", "u"]
qtde_vogais = 0
for letra in frase:
    for vogal in vogais:
        if vogal == letra:
            qtde_vogais += 1
print(qtde_vogais)
