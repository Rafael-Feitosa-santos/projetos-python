from math import ceil
from datetime import datetime


class Veiculo:
    preco_hora = 10
    hora_adicional = 5

    def __init__(self, placa, ticket):
        self.placa = placa
        self.ticket = ticket
        self.entrada = datetime.now()
        self.saida = None
        self.valor = 0

    def registra_saida(self):
        self.saida = datetime.now()

        tempo = self.saida - self.entrada
        horas = tempo.total_seconds() / 3600

        horas_cobradas = ceil(horas)

        if horas_cobradas <= 1:
            self.valor = self.preco_hora
        else:
            horas_adicionais = horas_cobradas - 1
            self.valor = self.preco_hora + (horas_adicionais * self.hora_adicional)

    def tempo_estacionado(self):
        if not self.saida:
            return 0, 0

        tempo = self.saida - self.entrada

        total_segundos = int(tempo.total_seconds())
        horas = total_segundos // 3600
        minutos = (total_segundos % 3600) // 60

        return horas, minutos

    def comprovante(self):
        print("\n------ COMPROVANTE ------")
        print(f"Ticket: {self.ticket}")
        print(f"Placa: {self.placa[:3]}-{self.placa[3:]}")
        print(f"Entrada: {self.entrada.strftime('%d/%m/%Y - %H:%M:%S')}")

        if self.saida:
            print(f"Saída: {self.saida.strftime('%d/%m/%Y - %H:%M:%S')}")

            horas, minutos = self.tempo_estacionado()

            print(f"Tempo estacionado: {horas}h {minutos}min")
            print(f"Valor: R$ {self.valor:.2f}")

        print("-------------------------\n")

        input("Pressione ENTER para continuar...")
