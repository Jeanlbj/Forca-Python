from Model.CategoriaEscolha import CategoriaEscolha
from Model.Menu import Menu


class Forca:
    def __init__(self):
        pass

    def jogar_forca(self):
        menu = Menu()
        categoria = CategoriaEscolha()

        print("=== JOGO DA FORCA ===")

        menu.menu_categoria()

        while True:

            opcao = int(input("\nEscolha o tipo de palavra conforme menu: "))
            if opcao != 1 and opcao != 2:
                print("Opção invalida, digite novamente.")

            if opcao == 1:
                palavra_aleatoria = categoria.escolha_aleatoria()
                break
            else:
                if opcao == 2:
                    palavra_aleatoria = categoria.escolha_categoria()
                    break

        palavra_jogo = []

        for i in palavra_aleatoria:
            palavra_jogo.append("*")

        erros = 0
        acertos = 0

        menu.menu_jogo()

        print(f"\nPalavra: {"".join(palavra_jogo)}, contém {len(palavra_jogo)} letras")

        print("\n============")

        menu.opcao_menu(palavra_aleatoria, palavra_jogo)

        print("\n============")

        jogar_novamente = str(input("\nDeseja jogar novamente (S/N): ")).upper()

        if jogar_novamente == "S":
            print()
            self.jogar_forca()
        else:
            print("\n=== Fim de Jogo ===")
            print("Deselvolvimento: Jean Lucas de Andrade Barbosa")
