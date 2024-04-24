# Escreva um programa que leia os preços de três produtos e informe qual você deve
# comprar. A decisão é sempre pelo mais barato.
produto1 = float(input("Digite o valor do produto A: "))
produto2 = float(input("Digite o valor do produto B: "))
produto3 = float(input("Digite o valor do produto C: "))

print("O valor do produto que você deve comprar é de R${}".format(min(produto1, produto2, produto3)))
