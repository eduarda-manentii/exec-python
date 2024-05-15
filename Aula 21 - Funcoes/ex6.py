#6.	Escreva um programa, com uma função que tem como parâmetro uma lista.
# O programa deve chamar a função passando uma lista com números inteiros
# e retornar os dobro de cada um dos números .

def retorna_dobro(lista_numeros):
    lista_dobro = []
    for numero in lista_numeros:
       lista_dobro.append(numero * 2)
    return lista_dobro

lista = [0, 1, 2, 3]
print(retorna_dobro(lista))
