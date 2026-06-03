import time


def validar_entrada(valor):
    return float(valor.replace(",", "."))


minutos = validar_entrada(input("Digite minutos: "))
segundos = int(minutos * 60)

while segundos > 0:
    minuto = segundos // 60
    segundo = segundos % 60

    print(f"\r{minuto:02d}:{segundo:02d}", end="", flush=True)
    time.sleep(1)
    segundos -= 1

print("\r            \rTempo esgotado!")
