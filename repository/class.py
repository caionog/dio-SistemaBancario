from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, endereco, conta):
        self._endereco = endereco
        self._conta = []
    @property
    def realizar_transacao(self, conta, transacao):
        None
    
    def adicionar_conta(self, conta):
        self._conta.append(conta)

class PessoaFisica:
    def __init__(self, nome, cpf, data_nascimento):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento

class Historico:
    def __init__(self):
        self._transacoes = []
    @property
    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

class Conta:
    def __init__(self, saldo, cliente, numero):
        self.cliente = cliente
        self.saldo = 0.0
        self.numero = numero
        self.agencia = '0001'
        self.historico = Historico()



    @property
    def realziar_transacao(conta,transacao):
        None
    def adicionar_conta(conta):
        None

class ContaCorrente:
    def __init__(self, limite, limite_saque):
        self._limite = '0'
        self._limite_saques = '0'