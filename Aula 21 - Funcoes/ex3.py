# 3. Escreva um programa com uma função chamada calcula_imposto.
# A função possui dois parâmetros: taxa_imposto, que é uma porcentagem do imposto e custo,
#  que é o custo de um item antes do imposto. A função deve retornar o valor de venda,
# ou seja, o custo mais o imposto

def calcula_imposto(taxa_imposto, custo):
    imposto = (custo * taxa_imposto) / 100
    return custo + imposto

print(calcula_imposto(10, 1000))
