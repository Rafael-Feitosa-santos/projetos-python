carrinho = []
total = 0.0

n = int(input("Informe a quantidade de itens: ").strip())

for _ in range(n):
    linha = input("Informe os produtos: ").strip().replace(",", ".")
    posicao_espaco = linha.rfind(" ")
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    carrinho.append((item, preco))
    total += preco

for produto, preco in carrinho:
    print(f"{produto}: R${preco:.2f}")

print(f"Total: R${total:.2f}")
