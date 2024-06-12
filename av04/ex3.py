# 3. Escreva um programa para ler o nome completo de uma pessoa e chame uma
# função para imprimir os caracteres ímpares do nome.

caracteres_impares = []
def imprime_caracteres_impares(nome):
    for i in  range (0, len(nome)):
        resto = i % 2
        if(resto > 0):
            caracteres_impares.append(nome[i])
    return caracteres_impares


nome_completo = input("Digite o nome completo: ")
print(imprime_caracteres_impares(nome_completo))
