import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


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


def erro_insercao(*args):
    for valor in args:
        if valor == 0:
            print("\n⚠️ Atenção!!\nExiste campos que estão zerados, tente novamente.\n")
            return True
    return False


def validar_entrada(valor):
    return float(valor.replace(",", "."))


def main():
    opcoes = {
        1: calculo_redondo,
        2: calculo_quadrado,
        3: calculo_retangular
    }

    while True:
        print("#####################################")
        print("📏 Cálculo de beneficiamento".center(33).title())
        print("#####################################\n")

        print("Escolha a opção desejada:\n")
        print("[1] - 🔵 Tubo Redondo")
        print("[2] - 🟥 Tubo Quadrado")
        print("[3] - 🟦 Tubo Retangular")
        print("[4] - ❌ Sair\n")

        try:
            op = int(input("Selecione a operação desejada: "))
            if op == 4:
                print("🚀 Sistema finalizado!")
                break

            if op not in opcoes:
                print("\n❌ Opção inválida. Tente novamente.\n")
                continue

            tamanho_peca = 6

            limpar_tela()

            if op == 3:
                diametro_menor = validar_entrada(input("Insira o diâmetro menor: "))
                diametro_maior = validar_entrada(input("Insira o diâmetro maior: "))
                espessura = validar_entrada(input("Insira a espessura: "))
                pecas = int(input("Quantidade de peças: "))
                comprimento = pecas * tamanho_peca

                if erro_insercao(diametro_maior, espessura, pecas):
                    continue

                calculo = calculo_retangular(diametro_maior, diametro_menor, espessura, comprimento)

            elif op in opcoes:
                diametro = validar_entrada(input("Insira o diâmetro: "))
                espessura = validar_entrada(input("Insira a espessura: "))
                pecas = int(input("Quantidade de peças: "))
                comprimento = pecas * tamanho_peca

                if erro_insercao(diametro, espessura, pecas):
                    continue

                calculo = opcoes[op](diametro, espessura, comprimento)

            print(f"\n📏 Total de metros: {comprimento} mts")
            print(f"⚖️ Peso: {calculo:.0f} kg ✅\n")

        except ValueError:
            print("\n❌ Erro de valor. Por favor, insira um número válido.\n")

        except KeyboardInterrupt:
            print("\n⏹️ Execução interrompida pelo usuário.")
            return

        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}\n")


if __name__ == "__main__":
    main()
