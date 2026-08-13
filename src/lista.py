numeros = [1, 2, 2, 3, 4, 4, 5]

sem_repetidos = []

for numero in numeros:
    if numero not in sem_repetidos:
        sem_repetidos.append(numero)

print(sem_repetidos)

print("=" * 35)

sem_repetidos = list(set(numeros))
print(sem_repetidos)
