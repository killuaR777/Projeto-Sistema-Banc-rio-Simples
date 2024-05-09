from time import sleep
print("-="*20)
print(" "*3, "SISTEMA BANCÁRIO DIO".center(30, "="))
print("-="*20)
sleep(0.5)
saldo = 100
Deposito = 0
Saque = 0
limite_saque = 0
extrato_saque = []
extrato_deposito = []
quant_saques = 0
print("Bem vindo ao banco DIO!")
print("-="*20)

while True:
    menu = print("""
    
        [ 1 ] Saldo
        [ 2 ] Depósito
        [ 3 ] Saque
        [ 4 ] Extrato
        [ 5 ] Finalizar
    
    """)

    opcao_de_menu = int(input("Qual serviço deseja realizar? "))

    if opcao_de_menu == 1:
        print("-="*20)
        print(f"No momento, o seu Saldo é de: R${saldo}")
    elif opcao_de_menu == 2:
        print("-=" * 20)
        Deposito = int(input("Quanto deseja depositar? R$"))
        if Deposito <= 0:
            print("-=" * 20)
            print("Não é possível Depisitar Valores Negativos")
        else:
            print("-=" * 20)
            print("Deposito Feito com sucesso!")
            saldo += Deposito
            extrato_deposito.append(Deposito)
            print("-=" * 20)
            print(f"O seu saldo agora é de R${saldo}")
    elif opcao_de_menu == 3:
        print("-=" * 20)
        valor_saque = float(input("Quantos Reais você deseja sacar? R$"))
        if valor_saque <= 0:
            print("-=" * 20)
            print("Valor de saque inválido")
        elif saldo <= 0:
            print("-=" * 20)
            print("Saldo insuficiente para fazer o saque")
        elif limite_saque >= 3:
            print("-=" * 20)
            print("limite de saque diario atingido! Tente denovo amanhã")
        elif valor_saque > saldo:
            print("-=" * 20)
            print("Seu saldo é insuficiente para fazer o saque. ")
        else:
            saldo -= valor_saque
            limite_saque += 1
            quant_saques += 1
            extrato_saque.append(valor_saque)
            print("-=" * 20)
            print("Saldo realizado com sucesso ")
            print("-=" * 20)
            print(f"Seu saldo agora é de R${saldo}")
    elif opcao_de_menu == 4:
        print("-=" * 20)
        print("--EXTRATO DO DIA--")
        print("-=" * 20)
        print(f"Saques: R${extrato_saque} ")
        print("-=" * 20)
        print(f"Depositos: R${extrato_deposito}")
    elif opcao_de_menu == 5:
        print("-=" * 30)
        print("Muito obrigado por escolher o nosso Banco. Até a proxima! :)")
        print("-=" * 30)
        break
    else:
        print("-=" * 30)
        print("Ainda não temos essa opção, Por enquanto, escolha alguma das opções acima: ")
        print("-=" * 30)
        sleep(1)