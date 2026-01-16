import time
import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

clientes = {}


def barra_progresso(texto, duracao=2):
    print(texto)
    for i in range(21):
        time.sleep(duracao / 20)
        sys.stdout.write("\r[" + "#" * i + "-" * (20 - i) + f"] {i * 5}%")
        sys.stdout.flush()
    print("\n")


def cadastro():
    print("======= Bem vindo =======")
    barra_progresso("Entrando no sistema..")

    try:
        quantidade = int(input("Informe a quantidade de pessoas que deseja cadastrar: "))
    except ValueError:
        print("Entrada inválida, apenas valores númericos")
        return

    for i in range(quantidade):
        nome = input(f"Digite o nome da pessoa {i + 1}: ").title().strip()
        produto = input(f"Digite o produto de {nome}: ").title().strip()
        data_hora = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime("%H:%M:%S - %d/%m/%Y")
        clientes[nome] = {"produto": produto, "data_hora": data_hora}

    barra_progresso("Efetuando o cadastro..")

    os.system("cls" if os.name == "nt" else "clear")

    print("\n######## Dicionário criado: ########\n")
    print("------------- Produtos ------------- ")
    for idx, (nome, dados) in enumerate(clientes.items(), start=1):
        print(f" ID: {idx} - Nome: {nome} - produto:{dados["produto"]} - Data/Hora: {dados["data_hora"]}")
    print("------------------------------------")
    print(f"Cadastrados: {len(clientes)}")


cadastro()
