Menu = ("""
      ########## Seja Bem Vindo(a) Banco Jacu ##########
      
                  $$$$$$$$$$ Menu $$$$$$$$$$
                  
      [1] Depositar
      [2] Sacar
      [3] extrato
      [4] Sair
      
      ################## Deus Abençoe ##################
      """)

saldo = 500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(Menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente, seu saldo é: ", saldo)
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.\nSeu limite é: ", limite)
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.\nSeu limite saque é: ", LIMITE_SAQUES)
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "3":
        print("\n================= extrato ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")
        
    elif opcao == "4":
        print("\n                Banco Jacu Agradeçe pela Parceria")
        print("\n      5################## Volte Sempre ################## \n")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")