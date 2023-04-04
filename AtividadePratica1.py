print("Bem vindo a Loja do Helí Piancó")

# Estou imprimindo a descrição dos descontos
print("Promoção - Show dos descontos")
print("Em compras com quantidade até 9 produtos, o deconto é de 0%")
print("Em compras com quantidade entre 10 e 99 produtos, o desconto é de 5%")
print("Em compras com quantidade entre 100 e 999 produtos, o desconto é de 10%")
print("Em compras com quantidade acima de 1000 produtos, o desconto é de 15%")

# Recebendo valores do usuário (Valor do produto e quantidade)
valor_produto = float(input("Digite o valor do produto: "))
quantidade_produto = int(input("Digite a quantidade de produtos: "))

# Mostrando ao usuário o valor da compra, sem desconto.
preco_sem_desconto = valor_produto * quantidade_produto
print(f"O valor da sua compra sem desconto, é: R${preco_sem_desconto:.2f}")

# Condicional que define o valor do desconto, de acordo com a quantidade a ser comprada.
if(quantidade_produto < 10):
  #Se for menos de 10 itens, não tem desconto.
  preco_com_desconto = preco_sem_desconto - (preco_sem_desconto * 0)
  print(f"O valor da sua compra com o desconto de 0%, é: R${preco_com_desconto:.2f}")
elif(quantidade_produto >= 10 and quantidade_produto <= 99):
  #Se for entre 10 e 99 itens, ganhará um desconto de 5%.
  preco_com_desconto = preco_sem_desconto - (preco_sem_desconto * 0.05)
  print(f"O valor da sua compra com o desconto de 5%, é: R${preco_com_desconto:.2f}")
elif(quantidade_produto >= 100 and quantidade_produto <= 999):
  #Se for entre 100 e 999 itens, ganhará um desconto de 10%.
  preco_com_desconto = preco_sem_desconto - (preco_sem_desconto * 0.10)
  print(f"O valor da sua compra com o desconto de 10%, é: R${preco_com_desconto:.2f}")
else:
  #Se não for nenhuma das opções acima, que será mais de 1000 itens, ganhará um desconto de 15%.
  preco_com_desconto = preco_sem_desconto - (preco_sem_desconto * 0.15)
  print(f"O valor da sua compra com o desconto de 15%, é: R${preco_com_desconto:.2f}")