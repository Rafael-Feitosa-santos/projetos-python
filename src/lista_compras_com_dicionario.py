def adicionar_item(lista):
    produto = input("Digite o nome do produto: ").title()
    valor = float(input("Digite o valor do produto: ").replace(",", "."))

    if produto not in lista:
        lista[produto] = valor


def mostrar_lista(lista):
    total = 0
    print("\nLista de Compras:")
    for produto, valor in lista.items():
        print(f"{produto}: R$ {valor:.2f}")
        total += valor
    print(f"\nTotal: R$ {total:.2f}")


# Exemplo de uso
lista_de_compras = {}
while True:
    adicionar_item(lista_de_compras)
    continuar = input("Deseja adicionar mais um item? (s/n): ").strip().lower()
    if continuar.lower() != 's':
        break

mostrar_lista(lista_de_compras)
