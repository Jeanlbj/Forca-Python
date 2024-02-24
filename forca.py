import random
from Model.CategoriaEscolha import CategoriaEscolha
from Model.Menu import Menu


def jogar_forca():
    menu = Menu()
    categoria = CategoriaEscolha()

    print("=== JOGO DA FORCA ===")

    menu.menu_categoria()

    flag_opcao = True

    while flag_opcao is True:

        opcao = int(input("\nEscolha o tipo de palavra conforme menu: "))
        if opcao != 1 and opcao != 2:
            print("Opção invalida, digite novamente.")

        if opcao == 1:
            palavra_aleatoria = categoria.escolha_aleatoria()
            flag_opcao = False
        else:
            if opcao == 2:
                palavra_aleatoria = categoria.escolha_categoria()
                flag_opcao = False

    palavra_jogo = []

    for i in palavra_aleatoria:
        palavra_jogo.append("*")

    erros = 0
    acertos = 0

    menu.menu_jogo()

    print(f"\nPalavra: {"".join(palavra_jogo)}, contém {len(palavra_jogo)} letras")

    print("\n============")

    letras_digitadas = []

    while True:

        opcao_menu = str(input("\nDigite a opção desejada: "))

        if opcao_menu == "1":

            letra = str(input("Digite a letra: ")).upper()

            print("\n============")

            if letra in letras_digitadas:
                print("Você já digitou essa letra")
                print(f"Letras digitadas: {letras_digitadas}")
            else:
                if letra in palavra_aleatoria:
                    letras_digitadas.append(letra)
                    acertos += 1

                    for i in range(len(palavra_jogo)):
                        if palavra_aleatoria[i] == letra:
                            palavra_jogo[i] = letra

                    print(f"\nVocê acertou a letra {letra}!")
                    print(f"{"".join(palavra_jogo)}")
                    print(f"Você tem {erros} erros, você pode errar até 6 vezes.")

                    if "".join(palavra_jogo) == palavra_aleatoria:
                        print("\n=== Você Ganhou! ===")
                        break
                else:
                    letras_digitadas.append(letra)
                    erros += 1

                    print(f"\nVocê errou, a letra {letra} não está na palavra!")
                    print(f"{"".join(palavra_jogo)}")
                    print(f"Você tem {erros} erros, você pode errar até 6 vezes.")

                    if erros > 5:
                        print("\n=== Você perdeu! ===")
                        break

        else:
            if opcao_menu == "2":

                palavra = str(input("Digite a palavra: ")).upper()

                print("\n============")

                if palavra == palavra_aleatoria:
                    palavra_jogo = palavra

                    print(f"\n{"".join(palavra_jogo)}")
                    print("\n=== Você ganhou! ===")
                    break
                else:
                    print(f"A palavra certa era {palavra_aleatoria}")
                    print("\n=== Você perdeu! ===")
                    break

            else:
                if opcao_menu == "3" and acertos == 0:

                    acertos += 1
                    dica = palavra_aleatoria[random.randint(0, len(palavra_aleatoria) - 1)]

                    for i in range(len(palavra_jogo)):
                        if palavra_aleatoria[i] == dica:
                            palavra_jogo[i] = dica

                    print(f"\nA dica é a letra {dica}")
                    print(f"{"".join(palavra_jogo)}")
                else:
                    if opcao_menu == "3" and acertos > 0:

                        print("Você não tem mais dicas")
                    else:
                        print("Opção errada, digite novamente como está no menu")

        menu.menu_jogo()

    print("\n============")

    jogar_novamente = str(input("\nDeseja jogar novamente (S/N): ")).upper()

    if jogar_novamente == "S":
        print()
        jogar_forca()
    else:
        print("\n=== Fim de Jogo ===")
        print("Deselvolvimento: Jean Lucas de Andrade Barbosa")


if __name__ == "__main__":
    jogar_forca()
