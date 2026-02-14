import requests


def buscar_pokemon(nome):
    url = f" https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        print("\n==== Dados do Pokémon ===")
        print(f"nome: {dados['name'].title()}")
        print(f"Altura: {dados['height']}")
        print(f"Peso: {dados['weight']}")
        print(f"Tipo: ")
        for tipo in dados['types']:
            print(f"- {tipo['type']['name']}")
    else:
        print("Pokémon não localizado")


pokemon = input("Digite o nomme do Pokémon: ").strip()

buscar_pokemon(pokemon)
