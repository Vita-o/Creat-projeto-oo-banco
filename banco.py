import sqlite3
from Conta_Bancaria import Conta

class banco:

  def __init__(self, nome_arquivo):
    self.conexao = sqlite3.connect(nome_arquivo)
    self.criar_tabela()

  def criar_tabela(self):
    cursor = self.conexao.cursor()
    cursor.execute(
      """
      CREATE TABLE IF NOT EXISTS contas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        saldo REAL NOT NULL
      )
      """
    )
    self.conexao.commit()

  def criar_conta(self, nome, saldo=0.0):
    cursor = self.conexao.cursor()
    cursor.execute(
      """
      INSERT INTO contas (nome, saldo) VALUES (?,?)
      """, (nome, saldo)
    )
    self.conexao.commit()
    return cursor.lastrowid

  def buscar_conta(self, id_conta):
    cursor = self.conexao.cursor()
    conta = cursor.execute(
      """
      SELECT id, nome, saldo FROM contas WHERE id = ?
      """,(id_conta)
    )
    dados = cursor.fetchone()
    if dados:
      id, nome, saldo = dados
      return Conta(id, nome, saldo)
    return None

  def depositar(self, id_conta, valor):
    conta = self.buscar_conta(id_conta)
    if conta:
      if conta.deposito_valido(valor):
        cursor = self.conexao.cursor()
        cursor.execute(
          """
          UPDATE contas SET saldo = ? WHERE id = ?
          """, (conta.saldo, conta.numero_conta)
        )
        self.conexao.commit()

  def sacar(self, id_conta, valor):
    conta = self.buscar_conta(id_conta)
    if conta:
      if conta.saque_valido(valor):
        cursor = self.conexao.cursor()
        cursor.execute(
          """
          UPDATE contas SET saldo = ? WHERE id = ?
          """, (conta.saldo, conta.numero_conta)
        )
        self.conexao.commit()
  def deletar(self, id_conta):
    cursor = self.conexao.cursor()
    cursor.execute(
      """
      DELETE FROM contas
    WHERE id = ?   
      """,(id_conta)
    )