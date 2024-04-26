# A série de Fibonacci é formada pela sequência
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# escreva um programa que mostre os 20 primeiros termos da série.

n1 = 0
n2 = 1
for c in range (0, 21):
    print(n1)
    print(n2)
    n1 = n1 + n2
    n2 = n1 + n2
