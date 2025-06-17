# Descrição
# Implemente uma classe Veiculo que represente um carro com marca, modelo e ano. Crie um método que verifique se o carro é considerado antigo (mais de 20 anos).
#
# Entrada
# Marca, modelo e ano do veículo.
# Saída
# "Veículo antigo" se o carro tiver mais de 20 anos.
# "Veículo novo" caso contrário.
# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
#
# Entrada	Saída
# Toyota
# Corolla
# 2000
#
# Veículo antigo
#
# Honda
# Civic
# 2005
#
# Veículo novo
#
# Ford
# Fiesta
# 1999
#
# Veículo antigo

from datetime import datetime

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def verificar_antiguidade(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self.ano
        if idade > 20:
            return "Veículo antigo"
        else:
            return "Veículo novo"

# Entrada direta
marca = input("Informe a marca: ").strip().title()
modelo = input("Informe o modelo: ").strip().title()
ano = int(input("Informe o ano: ").strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())
