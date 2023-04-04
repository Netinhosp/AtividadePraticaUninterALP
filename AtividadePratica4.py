print("Bem vindo ao Controle de Estoque da Bicicletaria do Helí Piancó")

# Criando lista, que irá armazenar o estoque de peças
estoque_pecas = []
# Contador, para gerar códigos unicos para cada item
index = 1

# Função que exibe menus
def menu():
  #Laço de retição para o programa nunca parar, antes que o usuário deseje sair
  while True:
    #Imprimindo opções do menu na tela
    print("Escolha a opção desejada:")
    print("1-Cadastrar Peças")
    print("2-Consultar Peças")
    print("3-Remover Peças")
    print("4-Sair")

    # Recebendo opção que o usuário escolheu
    opcao = int(input())

    # Condicional para interpretar opção do usuário
    if(opcao == 1):
      print("Você selecionou a opção Cadastrar Peça")
      cadastrarPeca(index)
    elif(opcao == 2):
      print("Você selecionou a opção Consultar Peça")
      consultarPeca()
    elif(opcao == 3):
      print("Você selecionou a opção Remover Peça")
      removerPeca()
    elif(opcao == 4):
      print("Você selecionou a opção Sair")
      break
    else:
      print("Opção inválida - Escolha novamente")
      continue

# Função que cadastra peça
def cadastrarPeca(codigo):
  # Chamando variáveis global
  global estoque_pecas
  global index

  print(f"Código da Peça: {codigo}")

  # Tratando possíveis erros
  try:
    # Recebendo dados do usuário, sobre a peça cadastrada
    nome_peca = input("Digite o nome da peça: ")
    fabricamte_peca = input("Digite o fabricante da peça: ")
    preco_peca = float(input("Digite o valor da peça: "))
  except:
    print("Por favor digitar um valor numérico no preço preço do produto")
    menu()
  
  # Criando um dicionário, com os dados fornecidos pelo usuário
  nova_peca = {"código": codigo,
               "nome": nome_peca,
               "fabricante": fabricamte_peca,
               "Preço": preco_peca,}

  # Adicionando o dicionário a uma lista
  estoque_pecas.append(nova_peca)

  # Acrecentando '+ 1' ao contador
  codigo += 1
  index = codigo

  # Chamando função menu
  menu()

# Função que consulta peças em estoque
def consultarPeca():
  # Laço de repetição que navega no menu de consultas
  while True:
    # Imprimindo opções para o usuário
    print("Escolha a opção desejada:")
    print("1-Consultar Todas as Peças")
    print("2-Consultar Peças por Código")
    print("3-Consultar Peças por Fabricante")
    print("4-Retornar")

    # Recebendo dados sobre a opção do usuário
    opcao = int(input())

    # Condicional para interpretar opção do usuário
    if(opcao == 1):
      if(estoque_pecas == []):
        # Se o estoque estiver vazio, restornar uma mensagem para o usuário
        print("Ainda não há nenhuma peça cadastrada!")
      else:
        # Laço de repetição, para imprimir todas as peças contidas em estoque
        for pecas in estoque_pecas:
          print("-------------------")
          for chave, valor in pecas.items():
            print(f"{chave}: {valor} \n")
      menu()
    elif(opcao == 2):
      consultaPorCod()
    elif(opcao == 3):
      consultaPorFab()
    elif(opcao == 4):
      menu()
    else:
      print("Opção inválida - Escolha novamente")
      continue

# Função que realiza uma consulta de peças, por código
def consultaPorCod():
  # Tratando possíveis erros
  try:
    # Recebendo dados do usuário
    codigo = int(input("Digite o Código da Peça: "))
  except:
    print("Por favor, digitar apenas valores numéricos")

  # Declarando variável
  pecaCod = ""

  # Laço de repetição para imprir a peça de acorco com o código
  for cod in estoque_pecas:
    if(cod["código"] == codigo):
      pecaCod = cod
      for chave, valor in pecaCod.items():
        print(f"{chave}: {valor} \n")
  
  # Se não encontrar a peça com o código digitado, devolver uma mensagem
  if(pecaCod == ""):
    print(f"Nenhuma peça foi encontrada contendo esse código: {codigo}")
  
  # Chamando função do menu ao final da exução dessa função
  menu()

# Função que gera uma consulta pelo nome do fabricante
def consultaPorFab():
  # Recebendo dados
  fabricante = input("Digite o Fabricante da Peça: ")
  # Declarando variável
  pecaPorFabricantes = ""

  # Laço de repetição que verifica a peça com o fabricante desejado
  for estoque in estoque_pecas:
    if(estoque["fabricante"] == fabricante):
      pecaPorFabricantes = estoque
      for chave, valor in pecaPorFabricantes.items():
        print(f"{chave}: {valor} \n")

  # Caso não tenha nenhuma peça do fabricante, exibir mensagem ao usuário
  if(pecaPorFabricantes == ""):
    print(f"Nenhuma peça desse fabricante foi encontrada: {fabricante}") 
  menu()

# Função que remove peças da lista, pelo código
def removerPeca():
  agua = "agua"
  # Tratando possíveis erros
  try:
    # Recebendo dados do usuário
    cod_remover = int(input("Digite o código da peça a ser removido: "))
  except:
    print("Por favor, digitar apenas valores numéricos")

  # Declarando variável, que é uma contador.
  index = 0

  # Laço de repetição que verifica código da peça
  for cod in estoque_pecas:
    if(cod["código"] == cod_remover):
      del estoque_pecas[index]
      break
    index += 1

menu()