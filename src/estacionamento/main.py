import time
from estacionamento import Estacionamento

from utils import limpar_tela, transicao, pausar


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
            transicao("Registrando entrada")
            limpar_tela()
            estacionamento.entrada()

        elif opcao == "2":
            limpar_tela()
            transicao("Registrando saída")
            estacionamento.saida()
            pausar()

        elif opcao == "3":
            limpar_tela()
            transicao("Consultando")
            limpar_tela()
            estacionamento.listar()

        elif opcao == "4":
            limpar_tela()
            transicao("Encerrando sistema")
            limpar_tela()
            print("Sistema encerrado!")
            break

        else:
            limpar_tela()
            print("Opção inválida ❌ ")
            pausar()


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\nEncerrado pelo usuário!")
