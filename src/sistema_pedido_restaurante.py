# Descrição
# Crie uma classe Pedido que represente um pedido em um restaurante, contendo os itens pedidos e um método para calcular o valor total da conta.
#
# Entrada
# Lista de itens e seus respectivos preços.
# Saída
# O valor total da conta.
# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
#
# Entrada	Saída
# 2
# Pizza 40.00
# Suco 7.50	47.50
# 3
# Hamburguer 15.50
# Refrigerante 5.00
# Batata 8.00	28.50
# 4
# Café 4.50
# Pão de queijo 6.00
# Bolo 10.25
# Chá 3.75	24.50


class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, preco):
        self.itens.append(preco)

    def calcular_total(self):
        return sum(self.itens)


quantidade_pedidos = int(input("Informe quantidade de pedidos que serão realizados: ").strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input("Informe o pedido: ").strip().title().replace(",", ".")
    nome, preco = entrada.rsplit(" ", 1)
    pedido.adicionar_item(float(preco))

# Exibe o total com duas casas decimais
print(f"Total: R${pedido.calcular_total():.2f}")
