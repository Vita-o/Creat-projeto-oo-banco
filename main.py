from banco import banco

banco = banco("banco.db")
while True:
  print("""
  1 - CRIAR CONTA
  2 - CONSULTAR CONTA
  3 - DEPOSITAR
  4 - SACAR
  5 - Deletar Conta
  0 - SAIR
  """)
  opcao = int(input("DIGITE a OPÇÃO: "))
  if opcao == 1:
    nome = str(input("Informr o nome: "))
    saldo = float(input("informe o Saldo: "))
    id_conta = banco.criar_conta(nome,saldo)
    print(f"Conta criada com Sucesso!! O numero da sua conta é: {id_conta}")

  
  elif opcao == 2:
    try:
      id_conta = input("Informe o numero da Conta: ")
      conta = banco.buscar_conta(id_conta)
      if conta:
        print(f"Saldo da conta {conta.titular}: R$ {conta.saldo}")
      else:
        print("Conta Inexistente.")
    except:
      print("ERRO. Digite o Numero da Conta")      
  elif opcao == 3:
    try:
      id_conta = input("Informe o numero da conta: ")
      valor = float(input("Informe o vslor do deposito: "))
      banco.depositar(id_conta, valor)
      print ("Deposito realizado com sucesso!!")
    except:
      print("ERRO. Digite Somente Numeros!!")
  
  elif opcao == 4:
    try:
      id_conta = input("Informe o numero da conta: ")
      valor = float(input("Informe o vslor do deposito: "))
      banco.sacar(id_conta, valor)
      print ("Sauqe realizado com sucesso!!")
    except:
      print("ERRO. Digite Somente Numeros")

  elif opcao == 5:
    try:
      id_conta = input("Informe o numero da conta: ")
      banco.deletar(id_conta)
      print("Conta Deletada com Sucesso!!")
    except:
      print("ERRO. Digite um Numero.")
  elif opcao == 0:
    print("Obigado por usar esse sistema!!")
    break