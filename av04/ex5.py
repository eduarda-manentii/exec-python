# 5. Escreva um programa, com uma função que deverá receber “n” valores e retornar a
# soma dos valores, a média, o maior e o menor valor informado


def calculos(*numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return soma, media, max(numeros), min(numeros)

soma, media, maior, menor = calculos(2, 2, 2)
print("Soma total: ", soma)
print("Media: ", media)
print("Maior número: ", maior)
print("Menor número: ", menor)
