class Projeto():
    def __init__(self, nome, descricao, gerente=None):
        self.nome = nome
        self.descricao = descricao
        self.gerente = gerente

    def __str__(self):
        if self.gerente:
            return f"Projeto: {self.nome} - {self.descricao} foi adicionado ao(á) gerente: {self.gerente}"
        return f"Projeto: {self.nome} - {self.descricao}"


class GerenteProjetos:
    def __init__(self, nome, projetos=None):
        if projetos is None:
            projetos = []
        self.nome = nome
        self.projetos = projetos

    def adicionar_projeto(self, projeto):
        projeto = Projeto(projeto.nome, projeto.descricao, self.nome)
        self.projetos.append(projeto)

    def listar_projetos(self):
        if self.projetos:
            print(f"\nProjeto do gerente: {self.nome} - Total de projetos: {len(self.projetos)}")
            for projeto in self.projetos:
                print(projeto)


projeto1 = Projeto("Sistema de vendas", "Desenvolvimento de um sistema para vendas online.")
projeto2 = Projeto("App de Finanças", "Aplicativo para controle financeiro pessoal.")

gerente = GerenteProjetos("Carlos")
gerente.adicionar_projeto(projeto1)
gerente.adicionar_projeto(projeto2)
gerente.listar_projetos()

print("\n===========================================================")

projeto3 = Projeto("App Fintech", "Aplicativo de banco digital.")

gerente2 = GerenteProjetos("Rafael")
gerente2.adicionar_projeto(projeto3)
gerente2.listar_projetos()

print("===========================================================")
