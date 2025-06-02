class GerenteProjetos:
    def __init__(self, nome, projetos=None):
        if projetos is None:
            projetos = []
            self.nome = nome
            self.projetos = projetos

    def adicionar_projeto(self, projeto):
        self.projetos.append(projeto)
        print(f"O projeto '{projeto}' foi adicionado ao(á) gerente: {self.nome}")

    def listar_projetos(self):
        if self.projetos:
            print(f"\nProjeto do gerente: {self.nome} - Total de projetos: {len(self.projetos)}")
            for projeto in self.projetos:
                print(f"- {projeto}")


gerente = GerenteProjetos("Carlos")
gerente.adicionar_projeto("Projeto A")
gerente.adicionar_projeto("Projeto B")
gerente.adicionar_projeto("Projeto C")
gerente.adicionar_projeto("Projeto D")
gerente.listar_projetos()

print("\n===========================================================")

gerente2 = GerenteProjetos("Rafael")
gerente2.adicionar_projeto("Projeto Java")
gerente2.adicionar_projeto("Projeto Python")
gerente2.adicionar_projeto("Projeto de API")
gerente2.adicionar_projeto("Projeto Web")
gerente2.listar_projetos()

print("===========================================================")
