# Descrição
# Uma clínica médica quer automatizar seu sistema de atendimento. Crie uma função que organize os pacientes em ordem de prioridade com base na idade e na urgência do caso.
#
# 📌 Critérios de Prioridade:
#
# Pacientes acima de 60 anos têm prioridade.
# Pacientes que apresentam a palavra "urgente" na ficha têm prioridade máxima.
# Os demais pacientes são atendidos por ordem de chegada.
# Entrada
# Um número inteiro n, representando a quantidade de pacientes.
# n linhas seguintes, cada uma contendo os dados de um paciente no formato: nome, idade, status
# nome: string representando o nome do paciente.
# idade: número inteiro representando a idade do paciente.
# status: string que pode ser "urgente" ou "normal".
# Saída
# A saída deve exibir a lista dos pacientes ordenada de acordo com as regras de prioridade, no formato: Ordem de Atendimento: nome1, nome2, nome3, ...
# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
#
# Entrada	Saída
# 3
# Carlos, 40, normal
# Ana, 70, normal
# Bruno, 30, urgente
#
# Ordem de Atendimento: Bruno, Ana, Carlos
#
# 4
# Paula, 30, normal
# Ricardo, 60, normal
# Tiago, 60, urgente
# Amanda, 50, urgente
#
# Ordem de Atendimento: Tiago, Amanda, Ricardo, Paula
#
# 5
# João, 65, normal
# Maria, 80, urgente
# Lucas, 50, normal
# Fernanda, 25, normal
# Pedro, 90, urgente
#
# Ordem de Atendimento: Pedro, Maria, João, Lucas, Fernanda

try:
    n = int(input("Informe quantidade de pacientes: ").strip())
    pacientes = []

    for i in range(n):
        linha = input("Informe o nome, idade, status: ").strip().title()
        nome, idade, status = linha.split(", ")
        idade = int(idade)
        pacientes.append((i, nome, idade, status))

    urgentes = []
    idosos = []
    demais = []

    for i, nome, idade, status in pacientes:
        if status == "Urgente":  # devido ao .title()
            urgentes.append((i, nome, idade))
        elif idade >= 60:
            idosos.append((i, nome))
        else:
            demais.append((i, nome))

    # Ordenar urgentes por idade decrescente e se empate, pela ordem de chegada (i)
    urgentes.sort(key=lambda x: (-x[2], x[0]))

    # Idosos e demais pela ordem de chegada (i)
    idosos.sort(key=lambda x: x[0])
    demais.sort(key=lambda x: x[0])

    ordem_atendimento = [nome for _, nome, _ in urgentes] + \
                        [nome for _, nome in idosos] + \
                        [nome for _, nome in demais]

    # Print com numeração da ordem de atendimento
    print("Ordem de Atendimento:")
    for posicao, nome in enumerate(ordem_atendimento, start=1):
        print(f"{posicao}. {nome}")

except ValueError:
    print("Entrada inválida!")
