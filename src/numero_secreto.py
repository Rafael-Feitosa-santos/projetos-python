import random

numero_secreto = random.randint(1, 10)
tentativas = 0
tentativas_maximo = 5

try:
    while tentativas < tentativas_maximo:
        tentativa = int(input("Adivinhe o número entre 1 a 10: "))
        tentativas += 1

        if tentativa == numero_secreto:
            print(f"Parabéns! Você acertou!\nTotal de tentativas realizadas: {tentativas}")
            break

        elif tentativa < numero_secreto:
            print("Muito baixo.")
        else:
            print("Muito alto")

        if tentativas == tentativas_maximo:
            print(
                f"\n======== Você atingiu o limite de {tentativas} tentativas. O número era {numero_secreto}. ========")
            break

except ValueError:
    print("Entrada inválida!!")

