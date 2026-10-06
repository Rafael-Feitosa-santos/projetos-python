

primeira_palavra = input("Insira a primeira palavra: ").strip().lower()
segunda_palavra = input("Insira a segunda palavra: ").strip().lower()

anagrama = sorted(primeira_palavra) == sorted(segunda_palavra)

if anagrama:
    print("As palavras são anagramas!!")
else:
    print("Não são anagramas!")