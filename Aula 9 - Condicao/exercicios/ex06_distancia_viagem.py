# Escreva um programa que leia a distância de uma viagem em KM. Calcule o preço
# da passagem, cobrando R$ 0,65 por KM para viagens até 250 KM e R$ 0,40 para
# viagens mais longas.
distancia_percorrida = int(input("Digite a percorrida percorrida: "))
if(distancia_percorrida <= 250):
    preco_passagem = distancia_percorrida * 0.65
else:
    preco_passagem = distancia_percorrida * 0.40
print("O carro percorreu {}Km/h e a passagem foi de {}".format(distancia_percorrida, preco_passagem))
