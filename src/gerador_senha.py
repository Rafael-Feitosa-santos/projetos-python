import secrets
import string


def gerador_senha(tamanho):
    chars = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(chars) for i in range(tamanho))
    print(senha)


try:
    quantidade_digitos = int(input("Informe quantos caracteres tenha a senha: "))
    gerador_senha(quantidade_digitos)

except ValueError:
    print("Entrada inválida!")
