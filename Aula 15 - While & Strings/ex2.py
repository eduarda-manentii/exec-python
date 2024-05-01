# Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da
# direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos.
# Escreva um programa que leia uma sequência de caracteres e diga se é um
# palíndromo ou não.

palavra = input("Digite uma palavra: ")
arvalap = ""
for c in range (len(palavra), 0, -1):
    arvalap += palavra[c - 1]

if arvalap == palavra:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
