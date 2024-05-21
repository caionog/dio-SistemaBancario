# O sistema possui apenas um usuário, deve realizer as operações Saque, Depósito e Extrato. Possui um limite de 3 Saques.

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.deposito = 0
        self.saque = 0
        self.extrato = []
        self.saldo = 0
        self.limite = 0

def menu():
    print("""Escolha a operação que deseja realizar:
    1 - Saque
    2 - Depósito
    3 - Extrato
    4 - Sair""")

#Criar usuário
usuario = Usuario("caio")
menu()
#Loop Principal
while True:
    opcao = input()
    
    if opcao == "1":  # Saque
        #Saque subtrai um valor menor ou igual ao saldo do usuário
        if usuario.limite < 3: 
            print("Digite o valor que deseja sacar:")
            valor_saque = int(input())
            if valor_saque > usuario.saldo:
                print("Saldo insuficiente.")
            else:
                usuario.saque = valor_saque
                usuario.extrato.append(-valor_saque)
                usuario.saldo -= valor_saque
                usuario.limite += 1
                print("Saque realizado com sucesso.")
        else:
            print("Limite diário de saques alcançado.")
    
    elif opcao == "2":  # Depósito
        #Depósito adiciona um valor maior que zero ao saldo do usuário
        print("Digite o valor que deseja depositar:")
        valor_deposito = int(input())
        usuario.deposito = valor_deposito
        usuario.extrato.append(valor_deposito)
        usuario.saldo += valor_deposito
        print("Depósito realizado com sucesso.")
    
    elif opcao == "3":  # Extrato
        #Extrato deve mostrar uma lista com todo o histórico de saques e depósitos realizados e mostrar o saldo total da conta
        print("Extrato:")
        for item in usuario.extrato:
            print(item)
        print("Saldo:", usuario.saldo)
    
    elif opcao == "4":  # Sair
        print("Obrigado por utilizar nosso sistema.")
        break
    
    else:
        print("Opção inválida.")

    menu()
