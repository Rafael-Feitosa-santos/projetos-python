# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
#
# Entrada	Saída
# Camiseta	Produto disponível
# Jaqueta	Produto disponível
# Vestido	Produto esgotado

# Lista de produtos disponíveis no estoque
estoque = ["Camiseta", "Calça", "Tênis", "Boné", "Jaqueta"]

# Entrada do usuário
produto = input("Digite o produto: ").strip().title()

# Verifica se o produto está no estoque
if produto in estoque:
    print("Produto disponível")
else:
    print("Produto esgotado")
