import os

lista = []

while True:
    print("Escolha uma opção:")
    escolha = input("[1]inserir, [2]apagar, [3]lista: ")

    if escolha == '1':
        os.system('cls')
        adicionar = input("Insira o produto: ").title()
        lista.append(adicionar)

    elif escolha == '2':
        os.system('cls')
        deletar = input("Deletar produto: ").title()
        if deletar not in lista:
            print("Produto não encontrado")
        else:
            lista.remove(deletar)

    elif escolha == '3':
        os.system('cls')
        enumerar = enumerate(lista, start=1)
        if lista:
            for indice, item in enumerar:
                print(f"{indice} - {item}")
        else:
            print(" ######## Lista está vázia!  ########")
    else:
        print("Nenhuma opção foi escolhida.")
