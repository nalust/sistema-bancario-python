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
quantidade_saque = 0
limite_saque_diario = 0
extrato = ''

while True:
    option = input(menu)

    if option == '1':
        print(' Extrato '.center(20, '*'))

        if extrato == '':
            print(f'''Não foram realizadas movimentações.

                Saldo: R$ {saldo:.2f}''')
        else:
            print(extrato)
            print(f'Saldo: R$ {saldo:.2f}')

    elif option == '2':
        print(' Depósito '.center(20, '*'))
        valor_deposito = float(input('Qual valor deseja depositar? '))
        saldo += valor_deposito
        print('Depósito realizado com sucesso!')
        extrato += f'Depósito: R$ {valor_deposito:.2f}\n'

    elif option == '3':
        print(' Saque '.center(20, '*'))
        
        valor_saque = float(input('Informe o valor do saque: '))
        if valor_saque <= 500:
            if saldo >= valor_saque:
                if quantidade_saque < 3:
                    limite_saque_diario += valor_saque
                    saldo -= valor_saque
                    print('Saque realizado com sucesso!')
                    quantidade_saque += 1
                    extrato += f'Saque: R$ {valor_saque:.2f}\n'
                else:
                    print('O limite é de 3 (três) saques por dia.')
            else:
                print('Saldo insuficiente.')
        else:
            print('O limite por saque é de R$ 500.')
       
    elif option == '0':
        print('Obrigado por utilizar nossos serviços!')
        break

    else:
        print('Opção inválida. Selecione uma das opções do menu.')