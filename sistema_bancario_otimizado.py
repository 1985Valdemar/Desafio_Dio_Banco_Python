import textwrap

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0
        self.limite = 500
        self.limite_saques = 3

def menu():
    menu_text = """\n
    Bem Vindo(a) Banco Tabajara
=============== MENU ================
[1]\tDepositar
[2]\tSacar
[3]\tExtrato
[4]\tNova conta
[5]\tListar contas
[6]\tNovo usuário
[0]\tSair
=====================================
=> """
    
    return input(textwrap.dedent(menu_text))

def depositar(conta, valor):
    if valor > 0:
        conta.saldo += valor
        conta.extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n*** Operação falhou! O valor informado é inválido. ***")

def sacar(conta, valor):
    excedeu_saldo = valor > conta.saldo
    excedeu_limite = valor > conta.limite
    excedeu_saques = conta.numero_saques >= conta.limite_saques

    if excedeu_saldo or excedeu_limite or excedeu_saques:
        print("\n*** Operação falhou! Verifique seu saldo, limite ou o número de saques. ***")

    elif valor > 0:
        conta.saldo -= valor
        conta.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        conta.numero_saques += 1
        print("\n$$$ Saque realizado com sucesso! $$$")

    else:
        print("\n*** Operação falhou! O valor informado é inválido. ***")

def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta.extrato else conta.extrato)
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente número): ")
    if not filtrar_usuario(cpf, usuarios):
        nome = input("Informe o seu nome completo: ")
        data_nascimento = input("Informe a data do seu nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("=== Usuário criado com sucesso! ===")
    else:
        print("\n*** Parece que já existe usuário com esse CPF! ***")
    
def filtrar_usuario(cpf, usuarios):
    cpf_sem_barras = ''.join(filter(str.isdigit, cpf))  # Remover barras do CPF
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf_sem_barras), None)

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        nova_conta = Conta(agencia, numero_conta, usuario)
        contas.append(nova_conta)
    else:
        print("\n*** Usuário não encontrado, fluxo de criação de conta encerrado! ***")

def listar_contas(contas):
    if not contas:
        print("\n=== Não há contas cadastradas. ===")
        return

    print("\n================ LISTA DE CONTAS ================")
    header = ["Agência", "Número da Conta", "Titular", "Saldo"]
    print("{:<15} {:<20} {:<30} {:<10}".format(*header))
    
    for conta in contas:
        info_conta = [conta.agencia, conta.numero_conta, conta.usuario['nome'], conta.saldo]
        print("{:<15} {:<20} {:<30} {:<10}".format(*info_conta))

    print("=" * 75)

def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            depositar(contas[-1], valor) if contas else print("\n*** Nenhuma conta cadastrada. ***")
            
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            sacar(contas[-1], valor) if contas else print("\n*** Nenhuma conta cadastrada. ***")

        elif opcao == "3":
            exibir_extrato(contas[-1]) if contas else print("\n*** Nenhuma conta cadastrada. ***")
        
        elif opcao == "6":
            criar_usuario(usuarios)
        
        elif opcao == "4":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            print("\n$$$$$ Banco Tabajara Agradeçe $$$$$")
            print("     ***** Volte Sempre *****\n")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
