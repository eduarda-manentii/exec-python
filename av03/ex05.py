# O cardápio de uma lanchonete é o seguinte:
# o	Especificação    Código     Preço
# o	Cachorro-Quente  102      R$ 12,80
# o	Hambúrguer          103      R$ 26.50
# o	X-burguer              104      R$ 21,10
# o	Refrigerante          105      R$ 3,00
# Escreva um programa que leia a quantidade de itens do pedido
# o código dos itens pedidos e as quantidades desejadas.
# Mostre o valor a ser pago pelo pedido.

cod_cachorro = 102
preco_cachorro = 12.80

cod_hamburguer = 103
preco_hamburguer = 26.50

cod_xburguer = 104
preco_xburguer = 21.10

cod_refrigerante = 105
preco_refrigerante = 3.00

valor_total = 0

qtde_itens = int(input("Qual a quantidade de itens? "))
if(qtde_itens <= 4):
   for c in range (0, qtde_itens):
      cod_item = int(input("Qual o código do item? "))
      qtde_item = int(input("Qual a quantidade do item? "))
      if(cod_item == cod_cachorro):
         valor_total += preco_cachorro * qtde_item
      else:
         if(cod_item == cod_hamburguer):
            valor_total += preco_hamburguer * qtde_item
         else:
            if(cod_item == cod_xburguer):
               valor_total += preco_xburguer * qtde_item
            else:
               if(cod_item == cod_refrigerante):
                  valor_total += preco_refrigerante * qtde_item
   print("O valor a ser pago é de {}.".format(valor_total))
else:
   print("A quantidade máxima de itens é 4.")
