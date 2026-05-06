import requests


def consulta_cep(cep):
    # URL base da API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"

    # Fazendo a requisição para a API
    response = requests.get(url)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        dados = response.json()
        return dados
    else:
        return {"erro": "Não foi possível consultar o CEP"}


while True:
    cep = input("Informe o CEP (ou 'sair' para parar): ")

    if cep.lower() == "sair":
        print("Programa finalizado")
        break

    resultado = consulta_cep(cep)

    if "erro" not in resultado:
        print("\nEndereço encontrado:")

        # Validando logradouro e bairro
        logradouro = resultado.get('logradouro', '')
        bairro = resultado.get('bairro', '')

        if not logradouro:
            logradouro = input("\nLogradouro não encontrado. Informe o logradouro manualmente: ").title().strip()
        if not bairro:
            bairro = input("Bairro não encontrado. Informe o bairro manualmente: ").title().strip()

        # Atualizando os dados
        resultado['logradouro'] = logradouro
        resultado['bairro'] = bairro

        # Exibindo os dados atualizados
        print(f"\nLogradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {resultado['localidade']}")
        print(f"Estado: {resultado['uf']}")

        numero = input("\nInforme o número do endereço: ")
        complemento = input("Informe o complemento (caso não haja, pressione Enter): ").title().strip()

        print("\n================ Consulta de Endereço  ================")
        print("\nEndereço completo:")
        print(f"Logradouro: {logradouro}")
        print(f"Número: {numero if numero else "s/n"}")
        print(f"Complemento: {complemento if complemento else "s/n"}")
        print(f"Bairro: {bairro if bairro else "s/n"}")
        print(f"Cidade: {resultado['localidade']}")
        print(f"Estado: {resultado['uf']}")
        print("=======================================================")
    else:
        print("Erro na consulta do CEP. Tente novamente.")