import os

lista = []

while True:
    print("Escolha uma opção:")
    escolha = input("[1]inserir, [2]apagar, [3]lista: ")

    if escolha == '1':
        os.system('cls')
        adicionar = input("Insira o produto: ")
        lista.append(adicionar)

    elif escolha == '2':
        os.system('cls')
        deletar = input("Deletar produto: ")
        lista.remove(deletar)

    elif escolha == '3':
        os.system('cls')
        enumerar = enumerate(lista)
        for item in enumerar:
            print(item)

    else:
        print("Nenhuma opção foi escolhida.")
