def calculo_redondo(diametro, espessura, comprimento):
    percentual = 0.02504
    return (diametro - espessura) * espessura * percentual * comprimento


def calculo_quadrado(diametro, espessura, comprimento):
    percentual = 0.008
    area = (diametro * 4) - (espessura * 8)
    peso = area * espessura * percentual * comprimento
    return peso


def calculo_retangular(diametro_maior, diametro_menor, espessura, comprimento):
    percentual = 0.008
    area = (diametro_maior + diametro_menor) * 2 - (espessura * 8)
    peso = area * espessura * percentual * comprimento
    return peso


def erro_insercao(diametro, espessura, pecas):
    if diametro == 0 or espessura == 0 or pecas == 0:
        print("\nAtenção!!\nExiste campos que estão zerados, tente novamente.\n")
        return True
    return False


def validar_entrada(valor):
    return float(valor.replace(",", "."))


op = -1

while op != 4:
    print("#####################################")
    print("Cálculo de beneficiamento".center(35))
    print("#####################################\n")

    print("Escolha a opção desejada:\n")
    print("[1] - Tubo Redondo")
    print("[2] - Tubo Quadrado")
    print("[3] - Tubo Retangular")
    print("[4] - Sair\n")

    try:
        op = int(input("Selecione a operação desejada: "))

        if op == 1:
            diametro = validar_entrada(input("Insira o diâmetro: "))
            espessura = validar_entrada(input("Insira a espessura: "))
            pecas = int(input("Quantidade de peças: "))
            tamanho_peca = 6
            comprimento = pecas * tamanho_peca

            if erro_insercao(diametro, espessura, pecas):
                continue

            calculo = calculo_redondo(diametro, espessura, comprimento)

            print(f"\nTotal de metros: {comprimento} mts")
            print(f"Peso: {calculo:.0f} kg \n")

        elif op == 2:
            diametro = validar_entrada(input("Insira o diâmetro: "))
            espessura = validar_entrada(input("Insira a espessura: "))
            pecas = int(input("Quantidade de peças: "))
            tamanho_peca = 6
            comprimento = pecas * tamanho_peca

            if erro_insercao(diametro, espessura, pecas):
                continue

            calculo = calculo_quadrado(diametro, espessura, comprimento)

            print(f"\nTotal de metros: {comprimento} mts")
            print(f"Peso: {calculo:.0f} kg \n")

        elif op == 3:
            diametro_menor = validar_entrada(input("Insira o diâmetro menor: "))
            diametro_maior = validar_entrada(input("Insira o diâmetro maior: "))
            espessura = validar_entrada(input("Insira a espessura: "))
            pecas = int(input("Quantidade de peças: "))
            tamanho_peca = 6
            comprimento = pecas * tamanho_peca

            if erro_insercao(diametro_maior, espessura, pecas) or erro_insercao(diametro_menor, espessura, pecas):
                continue

            calculo = calculo_retangular(diametro_maior, diametro_menor, espessura, comprimento)

            print(f"\nTotal de metros: {comprimento} mts")
            print(f"Peso: {calculo:.0f} kg \n")

        elif op == 4:
            print("Saindo...")
        else:
            print("\nOpção inválida. Tente novamente.\n")

    except ValueError:
        print("\nErro de valor. Por favor, insira um número válido.\n")
    except Exception as e:
        print(f"\nErro inesperado: {e}\n")
