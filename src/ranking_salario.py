import random

qtd = 10
salario = [random.uniform(1518, 2500) for i in range(qtd)]

salario_ordem = sorted(salario)
salario_formato = [round(i, 2) for i in salario_ordem]

print(f"Todos os salários - Total: {len(salario_formato)}")
for i in salario_formato:
    print(f"- R${i}")

print("=" * 47)

salarios_maiores_2000 = [s for s in salario if s > 2000]
salarios_maiores_2000 = sorted(salarios_maiores_2000)
salario_formato = [round(i, 2) for i in salarios_maiores_2000]

print(f"Todos salários acima de R$ 2.000,00 - Total: {len(salarios_maiores_2000)}")
for i in salario_formato:
    print(f"- R${i}")
