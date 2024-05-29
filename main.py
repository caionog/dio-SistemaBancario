from datetime import datetime
# O sistema possui apenas um usuário, deve realizer as operações Saque, Depósito e Extrato. Possui um limite de 3 Saques.

class Usuario:
    def __init__(self, nome, nascimento, cpf, endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.deposito = 0
        self.saque = 0
        self.extrato = []
        self.saldo = 0
        self.limite = 0

class ContaCorrente:
    def __init__(self,conta,usuario):
        self.agencia = '0001'
        self.conta = conta
        self.usuario = usuario
#Lista para armazenar os usuários e contas correntes
listaUsuarios = []
listaContasCorrente = []
def menu():
    print("""Escolha a operação que deseja realizar:
    1 - Saque
    2 - Depósito
    3 - Extrato
    4 - Sair
    5 - Criar usuário
    6 - Listar usuários
    7 - Criar Conta""")

#Sacar
#Saque subtrai um valor menor ou igual ao saldo do usuário
def saque(usuario):
    if usuario.limite < 3:
        print("Digite o valor que deseja sacar:")

        valor_saque = int(input())
        if valor_saque > usuario.saldo:
            print("Saldo insuficiente")
        else:
            usuario.saque = valor_saque
            usuario.extrato.append(-valor_saque)
            usuario.saldo -= valor_saque
            usuario.limite += 1
            print("Saque realizado com sucesso.")
            menu()

    else:
        print("Limite diário alcançado")
        menu()

#Depositar
#Depósito adiciona um valor maior que zero ao saldo do usuário
def deposito(usuario):
    print("Digite o valor que deseja depositar:")
    valor_deposito = int(input())
    usuario.deposito = valor_deposito
    usuario.extrato.append(valor_deposito)
    usuario.saldo += valor_deposito
    print("Depósito realizado com sucesso.")
    menu()

#Ver extrato
#Extrato deve mostrar uma lista com todo o histórico de saques e depósitos realizados e mostrar o saldo total da conta
def extrato(usuario):
        print("Extrato:")
        for item in usuario.extrato:
            print(item)
        print("Saldo:", usuario.saldo)

#Criar novo usuário
#Deve receber input para criar um novo usuário
def criarUsuario():
    print("\nDigite o seu nome:")
    criarNome = input()

    while True:
        try:
            print("\nDigite seu CPF (apenas números):")
            criarCPF = int(input())
            #Verifica se CPF possui 11 dígitos
            if len(str(criarCPF)) != 11:
                print("CPF inválido. Digite apenas 11 números.")
            else:
                break
        except ValueError:
            print("CPF inválido. Digite apenas números.")

    while True:
        while True:
            print("\nDigite sua data de nascimento (formato: DD/MM/AAAA):")
            criarNascimento = input()
            try:
                # Tenta converter a string de data de nascimento em um objeto datetime
                data_nascimento = datetime.strptime(criarNascimento, '%d/%m/%Y')
                break
            except ValueError:
                # Se ocorrer um ValueError, a data não está no formato correto
                print("Data de nascimento inválida. Digite no formato DD/MM/AAAA.")

        # Se a data de nascimento estiver no formato correto, saia do loop
        if 'data_nascimento' in locals():
            break
 

    print("\nDigite seu endereço:")
    criarEndereco = input()

    usuario2 = Usuario(criarNome, criarNascimento, criarCPF, criarEndereco)
    listaUsuarios.append(usuario2)
    menu()
    return usuario2
#Listar usuarios
def listarUsuarios():
    print("\nRetornar todos usuarios")
    for usuario in listaUsuarios:
        print(usuario.nome)
#Filtrar lista de usuarios por cpf
def filtrarConta(cpfFornecido):
    return next((u for u in listaUsuarios if u.cpf == cpfFornecido), None)

#Criar conta
def criarConta():
    cpf = input("\nDigite o CPF do usuário para quem deseja criar uma conta. Digite no formato XXX.XXX.XXX-XX")
    #Verifica se o CPF informado está em listaUsuarios
    usuario = filtrarConta(cpf)
    if usuario:
        #Cria conta baseado no CPF informado
        numero_conta = len(listaContasCorrente) + 1
        conta = ContaCorrente(numero_conta,cpf)
        listaContasCorrente.append(conta)
        print(f"\nSua conta foi criada Número da conta: {numero_conta}, Agência: {conta.agencia})")
    else:
        print("\nNão foi possível criar a conta")
            

#Teste
usuario = Usuario("caio", "03/08/1998","111.111.111-2", "Rua imaginaria")
listaUsuarios.append(usuario)

#Loop Principal (MAIN)
def main():
    menu()
    while True:
       opcao = input()  
       if opcao == "1":  # Saque
          saque(usuario)
       elif opcao == "2":  # Depósito
            deposito(usuario)
       elif opcao == "3":  # Extrato
             extrato(usuario)
       elif opcao == "4":  # Sair
             print("Obrigado por utilizar nosso sistema.")
             break 
       elif opcao =="5": # Criar usuário
           criarUsuario()
       elif opcao =="6": #listar usuários
           listarUsuarios()
       elif opcao == "7": #Criar conta
           criarConta()
       else:
              print("Opção inválida.")
    menu()

#Execução do código    
main()