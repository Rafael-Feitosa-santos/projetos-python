import os

def rendimento_anual():
    capital = float(input("Qual o valor do investimento: ").replace(",", "."))
    taxa_anual = float(input("Taxa anual (%): ").replace(",", "."))
    meses = int(input("Prazo da aplicação (meses): "))

    anos = meses / 12

    valor_final = capital * (1 + taxa_anual / 100) ** anos
    rendimento = valor_final - capital

    print("\nResumo da aplicação")
    print(f"Capital inicial: R$ {capital:,.2f}")
    print(f"Taxa anual: {taxa_anual:.2f}%")
    print(f"Prazo: {meses} meses ({anos:.2f} anos)")
    print(f"Valor final: R$ {valor_final:,.2f}")
    print(f"Rendimento: R$ {rendimento:,.2f}")


def redimento_mensal():
    capital = float(input("Qual o valor investimento: ").replace(",", "."))
    taxa_mensal = float(input("Taxa mensal %: ").replace(",", "."))
    meses = int(input("Prazo da aplicação (meses): "))

    valor_final = capital * (1 + taxa_mensal / 100) ** meses
    rendimento = valor_final - capital

    print("\nResumo da aplicação")
    print(f"Capital inicial: R$ {capital:,.2f}")
    print(f"Taxa mensal: {taxa_mensal:.2f}%")
    print(f"Prazo: {meses} meses")
    print(f"Valor final: R$ {valor_final:,.2f}")
    print(f"Rendimento: R$ {rendimento:,.2f}")


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def voltar_ao_menu_principal():
    input('Tecle ENTER para voltar ao menu!')
    limpar_tela()


while True:
    print("\n=== CALCULADORA DE JUROS COMPOSTOS ===")
    print("""
        1 - Juros compostos mensal.
        2 - Juros compostos anual.
        0 - Sair
    """)
    try:
        opcao = int(input("Escolha a opção: "))

        if opcao == 1:
            limpar_tela()
            redimento_mensal()
            print("")
            voltar_ao_menu_principal()
        elif opcao == 2:
            limpar_tela()
            rendimento_anual()
            print("")
            voltar_ao_menu_principal()
        elif opcao == 0:
            limpar_tela()
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida! tente novamente!")
            input("Pressione ENTER para continuar...")
            limpar_tela()
    except ValueError:
        print("\n❌ Erro de valor. Por favor, insira um número válido.\n")
        voltar_ao_menu_principal()

    except KeyboardInterrupt:
        limpar_tela()
        print("\n⏹️ Execução interrompida pelo usuário.")
        break
        limpar_tela()
