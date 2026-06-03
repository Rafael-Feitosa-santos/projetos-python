from random import choice

nomes = input("Digite vários nomes separados por vírgulas: ")
lista_nomes = nomes.split(",")

sorteado = choice(lista_nomes)

print(f"\n====== O nome sorteado foi {sorteado.strip().title()} ======")