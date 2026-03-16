import os

from estacionamento import Estacionamento


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    estacionamento = Estacionamento()

    while True:

        limpar_tela()

        print("====== ESTACIONAMENTO ======")
        print("1 - Entrada de veículo")
        print("2 - Saída de veículo")
        print("3 - Listar veículos")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            limpar_tela()
            estacionamento.entrada()
            limpar_tela()

        elif opcao == "2":
            limpar_tela()
            estacionamento.saida()
            limpar_tela()

        elif opcao == "3":
            limpar_tela()
            estacionamento.listar()
            limpar_tela()

        elif opcao == "4":
            limpar_tela()
            print("Sistema encerrado")
            break

        else:
            limpar_tela()
            print("Opção inválida")
            input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário!")
