def menu():
    menu = """\n
    ================ MENU ================
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q] \tSair

    => """
    return input(menu)

def depositar(saldo, deposito, extrato, /):
    if not validaDepositoNegativo(deposito):
        print("Depósito inválido. Informe um valor positivo")
    else:
        saldo += deposito
        extrato += f"\nDepósito no valor de R$ {deposito:.2f}"

    return saldo, extrato

def validaDepositoNegativo(deposito):
    return deposito > 0

def sacar(*, saldo, valor_saque, extrato, limite, numero_saques):
    if not validaLimiteValorSaques(valor_saque, limite):
        print(f"Não é possível sacar, pois o valor é maior que o limite de R$ {limite} por saque.")
        return saldo, extrato
    
    if not validaSaldoParaSaque(valor_saque, saldo):
        print("Não é possível sacar, pois não tem saldo suficiente.")
        return saldo, extrato

    numero_saques += 1
    saldo -= valor_saque
    extrato += f"\nSaque número {numero_saques} no valor de R$ {valor_saque:.2f}"

    return saldo, extrato, numero_saques


def validaLimiteQuantidadeSaques(numero_saques, limite_saques):
    return numero_saques < limite_saques

def validaLimiteValorSaques(valor_saque, limite):
    return valor_saque <= limite

def validaSaldoParaSaque(valor_saque, saldo):
    return valor_saque <= saldo

def emitirExtrato(saldo, /, *, extrato):
    titulo = "Extrato da conta"
    print(titulo.center(35,"-"))
    print(extrato) if extrato else print("Não existem movimentos no período.")
    print(f"\nSaldo atual da conta: R$ {saldo:.2f}")
    print("".center(35,"-"))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            deposito = float(input("Digite o valor (positivo) de depósito: "))
            saldo, extrato = depositar(saldo, deposito, extrato)
        
        elif opcao == "s":
            if not validaLimiteQuantidadeSaques(numero_saques, LIMITE_SAQUES):
                print(f"Não é possível sacar, pois o número de saques é maior que o limite de {LIMITE_SAQUES} por dia.")
                continue

            valor_saque = float(input("Digite o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                            saldo=saldo,
                            valor_saque=valor_saque,
                            extrato=extrato,
                            limite=limite,
                            numero_saques=numero_saques,
                        )

        elif opcao == "e":
            emitirExtrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()