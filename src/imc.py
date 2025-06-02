def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc


def validar_entrada(valor):
    return float(valor.replace(",", "."))


try:
    print("===========================")
    print("Cálculo IMC".center(25))
    print("===========================")

    peso = validar_entrada(input("informe seu peso: "))
    altura = validar_entrada(input("informe sua altura: "))

    imc = calcular_imc(peso, altura)

    print(f"Seu imc é {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc <= 24.90:
        print("Classificação: Peso normal")
    elif imc <= 29.90:
        print("Classificação: Sobrepeso")
    elif imc <= 34.90:
        print("Classificação: Obesidade Grau I")
    elif imc <= 39.90:
        print("Classificação: Obesidade Grau II")
    else:
        print("Classificação: Obesidade Grau III ou Mórbita")

except ValueError:
    print("⚠️ Atenção: Erro de valor. Por favor, insira um número válido.")

except KeyboardInterrupt:
    print("\n⚠️ Execução interrompida pelo usuário. Tente novamente.")
