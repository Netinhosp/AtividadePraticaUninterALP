print("Bem vindo a Transportadora do Helí Piancó - 4135277")
# Declarando variáveis global
preco_volume = 0
multiplicador_peso = 0
multiplicador_rota = 0

# Função para manipular dados sobre a dimensão do objeto
def dimensoesObjeto():
  # Laço de repetição para receber e verificar valores
  while True:
    # Tentando realizar captura de dados
    try:
      # Recebendo dados do usuário
      comprimento_obj = int(input("Digite o comprimento do objeto (em cm): "))
      largura_obj = int(input("Digite a largura do objeto (em cm): "))
      altura_obj = int(input("Digite a altura do objeto (em cm): "))
    # Tratando possíveis erros
    except:
      print("Você digitou alguma dimensão do objeto com valor não numérico")
      print("Por favor entre com as dimensões desejadas novamente")
      continue
    
    # Realizando calculo do volume do objeto
    volume = altura_obj * largura_obj * comprimento_obj
    # Chamando variável global para dentro da função
    global preco_volume
    # Imprimindo o valor do volume para o usuário
    print(f"O volume do objeto é (em cm³): {volume}")
    
    # Condicional que verifica volume do objeto e atribui seu devido preço
    if(volume < 1000):
      preco_volume = 10
    elif(volume >= 1000 and volume < 10000):
      preco_volume = 20
    elif(volume >= 10000 and volume < 30000):
      preco_volume = 30
    elif(volume >= 30000 and volume < 100000):
      preco_volume = 50
    else:
      # Imprimindo erro para o usuário
      print("Não aceitamos objetos tão grandes")
      print("Por favor entre com as dimensões desejadas novamente")
      # Retornando para o início do laço de repetição
      continue
    
    # Imprimindo preço de acorco com o volume, para o usuário
    print(f"Preço por volume é: R${preco_volume}")
    # Quebrando laço de repetição
    break

# Função para manipular dados sobre o peso do objeto
def pesoObjeto():
  # Laço de repetição para receber e verificar valores
  while True:
    # Tentando realizar captura de dados
    try:
      # Recebendo dados do usuário
      peso_obj = int(input("Digite o peso do objeto (em kg): "))
    # Tratando possíveis erros
    except:
      print("Você digitou o peso do objeto com valor não numérico")
      print("Por favor entre com o peso desejado novamente")
      continue
    
    # Imprimindo o peso do objeto para o usuário
    print(f"O peso do objeto (em kg) é: {peso_obj}")
    # Chamando variável global para dentro da função
    global multiplicador_peso

    # Condicional que verifica peso do objeto e atribui seu devido multiplicador
    if(peso_obj <= 0.1):
      multiplicador_peso = 1
    elif(peso_obj >= 0.1 and peso_obj < 1):
      multiplicador_peso = 1.5
    elif(peso_obj >= 1 and peso_obj < 10):
      multiplicador_peso = 2
    elif(peso_obj >= 10 and peso_obj < 30):
      multiplicador_peso = 3
    else:
      # Imprimindo erro para o usuário
      print("Não aceitamos objetos tão pesados!")
      print("Por favor entre com o peso desejado novamente")
      # Retornando para o início do laço de repetição
      continue
    
    # Imprimindo multiplicador de acorco com o peso do objeto, para o usuário
    print(f"O multiplicador de acordo com o peso do objeto é: {multiplicador_peso}")
    # Quebrando laço de repetição
    break

# Função para manipular dados sobre a rota do objeto
def rotaObjeto():
  # Laço de repetição para receber e verificar valores
  while True:
    # Recebendo dados do usuário
    rota_obj = input("Selecione a rota: \n AR - De Arcoverde para Recife \n AC - De Arcoverde para Caruaru"
                    + "\n CA - De Caruaru para Arcoverde \n CR - De Caruaru para Recife"
                    + "\n RC - De Recife para Caruaru \n RA - De Recife para Arcoverde \n")
    
    # Chamando variável global para dentro da função
    global multiplicador_rota
    
    # Condicional que verifica rota do objeto e atribui seu devido multiplicador
    if(rota_obj == "RC"):
      multiplicador_rota = 1
    elif(rota_obj == "CR"):
      multiplicador_rota = 1
    elif(rota_obj == "AC"):
      multiplicador_rota = 1.2
    elif(rota_obj == "CA"):
      multiplicador_rota = 1.2
    elif(rota_obj == "RA"):
      multiplicador_rota = 1.5
    elif(rota_obj == "AR"):
      multiplicador_rota = 1.5
    else:
      # Imprimindo erro para o usuário
      print("Você digitou uma rota inexistente")
      print("Por favor entre com a rota desejada novamente")
      # Retornando para o início do laço de repetição
      continue
    
    # Imprimindo multiplicador de acorco com a rota do objeto, para o usuário
    print(f"O multiplicador de acordo com o rota do objeto é: {multiplicador_rota}")
    # Quebrando laço de repetição
    break

# Função para calcular valor final do transporte
def precoTranporte():
  # Chamando variáveis global para dentro da função
  global preco_volume
  global multiplicador_peso
  global multiplicador_rota
  # Calculando valor final do transporte
  valor_final = preco_volume * multiplicador_peso * multiplicador_rota
  # Imprimindo valor final do transporte para o usuário
  print(f"Total a pagar(R$): {valor_final}")

# Chamando funções para serem executadas
dimensoesObjeto()
pesoObjeto()
rotaObjeto()
precoTranporte()