def validar_entrada(valor):
    return float(valor.replace(",", "."))


menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:
    try:
        print(menu)
        opcao = int(input("Informe a operação que deseja fazer: "))

        if opcao == 1:
            valor = validar_entrada(input("Informe o valor que deseja depositar: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito de R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == 2:
            valor = validar_entrada(input("Informe o valor que deseja sacar: "))

            excedeu_saque = numero_saques >= LIMITE_SAQUES
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite

            if excedeu_saque:
                print("Operação falhou! Número máximo de saques excedido.")

            elif excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor excedeu o limite permitido por saque.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque de R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == 3:
            print(" Extrato ".center(45, "*"))
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("".center(45, "*"))

        elif opcao == 4:
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida! Por favor, selecione novamente a operação desejada.")

    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
        break

    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
