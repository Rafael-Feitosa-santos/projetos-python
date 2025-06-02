import datetime
import pytz

class Telefone:
    def __init__(self, historico_chamadas = None, historico_mensagem = None):
        if historico_chamadas is None:
            historico_chamadas = []
        if historico_mensagem is None:
            historico_mensagem = []
        self.historico_chamadas = historico_chamadas
        self.historico_mensagem = historico_mensagem

    def fazer_chamadas(self, numero):
        tz_brasilia = pytz.timezone('America/Sao_Paulo')
        data_hora = datetime.datetime.now().strftime("%H:%M - %d/%m/%y")
        self.historico_chamadas.append((numero, data_hora))
        print(f"Chamadas: {numero}")

    def enviar_mensagem(self, numero, texto):
        tz_brasilia = pytz.timezone('America/Sao_Paulo')
        data_hora = datetime.datetime.now().strftime("%H:%M - %d/%m/%y")
        self.historico_mensagem.append((numero, texto, data_hora))
        print(f"Enviando mensagem para {numero}: {texto}")

    def visualizar_historico_chamadas(self):
        print("Histórico de chamadas:")
        for numero, data_hora in self.historico_chamadas:
            print(f"Chamada para {numero} em {data_hora}")

    def visualizar_historico_mensagem(self):
        print("Histórico de mensagens:")
        for numero, texto, data_hora in self.historico_mensagem:
            print(f"Mensagem enviada para {numero} em {data_hora}: {texto}")
