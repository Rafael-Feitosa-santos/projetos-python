import sys

import requests

TRADUCOES = {
    "Partly cloudy": "Parcialmente nublado",
    "Sunny": "Ensolarado",
    "Clear": "Céu limpo",
    "Cloudy": "Nublado",
    "Rain": "Chuva",
    "Light rain": "Chuva leve",
    "Heavy rain": "Chuva forte",
    "Snow": "Neve",
    "Fog": "Névoa",
    "Patchy rain nearby": "Chuvas esporádicas nas proximidades"

}


def clima(cidade):
    url = f"http://wttr.in/{cidade}?format=j1&lang=pt"
    resposta = requests.get(url, timeout=6)
    resposta.raise_for_status()

    try:
        if resposta.status_code == 200:
            dados = resposta.json()
            condicao = dados["current_condition"][0]
            temperatura = condicao["temp_C"]
            descricao_en = condicao["weatherDesc"][0]["value"]
            descricao = TRADUCOES.get(descricao_en, descricao_en)
            umidade = condicao["humidity"]
            vento = condicao["windspeedKmph"]

            print(f"\nClima em {cidade}:")
            print(f"🌡️ Temperatura: {temperatura}°C")
            print(f"☁️ Condição: {descricao}")
            print(f"💧 Umidade: {umidade}%")
            print(f"💨 Vento: {vento} km/h")

    except requests.exceptions.Timeout:
        print("A requisição demorou muito para responder.")
    except requests.exceptions.RequestException as erro:
        print(f"Erro ao buscar dados: {erro}")


executando = True

while executando:
    try:
        cidade = input("Informe o local que deseja verificar o tempo: ")
        clima(cidade)

        while True:
            sair = input("\nDeseja vê outro lugar?(S/N): ").upper()
            if sair == "N":
                print(" ==== Sistema finalizado! ====")
                executando = False
                break
            elif sair == "S":
                break
            else:
                print("Opção inválida! Digite apenas S ou N.")

    except KeyboardInterrupt:
        print("\n >>>> Sistema finalizado pelo usuario! <<<<")
        break
