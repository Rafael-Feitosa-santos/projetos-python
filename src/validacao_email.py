def validar_email(email):
    # Regra 1: Não pode conter espaços
    if " " in email:
        return "E-mail inválido"

    # Regra 2: Deve conter exatamente um "@"
    if email.count("@") != 1:
        return "E-mail inválido"

    # Posição do "@"
    posicao_arroba = email.index("@")

    # Regra 3: Não pode começar ou terminar com "@"
    if posicao_arroba == 0 or posicao_arroba == len(email) - 1:
        return "E-mail inválido"

    # Regra 4: Verificar se o domínio é válido (após o "@", deve haver pelo menos um ".")
    dominio = email[posicao_arroba + 1:]
    if "." not in dominio:
        return "E-mail inválido"

    return "E-mail válido"


# Entrada do usuário
email = input("Informe seu e-mail: ").strip()

# Saída
print(validar_email(email))
