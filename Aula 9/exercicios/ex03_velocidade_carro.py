# Escreva um programa que leia a velocidade de um carro. Se a velocidade for maior
# que 100 Km/h, mostre uma mensagem dizendo que ele foi multado. Mostre também
# o valor da multa, R$ 8,00 para cada KM acima do limite.
velocidade_atual = int(input("Velocidade do carro: "))
velocidade_permitida = 100
if(velocidade_atual > velocidade_permitida):
    velocidade_acima = velocidade_atual - velocidade_permitida
    preco_multa = 8.00
    total_multa = velocidade_acima * preco_multa
    print("Sua velocidade de {} é superior a 100km/h. ".format(velocidade_atual) +
        "Você foi multado no valor de R${}".format(total_multa))
else:
    print("Sua velocidade de está dentro do permitido")
