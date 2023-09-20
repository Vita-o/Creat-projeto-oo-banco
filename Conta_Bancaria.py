import datetime

class Conta:

  def __init__(self, numero_conta, titular, saldo):
    self.numero_conta = numero_conta
    self.titular = titular
    self.saldo = saldo
    # self.movimentacao = list()

  def deposito_valido(self, novo_valor):
    if novo_valor > 0:
      self.saldo += novo_valor
      # self.add_movimentacao("Saque", valor,)
      return True
    return False

  def saque_valido(self,valor):
    if self.saldo >= valor:
      self.saldo -= valor 
      # self.add_movimentacao("Saque", valorr,)
      return True
    return False
  
  # def add_movimentacao(self, acao, valor):
  #     data = datetime.datetime.now()
  #     data = data.strftime("%x")
  #     movimentacao = f"{acao} no valor de R${valor} na data {data}"
  #     self.movimentacao.append(movimentacão)
  def extrato(self):
    print("------------- Extraçao -------------")
    print(f"Conta: {self.numero_conta}\n titular:{self.titular}")
    for movimentacao in self.movimentacao:
      print(movimentacao)
    print(f"-------------------- Saldo {self.saldo}")
    