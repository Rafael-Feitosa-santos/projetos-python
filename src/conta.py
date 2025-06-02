def sacar(saldo, saque, LIMITE_CHEQUE):
    if saque > 0 and saque <= saldo:
        saldo -= saque
        print(f"Saque R${saque:.2f} realizado com sucesso!")
    elif saldo + LIMITE_CHEQUE >= saque:
        limite_usado = saque - saldo
        saldo = 0
        LIMITE_CHEQUE -= limite_usado
        print(f"Saque de R${saque:.2f} realizado com sucesso! Limite do cheque especial utilizado: R${limite_usado:.2f}")
    else:
        print("Saldo insuficiente!")
    return saldo, LIMITE_CHEQUE

def depositar(saldo, deposito, LIMITE_CHEQUE, LIMITE_INICIAL):
    if deposito > 0:
        saldo += deposito
        print(f"Depósito de R${deposito:.2f} realizado com sucesso!")
        if saldo > 0:
            LIMITE_CHEQUE = LIMITE_INICIAL
    return saldo, LIMITE_CHEQUE

def consultar_saldo(saldo, LIMITE_CHEQUE):
    print(f"Saldo atual: R${saldo:.2f} (Limite do cheque especial: R${LIMITE_CHEQUE:.2f})")

saldo = 200
saque = 130
deposito = 300
LIMITE_CHEQUE = 100
LIMITE_INICIAL = 100

consultar_saldo(saldo, LIMITE_CHEQUE)
saldo, LIMITE_CHEQUE = sacar(saldo, saque, LIMITE_CHEQUE)
consultar_saldo(saldo, LIMITE_CHEQUE)
saldo, LIMITE_CHEQUE = sacar(saldo, saque, LIMITE_CHEQUE)
consultar_saldo(saldo, LIMITE_CHEQUE)
saque = 40
saldo, LIMITE_CHEQUE = sacar(saldo, saque, LIMITE_CHEQUE)
consultar_saldo(saldo, LIMITE_CHEQUE)
saldo, LIMITE_CHEQUE = depositar(saldo, deposito, LIMITE_CHEQUE, LIMITE_INICIAL)
consultar_saldo(saldo, LIMITE_CHEQUE)