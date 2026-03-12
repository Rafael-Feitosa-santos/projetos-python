import time
import winsound
from datetime import datetime


def hora_brasilia():
    hora = datetime.now()
    return hora


def despertador(hora, minuto):
    print(f"\nDespertador programado para {hora:02d}:{minuto:02d}")
    while True:
        try:
            agora = hora_brasilia()
            if agora.hour == hora and agora.minute == minuto:
                for i in range(5):
                    print(" >>> 🔔 ACORDA!! 🔔 <<<")
                    winsound.Beep(1000, 2000)
                    time.sleep(1)
                break
            time.sleep(10)

        except KeyboardInterrupt:
            print("Programa finalizado pelo usuário!")


def entrada_dados():
    try:
        hora = int(input("Digite a hora para o despertador: "))
        minuto = int(input("Digite o minuto para o despertador: "))
        despertador(hora, minuto)

    except ValueError:
        print("Entrada inválida")
    except KeyboardInterrupt:
        print("\nPrograma finalizado pelo usuário!")


entrada_dados()
