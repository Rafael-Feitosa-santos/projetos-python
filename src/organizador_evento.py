# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input("Informe números de participantes: ").strip())

for _ in range(n):
    linha = input("Informe o tema e o nome: ").strip().title()
    participante, tema = linha.split(", ")

    # Se o tema não estiver no dicionário, cria a lista
    if tema not in eventos:
        eventos[tema] = []

    # Adiciona o participante ao tema
    eventos[tema].append(participante)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
