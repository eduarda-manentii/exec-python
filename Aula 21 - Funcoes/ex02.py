# 2.  Escreva um programa, com uma função que necessite de um argumento.
# A função deve retornar ‘P’, se o argumento for positivo, e ‘N’, se o argumento for zero ou negativo

def verifica_sinal(numero: int):
    if(numero > 0):
        sinal = 'P'
    else:
        sinal = 'N'
    return sinal

print(verifica_sinal(-5))
