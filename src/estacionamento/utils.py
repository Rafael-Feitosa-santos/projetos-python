# utils.py

import os
import time


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def transicao(mensagem="Processando"):
    print(mensagem, end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")
    time.sleep(0.5)


def pausar():
    input("\nPressione ENTER para continuar...")
