# 4. Escreva um programa, com uma função para criar uma lista com valores aleatórios entre 1 e 10.
#  A função deve ter como parâmetro o tamanho da lista e retornar os valores da lista,
# o maior valor da lista e o menor valor da lista.


from random import randint

# FORMA 1
# def cria_valores_aleatorios(tamanho):
#    numeros_random = []
#    for c  in range (0, tamanho):
#        numeros_random.append(random.randint(1, 10))
#        if c == 0:
#           maior = menor = numeros_random[c]
#        maior = max(numeros_random[c], maior)
#        menor = min(numeros_random[c], menor)
#    return numeros_random, maior, menor
# print(cria_valores_aleatorios(5))

# FORMA 2
def cria_valores_aleatorios(tamanho):
    numeros_random = []
    for _ in range (tamanho):
        numeros_random.append(randint(1, 10))
    return numeros_random, max(numeros_random),  min(numeros_random)

print(cria_valores_aleatorios(5))
