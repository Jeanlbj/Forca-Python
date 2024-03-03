import random


class Menu:

    def __int__(self):
        pass

    def menu_jogo(self):
        print("\n=== Menu ===")
        print("1 - Digitar Letra")
        print("2 - Digitar Palavra")
        print("3 - Dica (Caso não tenha descoberto nenhuma letra)")
        print("============")

    def menu_categoria(self):
        print("\n=== Escolha de Categoria de Palavra ===")
        print("1 - Palavra Aleatoria")
        print("2 - Escolha a Categoria")
        print("============")

    def opcao_menu(self, palavra_aleatoria, palavra_jogo):
        while True:

            opcao_menu = str(input("\nDigite a opção desejada: "))

            erros = 0
            acertos = 0
            letras_digitadas = []

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

            self.menu_jogo()
