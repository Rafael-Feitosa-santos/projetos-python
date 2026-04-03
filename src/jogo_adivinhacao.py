from random import randint


def jogo_adivinhacao(numero_inicial, numero_final):
    
    if numero_inicial > numero_final:
        print("\n\033[1;31mERRO: O número inicial deve ser menor que o número final!\033[0m")
        return
    elif numero_inicial == numero_final:
        print("\n\033[1;31mERRO: O número inicial não pode ser igual ao número final!\033[0m")
        return
    
    numero_secreto = randint(numero_inicial,numero_final)
    tentativas = 0
    tentativas_maximo = 5
    
    try:
        while tentativas < tentativas_maximo:
            print("-" * 35)
            tentativa = int(input(f"Adivinhe o número entre {numero_inicial} a {numero_final}: "))
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
                    f"\n======== \033[1;31mVocê atingiu o limite de {tentativas} tentativas. O número era {numero_secreto}.\033[0m ========")
                break
    except ValueError:
        print("Entrada inválida!!")
        

def main():
    print("=====================================")
    print("======== Jogo da Adivinhação ========")
    print("=====================================")
    
    numero_inicial = int(input("Informe o número inicial: "))
    numero_final = int(input("Informe o número final: "))
    
    jogo_adivinhacao(numero_inicial,numero_final)


if __name__ == "__main__":
    main()