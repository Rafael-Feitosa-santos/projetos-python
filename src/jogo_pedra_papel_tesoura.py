from random import randint
import time

opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}


def menu():
    print("\n" + " Jogo - Pedra, Papel e Tesoura ".center(50, "#"))
    print("Escolha opções abaixo: ")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("0 - Sair")


vitorias = 0
derrotas = 0
empates = 0

while True:
    try:
        menu()
        jogador = int(input("\nInforme a opção desejada: "))

        if jogador == 0:
            print("\nSaindo do jogo..")
            break

        if jogador not in opcoes:
            print("Opção inexistente, escolha 1, 2 ou 3")
            continue

        computador = randint(1, 3)

        print("\nJO...")
        time.sleep(0.5)
        print("KEN...")
        time.sleep(0.5)
        print("PO!!! ✊✋✌️\n")
        time.sleep(0.3)

        print(f"Você escolheu: {opcoes[jogador]}")
        print(f"Computador escolheu: {opcoes[computador]}")

        if jogador == computador:
            print("""    #### Empate ⚖️ #### """)
            empates += 1

        elif ((jogador == 1 and computador == 3) or
              (jogador == 2 and computador == 1) or
              (jogador == 3 and computador == 2)):
            print("""    #### Você Ganhou! 🏆🎉 #### """)
            vitorias += 1

        else:
            print("""    #### Perdeu 😞 #### """)
            derrotas += 1

        print("\n===== PLACAR ATUAL =====")
        print(f"Vitórias: {vitorias} | Derrotas: {derrotas} | Empates: {empates}")
        print("=========================\n")

    except ValueError:
        print("Entrada inválida. Tente novamente.")

    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário. Saindo do jogo..")
        break
