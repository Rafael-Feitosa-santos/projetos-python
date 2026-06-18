def calculo_desconto(preco, desconto=10):
    desconto = preco * (1 - desconto / 100)
    return desconto


def validar_entrada(valor):
    return float(valor.replace(",", "."))


def formatacao_valor(valor):
    valor_formatado = f"{valor:,.2f}".replace(",", ".")
    valor_formatado = valor_formatado[::-1].replace(".", ",", 1)[::-1]
    return valor_formatado


while True:
    try:
        preco = validar_entrada(input("Digite o valor da venda: "))
        break
    except ValueError:
        print("Valor inválido")

desconto = input(
    "Digite o desconto (%) ou pressione Enter para 10%. Se não quiser desconto, digite N: "
).strip().lower()

if desconto == "":
    desconto = 10
elif desconto == "n":
    desconto = 0
else:
    desconto = validar_entrada(desconto)

preco_desconto = calculo_desconto(preco, desconto)

print(f"Valor com desconto R$ {formatacao_valor(preco_desconto)}")