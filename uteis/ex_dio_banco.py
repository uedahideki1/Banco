import pr


def menu(valor):
    print('-' * 20)
    print(valor)
    print('-' * 20)


def linhas():
    print('-' * 70)


lista_dinheiro_depositado = list()
saque_lista = list()

deposito_total = dinheiro_depositado = novo_saldo = 0
quantidade = 1
saldo = 1000
txt = 'menu'
menu(f'{txt:^20}')

opcao = ''

while opcao != 'l':
    linhas()
    print('Para sacar aperte [s]')
    print('Para depositar aperte [d]')
    print('Para ver extrato aperte [e]')
    print('Para sair aperte [q]')
    linhas()
    opcao = str(input('escolha uma das opçes abaixo: ')).strip().lower()[0]

    if opcao == 's':

        saque = int(input('Qual o valor do saque? '))
        while saque > 500:
            print('limite maximo 500')
            saque = int(input('Qual o valor do saque? '))
        if quantidade <= 3:
            if saldo >= saque:
                if saque <= 500:
                    saque_lista.append(saque)
                    saldo -= saque
                    print('sucesso valor sacado')
                    quantidade += 1

            else:
                print('Não possui saldo suficiente')

        else:
            print('atingiu o limite diario de saque')



    elif opcao == 'd':
        dinheiro_depositado = int(input('Digite o valor de deposito: '))
        while True:
            if dinheiro_depositado >= 1:
                linhas()
                lista_dinheiro_depositado.append(dinheiro_depositado)
                saldo += dinheiro_depositado

                break
            else:
                while dinheiro_depositado <= 1:
                    print('Erro ao depositar digite um valor maior que 1 R$')
                    dinheiro_depositado = int(input('Digite o valor de deposito: '))

    elif opcao == 'e':
        novo_saldo1 = deposito_total - novo_saldo
        print(f'Mostrando todos os depositos {lista_dinheiro_depositado} ')
        print(f'mostrando todos os saques {saque_lista}')
        print(f'o saldo atual da conta e {saldo}')


    elif opcao == 'q':
        break

    else:
        print('Opção invalida digite novamente')
