# 1. Escreva um programa, com uma função que necessite de três argumentos,
# e retorne a soma desses argumentos.

def soma(a: int, b: int, c: int = 0):
    soma = a + b + c
    return soma

# outra forma
#    def soma(*numeros):
#        soma = 0
#        for numero in                                                                                                                      numeros:
#            soma += numero
#        return soma

numero1 = int(input("Digite o número 1: "))
numero2 = int(input("Digite o número 2: "))
numero3 = int(input("Digite o número 3: "))
print(soma(numero1, numero2, numero3))
