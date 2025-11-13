import random

nomes = ["Rafael", "Davi", "Matilde", "Gabriela"]
contagem = {nome: 0 for nome in nomes}

# Números de sorteios
total_sorteios = 10

for i in range(total_sorteios):
    sorteado = random.sample(nomes, 1)[0]
    contagem[sorteado] += 1
    print(f"{i + 1}º sorteado foi: {sorteado}")

print("\nContagem de sorteios:")
for nome, vezes in contagem.items():
    print(f"{nome}: {vezes} vez(es)")
