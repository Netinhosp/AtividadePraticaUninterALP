print("Bem vindo a Lanchonete do Helí Piancó")

# Imprimindo o cardápio para o usuário
print("- - - - - - - - - Cardápio - - - - - - - - - ")
print("Cachorro-Quente       - R$9,00  - código: 100")
print("Cachorro-Quente Duplo - R$11,00 - código: 101")
print("X-Egg                 - R$12,00 - código: 102")
print("X-Salada              - R$13,00 - código: 103")
print("X-Bacon               - R$14,00 - código: 104")
print("X-Tudo                - R$17,00 - código: 105")
print("Refrigerante Lata     - R$5,00  - código: 200")
print("Chá Gelado            - R$4,00  - código: 201")
print("- - - - - - - - - - - - - - - - - - - - - - -")

# Criando lista e variável para guarda os valores dos pedidos.
lista_lanches = []
valor_total = 0
index = 0

# Laço de repetição que permite o cliente escolher quantos itens desejar.
while True:
  # Recebendo código do item, que o usuário escolheu.
  cod_lanche = float(input("\nDigite o código do seu item: "))
  valor_lanche = 0
  # Verificando qual código o usuário escolheu, para saber retornar o preço e nome do item.
  if(cod_lanche == 100):
    lista_lanches.append("Cachorro-Quente")
    valor_lanche += 9
  elif(cod_lanche == 101):
    lista_lanches.append("Cachorro-Quente Duplo")
    valor_lanche += 11
  elif(cod_lanche == 102):
    lista_lanches.append("X-Egg")
    valor_lanche += 12
  elif(cod_lanche == 103):
    lista_lanches.append("X-Salada")
    valor_lanche += 13
  elif(cod_lanche == 104):
    lista_lanches.append("X-Bacon")
    valor_lanche += 14
  elif(cod_lanche == 105):
    lista_lanches.append("X-Tudo")
    valor_lanche += 17
  elif(cod_lanche == 200):
    lista_lanches.append("Refrigerante Lata")
    valor_lanche += 5
  elif(cod_lanche == 201):
    lista_lanches.append("Chá Gelado")
    valor_lanche += 4
  # Caso a opção que o usuário digitou, seja inválida, irá retornar para o início do laço de repetição.
  else:
    print("Opção inválida")
    continue
  
  # Imprimindo na tela, itens escolhidos e valor.
  print(f"Você pediu um {lista_lanches[index]} no valor de {valor_lanche:.2f}")
  # Incrementando +1 toda vez que realizar o laço, para percorrer a lista
  index += 1
  # Guardando o valor do pedido na variável TOTAL.
  valor_total += valor_lanche

  # Perguntando ao usuário, se ele deseja incluir mais algo na lista.
  novo_item = int(input("\nDeseja incluir mais algum item? \n1 - Sim \n0 - Não\n"))

  # Condicional, que verifica a resposta do usuário.
  if(novo_item == 1):
    continue
  elif(novo_item == 0):
    break
  else:
    print("\nOpção inválida - Digite seus itens novamente!")
    # Zerando as variáveis, caso precise começar o pedido de novo.
    lista_lanches = []
    valor_total = 0
    index = 0
    continue

# Imprimindo na tela valor TOTAL do pedido.
print(f"\nValor total do seu pedido R${valor_total:.2f}")
print("\nObrigado pela preferência, volte sempre.")