#  Escreva um programa que leia um ano qualquer e mostre se ele é bissexto.

# Se o ano não termina em 00, ele é bissexto caso seja divisível por 4.
# Exemplos: 1988, 1992, 1996, 2004, e assim por diante.
# Nota: Um número é divisível por 4 se a sua dezena (1988 = 88) é divisível por 4.
ano = input("Digite o ano: ")
ano_nao_bissexto = ano.endswith("00")
bissexto = int(ano) % 4 == 0
if(ano_nao_bissexto == False and bissexto == True):
    print("O ano de {} é bissexto.".format(ano))
else:
    print("O ano de {} não é bissexto.".format(ano))
