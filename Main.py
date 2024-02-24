import random


def escolha_palavra():
    palavras = ["MAÇA", "BANANA", "LARANJA", "UVA", "MORANGO", "ABACAXI", "MELANCIA", "PERA", "KIWI", "LIMAO", "MANGA",
                "PESSEGO", "MELAO", "CEREJA", "AMEIXA", "GOIABA", "ABACATE", "FIGO", "PITAYA", "FRAMBOESA"]
    palavra_escolhida = palavras[random.randint(0, 19)]
    return palavra_escolhida


def menu():
    print("\n=== Menu ===")
    print("1 - Digitar Letra")
    print("2 - Digitar Palavra")
    print("3 - Dica (Caso não tenha descoberto nenhuma letra)")
    print("============")


def jogar_forca():
    palavra_aleatoria = escolha_palavra()
    palavra_jogo = []

    for i in palavra_aleatoria:
        palavra_jogo.append("*")

    erros = 0
    acertos = 0

    print("=== JOGO DA FORCA ===")

    menu()

    print(f"\nPalavra: {"".join(palavra_jogo)}, contém {len(palavra_jogo)} letras")

    letras_digitadas = []

    while True:

        opcao_menu = int(input("\nDigite a opção desejada: "))

        if opcao_menu == 1:

            letra = str(input("\nDigite a letra: ")).upper()

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
            if opcao_menu == 2:

                palavra = str(input("\nDigite a palavra: ")).upper()

                if palavra == palavra_aleatoria:
                    palavra_jogo = palavra

                    print(f"{"".join(palavra_jogo)}")
                    print("\n=== Você ganhou! ====")
                    break
                else:
                    print(f"A palavra certa era {palavra_aleatoria}")
                    print("\n=== Você perdeu! ===")
                    break

            else:
                if opcao_menu == 3 and acertos == 0:

                    acertos += 1
                    dica = palavra_aleatoria[random.randint(0, len(palavra_aleatoria) - 1)]

                    for i in range(len(palavra_jogo)):
                        if palavra_aleatoria[i] == dica:
                            palavra_jogo[i] = dica

                    print(f"\nA dica é a letra {dica}")
                    print(f"{"".join(palavra_jogo)}")
                else:
                    if opcao_menu == 3 and acertos > 0:

                        print("\nVocê não tem mais dicas")
                    else:
                        print("\nOpção errada, digite novamente")

    jogar_novamente = str(input("\nDeseja jogar novamente (S/N): ")).upper()

    if jogar_novamente == "S":
        print()
        jogar_forca()
    else:
        print("\n=== Fim de Jogo ===")


if __name__ == "__main__":
    jogar_forca()
