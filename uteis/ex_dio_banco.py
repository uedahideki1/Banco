import textwrap

def menu():
    menu = """
====================  Menu ========================
[d]\tDepositar
[s]\tSacar 
[e]\tExtrato
[nc]\tNova conta
[lc]\tListar contas
[nu]\tNovo usuário
[q]\tSair
=> """
    return input(textwrap.dedent(menu))


def sacar(*, saldo, saque, numero_saques):
    while True:
        if saque > 500:
            print('Limite máximo de saque: R$ 500')
            saque = float(input('Qual o valor do saque? '))
        if numero_saques <= 3:
            if saldo >= saque:
                saldo -= saque
                print('Sucesso! Valor sacado:', saque)
                numero_saques += 1
            else:
                print('Não possui saldo suficiente')
        else:
            print('Atingiu o limite diário de saque')
        return saldo


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, *, extrato):
    print("\n========= EXTRATO ===========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==================================")


def criar_usuario(usuarios):
    cpf = int(input("Digite seu CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@ Já existe um usuário com esse CPF! @@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("==== Usuário criado com sucesso! ====")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C\C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print('='*100)
        print(linha)


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def main():
    numeros_saques = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    usuarios = []
    contas = []

    opcao = menu()

    while opcao != 'q':
        if opcao == 's':
            saque = float(input('Qual o valor do saque? '))
            saldo = sacar(saldo=saldo, saque=saque, numero_saques=numeros_saques)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        else:
            print('Opção inválida, digite novamente')

        opcao = menu()


main()
