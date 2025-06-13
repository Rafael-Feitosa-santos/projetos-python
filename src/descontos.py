def validar_entrada(valor):
    return float(valor.replace(",", "."))


descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "DESCONTO30": 0.30
}

try:
    preco = validar_entrada(input("Digite o preço do produto: ").strip())
    cupom = input("Digite o cupom de desconto: ").strip().upper().replace(" ", "")

    if cupom in descontos:
        desconto = descontos[cupom]
        preco_final = preco * (1 - desconto)
        print(f"====== Total: R${preco_final:.2f} ======")
    elif cupom == "":
        preco_final = preco
        print(f"====== Total: R${preco_final:.2f} ======")
    else:
        print("Cupom inválido")

except ValueError:
    print("Entrada inválida!")
