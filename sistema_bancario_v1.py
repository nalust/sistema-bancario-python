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
valor_deposito = 0

while True:
    option = input(menu)

    if option == '1':
        print(' Extrato '.center(20, '*'))
        print(f'''
        Déposito: {valor_deposito}
        Saldo: {saldo}
        ''')

    elif option == '2':
        print(' Depósito '.center(20, '*'))
        valor_deposito = float(input('Qual valor deseja depositar? '))
        saldo += valor_deposito

    elif option == '3':
        print(' Saque '.center(20, '*'))

    elif option == '0':
        print('Obrigado por utilizar nossos serviços!')
        break

    else:
        print('Opção inválida. Selecione uma das opções do menu.')