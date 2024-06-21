# Escreva um programa para ler um arquivo (formato texto) que contenha uma lista de endereços IP. O
# programa deverá verificar se os endereços são válidos e criar um outro arquivo com os endereços
# válidos e inválidos.

arq = open("Aula 28 - Arquivos Exercícios/enderecos.txt", encoding='utf-8')
outros = open("Aula 28 - Arquivos Exercícios/outros_enderecos.txt", "w+", encoding='utf-8')

linhas = arq.readlines()

validos = []
invalidos = []

for linha in linhas:
    it = 0
    numeros = linha.split(".")
    for numero in numeros:
        if int(numero) > 255:
            it += 1
            invalidos.append(linha)
            break
    if(it == 0):
        validos.append(linha)

outros.write("Válidos\n")
for valido in validos:
   outros.write(valido)

outros.write("Inválidos\n")
for invalido in invalidos:
   outros.write(invalido)

outros.close()
