#  Escreva um programa que leia um ano qualquer e mostre se ele é bissexto.

# Se o ano não termina em 00, ele é bissexto caso seja divisível por 4.
# Exemplos: 1988, 1992, 1996, 2004, e assim por diante.
# Nota: Um número é divisível por 4 se a sua dezena (1988 = 88) é divisível por 4.

ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano  % 100 != 0) or ano % 400 == 0:
    print("O ano de {} é bissexto.".format(ano))
else:
    print("O ano de {} não é bissexto.".format(ano))
