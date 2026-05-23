import os
from datetime import datetime, timedelta


def horario_brasilia():
    hora = datetime.now()
    horario_brasilia = hora
    horario_brasilia_formatada = horario_brasilia.strftime("%d/%m/%y às %H:%M")
    return horario_brasilia_formatada


produtos_cadastrados = {
    "iphone": {"preco": 5000, "quantidade": 10, "horario": "14/05/26 às 07:35"},
    "tv": {"preco": 3200, "quantidade": 5, "horario": "11/05/26 às 10:11"},
    "ps5": {"preco": 4500, "quantidade": 2, "horario": "09/05/26 às 09:35"}
}


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def voltar_ao_menu_principal():
    print()
    input('Tecle ENTER para voltar ao menu!')
    limpar_tela()


def validar_entrada(valor):
    return float(valor.replace(",", "."))


def formatacao_valor(valor):
    valor_formatado = f"{valor:,.2f}".replace(",", ".")
    valor_formatado = valor_formatado[::-1].replace(".", ",", 1)[::-1]
    return valor_formatado


def buscar_produto():
    produto = input("Insira o produto: ")

    if produto not in produtos_cadastrados:
        print("\n*** Produto não localizado ***")
    else:
        dados = produtos_cadastrados[produto]
        preco = formatacao_valor(dados["preco"])
        quantidade = dados["quantidade"]
        preco_total = formatacao_valor(dados["preco"] * dados["quantidade"])
        horario = dados["horario"]
        print(
            f"\nProduto: {produto.title()} | "
            f"Qtde: {quantidade} | "
            f"Unit: R$ {preco} | "
            f"Total: R$ {preco_total} - {horario}"
        )


def cadastrar_produto():
    produto = input("Digite o nome do produto: ").strip().lower()

    if produto in produtos_cadastrados:
        print(f"\n*** O produto '{produto.title()}' já está cadastrado! ***")
    else:
        try:
            preco = validar_entrada(input(f"Digite o preço do(a) {produto.title()}: "))
            quantidade = int(input("Digite a quantidade: "))

            produtos_cadastrados[produto] = {
                "preco": preco,
                "quantidade": quantidade,
                "horario": horario_brasilia()
            }
            print(f"\n>>> Produto '{produto.title()}' cadastrado com sucesso - {horario_brasilia()}! <<<")
        except ValueError:
            print("\n*** Preço inválido! Digite apenas números. ***")


def deletar_produto():
    produto = input("Digite o nome do produto que deseja deletar: ").strip().lower()

    if produto in produtos_cadastrados:
        del produtos_cadastrados[produto]
        print(f"\n>>> Produto '{produto.title()}' deletado com sucesso! <<<")
    else:
        print(f"\n*** O produto '{produto.title()}' não está cadastrado! ***")


def listar_produtos():
    if not produtos_cadastrados:
        print("Lista vazia!")
    else:
        for nome, dados in produtos_cadastrados.items():
            preco = formatacao_valor(dados["preco"])
            quantidade = dados["quantidade"]
            preco_total = formatacao_valor(dados["preco"] * dados["quantidade"])
            horario = dados["horario"]
            print(
                f"Produto: {nome.title()} | "
                f"Qtde: {quantidade} | "
                f"Unit: R$ {preco} | "
                f"Total: R$ {preco_total} - {horario}"
            )


def atualizar_produto():
    produto = input("Digite o nome do produto que deseja atualizar: ").strip().lower()

    if produto in produtos_cadastrados:
        print("\nO que você deseja atualizar?")
        print("1 - Nome do produto")
        print("2 - Valor do produto")
        print("3 - Quantidade do produto")
        print("4 - Nome, valor e quantidade")

        try:
            escolha = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n*** Entrada inválida! Digite apenas números. ***")
            return

        if escolha == 1:
            novo_nome = input("Digite o novo nome: ").strip().lower()
            produtos_cadastrados[novo_nome] = produtos_cadastrados.pop(produto)
            print(f"\n>>> Nome atualizado para '{novo_nome.title()}' com sucesso! <<<")

        elif escolha == 2:
            try:
                novo_preco = float(input("Digite o novo preço: "))
                produtos_cadastrados[produto]["preco"] = novo_preco
                print(f"\n>>> Preço do(a) '{produto.title()}' atualizado com sucesso! <<<")
            except ValueError:
                print("\n*** Preço inválido! Digite apenas números. ***")

        elif escolha == 3:
            try:
                nova_qtd = int(input("Digite a nova quantidade: "))
                produtos_cadastrados[produto]["quantidade"] = nova_qtd
                print(
                    f"\n>>> Quantidade do(a) '{produto.title()}' "
                    f"atualizada para {nova_qtd}! <<<"
                )
            except ValueError:
                print("\n*** Quantidade inválida! Digite apenas números inteiros. ***")

        elif escolha == 4:
            novo_nome = input("Digite o novo nome: ").strip().lower()
            try:
                novo_preco = float(input("Digite o novo preço: "))
                nova_qtd = int(input("Digite a nova quantidade: "))
                produtos_cadastrados[novo_nome] = {
                    "preco": novo_preco,
                    "quantidade": nova_qtd
                }
                del produtos_cadastrados[produto]
                print(
                    f"\n>>> Produto atualizado para '{novo_nome.title()}' "
                    f"com preço R$ {novo_preco:.2f} e quantidade {nova_qtd}! <<<"
                )
            except ValueError:
                print("\n*** Entrada inválida! Digite números válidos. ***")

        else:
            print("\n*** Opção inválida! ***")
    else:
        print(f"\n*** O produto '{produto.title()}' não está cadastrado! ***")


def menu():
    print("\n============= Sistema de consulta de produtos =============".title())
    print()
    print("1 - Cadastrar de produto.")
    print("2 - Consultar por produto.")
    print("3 - Deletar produto.")
    print("4 - Listar todos os produtos.")
    print("5 - Atualizar produto")
    print("6 - Sair")


while True:
    menu()
    op = int(input("\nInforme a operação que deseja realizar: "))

    match op:
        case 1:
            limpar_tela()
            cadastrar_produto()
            voltar_ao_menu_principal()
        case 2:
            limpar_tela()
            buscar_produto()
            voltar_ao_menu_principal()
        case 3:
            limpar_tela()
            deletar_produto()
            voltar_ao_menu_principal()
        case 4:
            limpar_tela()
            listar_produtos()
            voltar_ao_menu_principal()
        case 5:
            limpar_tela()
            atualizar_produto()
            voltar_ao_menu_principal()
        case 6:
            limpar_tela()
            print("\n***** \033[1mSistema finalizado\033[0m *****")
            break
        case default:
            print("Opção inválida!")
