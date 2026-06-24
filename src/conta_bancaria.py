import os
import sys
import time
from datetime import datetime, timedelta


def horario_brasilia():
    hora = datetime.now()
    horario_brasilia = hora
    horario_brasilia_formataca = horario_brasilia.strftime("%H:%M - %d/%m/%y")
    return horario_brasilia_formataca


def validar_entrada(valor):
    return float(valor.replace(",", "."))


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def barra_progresso(texto, duracao=2):
    print(texto)
    for i in range(21):
        time.sleep(duracao / 20)
        sys.stdout.write("\r[" + "#" * i + "-" * (20 - i) + f"] {i * 5}%")
        sys.stdout.flush()
    print("\n")


def voltar_ao_menu_principal():
    input('Tecle ENTER para voltar ao menu!')
    limpar_tela()
    barra_progresso("Carregando menu...")
    limpar_tela()


def formatacao_valor(valor):
    valor_formatado = f"{valor:,.2f}".replace(",", ".")
    valor_formatado = valor_formatado[::-1].replace(".", ",", 1)[::-1]
    return valor_formatado


def menu():
    menu = """
==============================
       MENU DE OPERAÇÕES
==============================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
==============================
    """
    print(menu)
    return menu


saldo = 0
limite = 2000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 5

while True:

    try:
        menu()
        opcao = int(input("Informe a operação que deseja fazer: "))

        if opcao == 1:
            limpar_tela()
            valor = validar_entrada(input("Informe o valor que deseja depositar: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito de R$ {formatacao_valor(valor)} - {horario_brasilia()}\n"
                print("Depósito realizado com sucesso!!")
            else:
                print("\033[31mOperação falhou! O valor informado é inválido.\033[0m")

            voltar_ao_menu_principal()

        elif opcao == 2:
            limpar_tela()
            valor = validar_entrada(input("Informe o valor que deseja sacar: "))

            excedeu_saque = numero_saques >= LIMITE_SAQUES
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite

            if excedeu_saque:
                print("\033[31mOperação falhou! Número máximo de saques excedido.\033[0m")

            elif excedeu_saldo:
                print("\033[31mOperação falhou! Você não tem saldo suficiente.\033[0m")

            elif excedeu_limite:
                print("\033[31mOperação falhou! O valor excedeu o limite permitido por saque.\033[0m")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque de - R$ {formatacao_valor(valor)} - {horario_brasilia()}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!!")
            else:
                print("\033[31mOperação falhou! O valor informado é inválido.\033[0m")

            voltar_ao_menu_principal()

        elif opcao == 3:
            limpar_tela()
            barra_progresso("Emitindo extrato..")
            limpar_tela()

            print()
            print(" Extrato ".center(50, "*"))
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {formatacao_valor(saldo)}")
            print("".center(50, "*"))

            voltar_ao_menu_principal()

        elif opcao == 4:
            limpar_tela()
            print("Saindo do sistema.")
            break

        else:
            print("\033[31mOpção inválida! Por favor, selecione novamente a operação desejada.\033[0m")

    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário.")
        break

    except ValueError:
        limpar_tela()
        print("\033[31mEntrada inválida! Por favor, insira um número.\033[0m")
        voltar_ao_menu_principal()
