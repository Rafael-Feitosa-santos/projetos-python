import os

from veiculo import Veiculo
from utils import pausar


class Estacionamento:

    def __init__(self):
        self.veiculos = {}
        self.ticket = 1

    def entrada(self):
        placa = input("Digite a placa: ").upper()

        if len(placa) != 7:
            print("Placa inválida! Deve conter 7 caracteres.")
            pausar()
            return

        for veiculo in self.veiculos.values():
            if veiculo.placa == placa:
                print("Veiculo com essa placa já está no estacionamento!")
                pausar()
                return

        veiculo = Veiculo(placa, self.ticket)
        self.veiculos[self.ticket] = veiculo
        os.system('cls' if os.name == 'nt' else 'clear')
        veiculo.comprovante()
        self.ticket += 1

    def saida(self):
        entrada = input("Informe o nº ticket (ENTER para cancelar): ")

        if entrada == "0" or entrada == "":
            print("Operação cancelada")
            return

        try:
            ticket = int(entrada)
        except ValueError:
            print("Entrada inválida")
            pausar()
            return

        if ticket in self.veiculos:
            veiculo = self.veiculos[ticket]

            veiculo.registra_saida()
            veiculo.comprovante()

            del self.veiculos[ticket]

        else:
            print("Veiculo não encontrado!")

    def listar(self):

        if not self.veiculos:
            print("Nenhum veiculo no estacionamento.")

        if self.veiculos:
            print("Veiculo encontrados: ")
            for ticket, veiculo in self.veiculos.items():
                print(
                    f"Ticket: {ticket} | Placa: {veiculo.placa[0:3]}-{veiculo.placa[3:]} | Entrada: {veiculo.entrada.strftime('%H:%M:%S')}")

        pausar()
