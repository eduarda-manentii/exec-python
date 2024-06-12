# 4. Escreva um programa que armazene em um dicionário as seguintes informações:
# a. hand = mão
# b. blue = azul
# c. book = livro
# d. pen = caneta
# O programa deverá ler uma palavra em inglês, verificar se a palavra existe no
# dicionário, em caso positivo, deverá mostrar a tradução, caso contrário mostrar uma
# mensagem informando que a palavra não consta no dicionário.

dicionario = {
    'hand': 'mão',
    'blue': 'azul',
    'book': 'livro',
    'pen': 'caneta'
}

palavra = input("Digite uma palavra em ingês: ")

#if palavra in dicionario:
#    print(dicionario[palavra])
#else:
#    print("Palavra não consta no dicionário.")

palavra_encontrada = False
for i in dicionario:
    if(i == palavra):
        palavra_encontrada = True
        print(dicionario[palavra])

if(palavra_encontrada == False):
    print("Palavra não consta no dicionário.")
