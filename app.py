class Livro:
    def __init__(self, titulo, autor, livro_id):
        self.titulo = titulo
        self.autor = autor
        self.livro_id = livro_id
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        else:
            return False

    def devolver(self):
        self.disponivel = True


class Membro:
    def __init__(self, nome, numero_membro):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico = []

    def emprestar_livro(self, livro):
        if livro.emprestar():
            self.historico.append(livro)
            return True
        else:
            return False

    def devolver_livro(self, livro):
        livro.devolver()
        self.historico.remove(livro)


class Biblioteca:
    def __init__(self):
        self.catalogo = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.catalogo[livro.livro_id] = livro

    def adicionar_membro(self, membro):
        self.membros[membro.numero_membro] = membro

    def emprestar_livro(self, livro_id, numero_membro):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(numero_membro)

        if livro and membro:
            return membro.emprestar_livro(livro)
        else:
            return False

    def devolver_livro(self, livro_id, numero_membro):
        livro = self.catalogo.get(livro_id)
        membro = self.membros.get(numero_membro)

        if livro and membro:
            membro.devolver_livro(livro)
            return True
        else:
            return False

    def pesquisar_livro(self, criterio, valor):
        resultados = []
        for livro in self.catalogo.values():
            if criterio == 'titulo' and valor.lower() in livro.titulo.lower():
                resultados.append(livro)
            elif criterio == 'autor' and valor.lower() in livro.autor.lower():
                resultados.append(livro)
            elif criterio == 'id' and str(valor) == livro.livro_id:
                resultados.append(livro)
        return resultados


# Interface de linha de comando simples
def main():
    biblioteca = Biblioteca()

    livro1 = Livro("Python Basics", "John Doe", "123")
    livro2 = Livro("Data Science 101", "Jane Smith", "456")
    livro3 = Livro("The Art of Programming", "Alan Turing", "789")

    membro1 = Membro("Alice", 1)
    membro2 = Membro("Bob", 2)

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    biblioteca.adicionar_membro(membro1)
    biblioteca.adicionar_membro(membro2)

    while True:
        print("\nMenu:")
        print("1. Emprestar Livro")
        print("2. Devolver Livro")
        print("3. Pesquisar Livro")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            livro_id = input("Digite o ID do livro: ")
            numero_membro = int(input("Digite o número do membro: "))
            if biblioteca.emprestar_livro(livro_id, numero_membro):
                print("Livro emprestado com sucesso.")
            else:
                print("Empréstimo falhou. Verifique o ID do livro e o número do membro.")

        elif escolha == "2":
            livro_id = input("Digite o ID do livro: ")
            numero_membro = int(input("Digite o número do membro: "))
            if biblioteca.devolver_livro(livro_id, numero_membro):
                print("Livro devolvido com sucesso.")
            else:
                print("Devolução falhou. Verifique o ID do livro e o número do membro.")

        elif escolha == "3":
            criterio = input("Digite o critério de pesquisa (titulo/autor/id): ")
            valor = input("Digite o valor de pesquisa: ")
            resultados = biblioteca.pesquisar_livro(criterio, valor)
            if resultados:
                print("\nResultados da pesquisa:")
                for livro in resultados:
                    print(f"Título: {livro.titulo}, Autor: {livro.autor}, ID: {livro.livro_id}")
            else:
                print("Nenhum resultado encontrado.")

        elif escolha == "4":
            print("Saindo do programa.")
            break

        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    main()
