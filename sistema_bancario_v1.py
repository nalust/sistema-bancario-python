menu = '''
============ Menu ============

Escolha uma das opções:

    (1) Extrato
    (2) Depósito
    (3) Saque
    (0) Sair

==============================    
'''

saldo = 0
deposito = 0
quantidade_saque = 0
limite_saque_diario = 0
saque = 0

while True:
    option = input(menu)

    if option == '1':
        print(' Extrato '.center(20, '*'))

        if deposito == 0 and saque == 0:
            print(f'''Não foram realizadas movimentações.
                Saldo atual: {saldo}''')
        else:
           
            print(f'''
            Depósito: R${deposito}
            Saque: R${saque}

            Saldo: R${saldo}
            ''')

    elif option == '2':
        print(' Depósito '.center(20, '*'))
        valor_deposito = float(input('Qual valor deseja depositar? '))
        saldo += valor_deposito
        print('Depósito realizado com sucesso!')
        deposito += valor_deposito

    elif option == '3':
        print(' Saque '.center(20, '*'))
        
        if limite_saque_diario <= 1500:
            valor_saque = float(input('Informe o valor do saque: '))
            if valor_saque <= 500:
                if saldo >= valor_saque:
                    if quantidade_saque < 3:
                        limite_saque_diario += valor_saque
                        saldo -= valor_saque
                        print('Saque realizado com sucesso!')
                        quantidade_saque += 1
                        saque += valor_saque
                    else:
                        print('O limite é de 3 (três) saques por dia.')
                else:
                    print('Saldo insuficiente.')
            else:
                print('O limite por saque é de R$ 500.')
        else:
            print('O limite de saque diário é de R$ 1.500.')
            
    elif option == '0':
        print('Obrigado por utilizar nossos serviços!')
        break

    else:
        print('Opção inválida. Selecione uma das opções do menu.')