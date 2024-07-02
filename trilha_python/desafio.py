menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def validaDepositoNegativo():
    return deposito > 0

def validaLimiteQuantidadeSaques():
    return numero_saques < LIMITE_SAQUES

def validaLimiteValorSaques():
    return valor_saque <= limite

def validaSaldoParaSaque():
    return valor_saque <= saldo

def emitirExtrato():
    titulo = "Extrato da conta"
    print(titulo.center(35,"-"))
    print(extrato) if extrato else print("Não existem movimentos no período.")
    print(f"\nSaldo atual da conta: R$ {saldo:.2f}")
    print("".center(35,"-"))


while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Digite o valor (positivo) de depósito: "))
        if not validaDepositoNegativo():
            print("Depósito inválido. Informe um valor positivo")
        else:
            saldo += deposito
            extrato += f"\nDepósito no valor de R$ {deposito:.2f}"
    
    elif opcao == "s":
        if not validaLimiteQuantidadeSaques():
            print(f"Não é possível sacar, pois o número de saques é maior que o limite de {LIMITE_SAQUES} por dia.")
            continue

        valor_saque = float(input("Digite o valor do saque: "))
        if not validaLimiteValorSaques():
            print(f"Não é possível sacar, pois o valor é maior que o limite de R$ {limite} por saque.")
            continue
        
        if not validaSaldoParaSaque():
            print("Não é possível sacar, pois não tem saldo suficiente.")
            continue

        numero_saques += 1
        saldo -= valor_saque
        extrato += f"\nSaque número {numero_saques} no valor de R$ {valor_saque:.2f}"

    elif opcao == "e":
        emitirExtrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
