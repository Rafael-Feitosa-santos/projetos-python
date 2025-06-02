nome = []

while True:
    entrada = input("Digite o nome(ou 'sair' pra parar): ").strip().title()
    if entrada.lower() == "sair":
        break
    if not entrada:
        print("⚠️ Não pode inserir valores vázios.")
        continue
    nome.append(entrada)

print("\nLista nomes: ")
if not nome:
    print("Lista está vázia!")
for item in nome:
    print(f"- {item}")