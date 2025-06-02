import random


def sortear(inicio, final):
    return random.randint(inicio, final)


while True:
    try:
        inicio = int(input("Digite o número inicial: "))
        final = int(input("Digite o número final: "))

        if inicio > final:
            print("O valor inicial não pode ser maior que o final!")
            continue

        numero_sorteado = sortear(inicio, final)
        print(f"O número sorteado foi: {numero_sorteado}")

    except ValueError:
        print("Entrada inválida")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower().strip() != "s":
        print("Finalizando...")
        break
