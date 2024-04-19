import textwrap

def menu():
    menu = '''\n
    ============ Menu ============

    Escolha uma das opções:

    (1)\tExtrato
    (2)\tDepósito
    (3)\tSaque
    (4)\tNovo Usuário
    (5)\tNova Conta
    (6)\tListar Contas
    (0)\tSair

    ==============================    
    '''
    return input(textwrap.dedent(menu))

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print(' SAQUE '.center(20, '*'))

    if (valor <= limite) and (saldo >= valor) and (limite_saques > numero_saques):
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'

        print('Saque realizado com sucesso!')
    else:
        if valor >= limite:
            print('O limite de saque é de R$ 500 por operação.')
        elif saldo <= valor:
            print('Saldo insuficiente.')
        elif limite_saques >= numero_saques:
            print('O limite é de 3 (três) saques por dia.')

    return saldo, extrato

def depositar(saldo, valor, extrato, /):
    print(' DEPÓSITO '.center(20, '*'))
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}\n'

        print('Depósito realizado com sucesso!')
    else:
        print('A operação falhou. Valor inválido.')

    return saldo, extrato

def ver_extrato(saldo, /, *, extrato):
    print(' EXTRATO '.center(20, '*'))

    if extrato == '':
        print(f'''Não foram realizadas movimentações na conta.\n
                 Saldo: R${saldo:.2f}''')
    else:
        print(extrato)
        print(f'\nSaldo: R${saldo:.2f}')

def criar_usuario(lista_usuarios):
    cpf = input('Informe o CPF (apenas números): ')
    usuario = filtrar_usuario(cpf, lista_usuarios)

    if usuario:
        print('O usuário já está cadastrado no sistema.')
        return
    
    nome = input('Informe o nome completo (sem abreviações): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla do estado): ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')

    lista_usuarios.append({'nome': nome, 'cpf': cpf, 'endereco': endereco, 'data_nascimento': data_nascimento})

    print('\nUsuário criado com sucesso!')

def filtrar_usuario(cpf, lista_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, usuarios, numero_conta):
    cpf = input('Informe o CPF (apenas números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'usuario': usuario, 'numero_conta': numero_conta}
    
    print('Usuário não encontrado. Crie um novo usuário (Opção 4).')

def listar_contas(lista_contas):
    for conta in lista_contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']} 
        '''
        print('*' * 50)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUE = 500
    AGENCIA = '0001'

    saldo = 0
    extrato = ''
    limite_saques = 3
    numero_saques = 0
    limite = 500
    lista_usuarios = []
    lista_contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == '1':
            ver_extrato(saldo, extrato=extrato)

        elif opcao == '2':

            valor_deposito = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == '3':
            valor_saque = float(input('Informe o valor do saque: '))
            saldo, extrato = sacar(saldo = saldo, 
                                   valor = valor_saque, 
                                   extrato = extrato, 
                                   limite = LIMITE_SAQUE, 
                                   numero_saques = numero_saques, 
                                   limite_saques = limite_saques)
            limite_saques -= 1
            numero_saques += 1

        elif opcao == '4':
            criar_usuario(lista_usuarios)
        
        elif opcao == '5':
            conta = criar_conta(AGENCIA, lista_usuarios, numero_conta)

            if conta:
                lista_contas.append(conta)
                numero_conta += 1

        elif opcao == '6':
            listar_contas(lista_contas)

        elif opcao == '0':
            print('Obrigado por utilizar nossos serviços!')
            break

        else:
            print('Opção inválida. Selecione uma das opções do menu.')
        
main()